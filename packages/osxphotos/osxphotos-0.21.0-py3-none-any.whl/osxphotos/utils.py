import glob
import logging
import os.path
import platform
import subprocess
import urllib.parse
from pathlib import Path
from plistlib import load as plistload

import CoreFoundation
import objc
from Foundation import *

_DEBUG = False


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s",
)

if not _DEBUG:
    logging.disable(logging.DEBUG)


def _get_logger():
    """Used only for testing
    
    Returns:
        logging.Logger object -- logging.Logger object for osxphotos
    """
    return logging.Logger(__name__)


def _set_debug(debug):
    """ Enable or disable debug logging """
    global _DEBUG
    _DEBUG = debug
    if debug:
        logging.disable(logging.NOTSET)
    else:
        logging.disable(logging.DEBUG)


def _debug():
    """ returns True if debugging turned on (via _set_debug), otherwise, false """
    return _DEBUG


def _get_os_version():
    # returns tuple containing OS version
    # e.g. 10.13.6 = (10, 13, 6)
    version = platform.mac_ver()[0].split(".")
    if len(version) == 2:
        (ver, major) = version
        minor = "0"
    elif len(version) == 3:
        (ver, major, minor) = version
    else:
        raise (
            ValueError(
                f"Could not parse version string: {platform.mac_ver()} {version}"
            )
        )
    return (ver, major, minor)


def _check_file_exists(filename):
    """ returns true if file exists and is not a directory
        otherwise returns false """
    filename = os.path.abspath(filename)
    return os.path.exists(filename) and not os.path.isdir(filename)


def _get_resource_loc(model_id):
    """ returns folder_id and file_id needed to find location of edited photo """
    """ and live photos for version <= Photos 4.0 """
    # determine folder where Photos stores edited version
    # edited images are stored in:
    # Photos Library.photoslibrary/resources/media/version/XX/00/fullsizeoutput_Y.jpeg
    # where XX and Y are computed based on RKModelResources.modelId

    # file_id (Y in above example) is hex representation of model_id without leading 0x
    file_id = hex_id = hex(model_id)[2:]

    # folder_id (XX) in above example if first two chars of model_id converted to hex
    # and left padded with zeros if < 4 digits
    folder_id = hex_id.zfill(4)[0:2]

    return folder_id, file_id


def _dd_to_dms(dd):
    """ convert lat or lon in decimal degrees (dd) to degrees, minutes, seconds """
    """ return tuple of int(deg), int(min), float(sec) """
    dd = float(dd)
    negative = dd < 0
    dd = abs(dd)
    min_, sec_ = divmod(dd * 3600, 60)
    deg_, min_ = divmod(min_, 60)
    if negative:
        if deg_ > 0:
            deg_ = deg_ * -1
        elif min_ > 0:
            min_ = min_ * -1
        else:
            sec_ = sec_ * -1

    return int(deg_), int(min_), sec_


