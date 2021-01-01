from .tasks.install_package import install_packages
from .tasks.setup_ssh import setup_ssh
from .tasks.setup_zsh import setup_zsh
from .tasks.setup_vim import setup_vim
from .tasks.setup_macos import setup_macos
from .utils.running_platform import get_distribution,Distribution
from .utils.package_manager import get_package_manager

dist = get_distribution()
pkg_m = get_package_manager(dist)

install_packages(dist, pkg_m)
setup_ssh()
setup_zsh()
setup_vim(dist)

if dist== Distribution.MacOS:
    setup_macos()
