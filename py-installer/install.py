from distro import major_version
from .tasks.install_package import install_packages
from .tasks.setup_macos import setup_macos
from .tasks.setup_ssh import setup_ssh
from .tasks.setup_fzf import setup_fzf
from .tasks.setup_vim import setup_vim
from .tasks.setup_zsh import setup_zsh
from .utils.running_platform import Distribution, get_distribution, get_major_version 
from .installerConfig import InstallerConfig

dist = get_distribution()
major_version =  int(get_major_version())

installerConfig = InstallerConfig(dist,major_version)


setup_zsh()
install_packages(installerConfig)
setup_ssh()
setup_vim(dist)
setup_fzf()

if dist== Distribution.MacOS:
    setup_macos()