def _copy_file(src, dest):
    """ Copies a file from src path to dest path 
        Uses ditto to perform copy 
        Raises exception if copy fails or either path is None """

    if src is None or dest is None:
        raise ValueError("src and dest must not be None", src, dest)

    if not os.path.isfile(src):
        raise ValueError("src file does not appear to exist", src)

    # if error on copy, subprocess will raise CalledProcessError
    try:
        subprocess.run(
            ["/usr/bin/ditto", src, dest], check=True, stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError as e:
        logging.critical(
            f"ditto returned error: {e.returncode} {e.stderr.decode(sys.getfilesystemencoding()).rstrip()}"
        )
        raise e


def dd_to_dms_str(lat, lon):
    """ convert latitude, longitude in degrees to degrees, minutes, seconds as string """
    """ lat: latitude in degrees  """
    """ lon: longitude in degrees """
    """ returns: string tuple in format ("51 deg 30' 12.86\" N", "0 deg 7' 54.50\" W") """
    """ this is the same format used by exiftool's json format """
    # TODO: add this to readme

    lat_deg, lat_min, lat_sec = _dd_to_dms(lat)
    lon_deg, lon_min, lon_sec = _dd_to_dms(lon)

    lat_hemisphere = "N"
    if any([lat_deg < 0, lat_min < 0, lat_sec < 0]):
        lat_hemisphere = "S"

    lon_hemisphere = "E"
    if any([lon_deg < 0, lon_min < 0, lon_sec < 0]):
        lon_hemisphere = "W"

    lat_str = (
        f"{abs(lat_deg)} deg {abs(lat_min)}' {abs(lat_sec):.2f}\" {lat_hemisphere}"
    )
    lon_str = (
        f"{abs(lon_deg)} deg {abs(lon_min)}' {abs(lon_sec):.2f}\" {lon_hemisphere}"
    )

    return lat_str, lon_str


def get_system_library_path():
    """ return the path to the system Photos library as string """
    """ only works on MacOS 10.15+ """
    """ on earlier versions, will raise exception """
    _, major, _ = _get_os_version()
    if int(major) < 15:
        raise Exception(
            "get_system_library_path not implemented for MacOS < 10.15", major
        )

    plist_file = Path(
        str(Path.home())
        + "/Library/Containers/com.apple.photolibraryd/Data/Library/Preferences/com.apple.photolibraryd.plist"
    )
    if plist_file.is_file():
        with open(plist_file, "rb") as fp:
            pl = plistload(fp)
    else:
        logging.warning(f"could not find plist file: {str(plist_file)}")
        return None

    photospath = pl["SystemLibraryPath"]

    if photospath is not None:
        return photospath
    else:
        logging.warning("Could not get path to Photos database")
        return None


def get_last_library_path():
    """ returns the path to the last opened Photos library 
        If a library has never been opened, returns None """
    # TODO: Need a module level method for this and another PhotosDB method to get current library path
    plist_file = Path(
        str(Path.home())
        + "/Library/Containers/com.apple.Photos/Data/Library/Preferences/com.apple.Photos.plist"
    )
    if plist_file.is_file():
        with open(plist_file, "rb") as fp:
            pl = plistload(fp)
    else:
        logging.debug(f"could not find plist file: {str(plist_file)}")
        return None

    # get the IPXDefaultLibraryURLBookmark from com.apple.Photos.plist
    # this is a serialized CFData object
    photosurlref = pl["IPXDefaultLibraryURLBookmark"]

    if photosurlref is not None:
        # use CFURLCreateByResolvingBookmarkData to de-serialize bookmark data into a CFURLRef
        photosurl = CoreFoundation.CFURLCreateByResolvingBookmarkData(
            kCFAllocatorDefault, photosurlref, 0, None, None, None, None
        )

        # the CFURLRef we got is a sruct that python treats as an array
        # I'd like to pass this to CFURLGetFileSystemRepresentation to get the path but
        # CFURLGetFileSystemRepresentation barfs when it gets an array from python instead of expected struct
        # first element is the path string in form:
        # file:///Users/username/Pictures/Photos%20Library.photoslibrary/
        photosurlstr = photosurl[0].absoluteString() if photosurl[0] else None

        # now coerce the file URI back into an OS path
        # surely there must be a better way
        if photosurlstr is not None:
            photospath = os.path.normpath(
                urllib.parse.unquote(urllib.parse.urlparse(photosurlstr).path)
            )
        else:
            logging.warning(
                "Could not extract photos URL String from IPXDefaultLibraryURLBookmark"
            )
            return None

        return photospath
    else:
        logging.debug("Could not get path to Photos database")
        return None


def list_photo_libraries():
    """ returns list of Photos libraries found on the system """
    """ on MacOS < 10.15, this may omit some libraries """

    # On 10.15, mdfind appears to find all libraries
    # On older MacOS versions, mdfind appears to ignore some libraries
    # glob to find libraries in ~/Pictures then mdfind to find all the others
    # TODO: make this more robust
    lib_list = glob.glob(f"{str(Path.home())}/Pictures/*.photoslibrary")

    # On older OS, may not get all libraries so make sure we get the last one
    last_lib = get_last_library_path()
    if last_lib:
        lib_list.append(last_lib)

    output = subprocess.check_output(
        ["/usr/bin/mdfind", "-onlyin", "/", "-name", ".photoslibrary"]
    ).splitlines()
    for lib in output:
        lib_list.append(lib.decode("utf-8"))
    lib_list = list(set(lib_list))
    lib_list.sort()
    return lib_list


def create_path_by_date(dest, dt):
    """ Creates a path in dest folder in form dest/YYYY/MM/DD/
        dest: valid path as str
        dt: datetime.timetuple() object
        Checks to see if path exists, if it does, do nothing and return path
        If path does not exist, creates it and returns path"""
    if not os.path.isdir(dest):
        raise FileNotFoundError(f"dest {dest} must be valid path")
    yyyy, mm, dd = dt[0:3]
    yyyy = str(yyyy).zfill(4)
    mm = str(mm).zfill(2)
    dd = str(dd).zfill(2)
    new_dest = os.path.join(dest, yyyy, mm, dd)
    if not os.path.isdir(new_dest):
        os.makedirs(new_dest)
    return new_dest
