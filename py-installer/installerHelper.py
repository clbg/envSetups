from .utils.running_platform import Distribution
from .utils.package_manager import PackageManager
from .utils.color_log import log
from .installerConfig import InstallerConfig

import os
class InstallerHelper(object):

    def __init__(self,installerConfig:InstallerConfig) :
        self.installerConfig= installerConfig

    def install(self):
        pass




