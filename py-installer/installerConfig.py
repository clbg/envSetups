from .utils.running_platform import Distribution
from .utils.package_manager import PackageManager
from .utils.color_log import log

import os
class InstallerConfig(object):

    def __init__(self,dist:Distribution,  major_version:int) :
        self.dist=dist
        self.major_version= major_version

    def get_dist_package_manager(self):
        """get package manager like yum/pacman/apt/choco/brew"""
        if self.dist == Distribution.Amazon:
           return PackageManager.Yum
        if self.dist == Distribution.Arch:
            return PackageManager.Pacman
        if self.dist == Distribution.Debian or self.dist == Distribution.Ubuntu:
            return PackageManager.Apt
        if self.dist == Distribution.MacOS:
            return PackageManager.Brew
        if self.dist == Distribution.Windows:
            return PackageManager.Choco
        else:
            log("Unknown Package manager in your self.distribution:" + str(self.dist))
            return PackageManager.UnKnown

    def is_mirror_cn(self):
        """ get if is running in cn """
        if os.getenv('ENV_SETUP_MIRROR') == 'CN':
            return True
        else:
            return False




