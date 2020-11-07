"""to get platform of running platform"""
from enum import Enum
import platform
import distro


class Distribution(Enum):
    """ find available distributions:
    https://distro.readthedocs.io/en/latest/
    Ctrl +F Distro ID"""
    Amazon = "amazon"
    Arch = "arch"
    Debian = "debian"
    MacOS = "macos"
    Ubuntu = "ubuntu"
    Windows = "windows"
    Unknow = "Unknow"


def get_distribution():
    """get distributions of windows/darwin/different linuxs"""
    if platform.system() == "Windows":
        return Distribution.Windows
    if platform.system() == "Darwin":
        return Distribution.MacOS
    else:
        dist = Distribution.Unknow
        try:
            dist = Distribution(distro.id())
        except ValueError:
            dist = Distribution.Unknow
        return dist
