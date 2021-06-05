from .utils.running_platform import Distribution
from .utils.package_manager import PackageManager
from .utils.color_log import log
from .utils.env_vars import isEnvEquals

import os

PKGLIST_FOR_NATIVE_PKG_M_DICT = {
   # silver_searcher is code searcher https://github.com/ggreer/the_silver_searcher#installing
   Distribution.Amazon: '',
   Distribution.Debian: '',
   Distribution.Ubuntu: '',
   Distribution.Arch: '',
   Distribution.MacOS: 'google-chrome iterm2 karabiner-elements kicad kindle telegram wechat deepl',
}

class InstallerConfig(object):

    def __init__(self,dist:Distribution,  major_version:int) :
        self.dist=dist
        self.major_version= major_version

    def get_native_package_manager(self):
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

    def get_native_package_manager_install_list(self):
        return  PKGLIST_FOR_NATIVE_PKG_M_DICT[self.dist]

    def get_secondary_package_manager(self):
        if self.dist == Distribution.MacOS:
            return PackageManager.UnKnown
        if self.dist == Distribution.Windows:
            return PackageManager.UnKnown
        return PackageManager.LinuxBrew

    def get_secondary_package_manager_install_list(self):
        return ''

    def is_mirror_cn(self):
        """ get if is running in cn """
        if isEnvEquals('CN','Y'):
            return True
        else:
            return False

    def is_desk(self):
        if isEnvEquals('DSK','Y'):
            return True
        else:
            return False

