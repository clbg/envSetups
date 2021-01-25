"""get your package manager on running device"""
from enum import Enum
from .running_platform import Distribution
from .run_bash import run_zsh_as_sudo, run_zsh
from .color_log import log

class PackageManager(Enum):
    """This is a Package Manager Enum."""
    Apt = "apt"
    Brew = "brew"
    Choco = "choco"
    Pacman = "pacman"
    Yum = "yum"
    UnKnown = "unknown"


def get_package_manager(dist: Distribution):
    """get package manager like yum/pacman/apt/choco/brew"""
    if dist == Distribution.Amazon:
        return PackageManager.Yum
    if dist == Distribution.Arch:
        return PackageManager.Pacman
    if dist == Distribution.Debian or dist == Distribution.Ubuntu:
        return PackageManager.Apt
    if dist == Distribution.MacOS:
        return PackageManager.Brew
    if dist == Distribution.Windows:
        return PackageManager.Choco
    else:
        log("Unknown Package manager in your distribution:" + str(dist))
        return PackageManager.UnKnown


def update_source(pkg_m: PackageManager):
    """update source like apt update"""
    log("Updating your source")
    if pkg_m == PackageManager.Pacman:
        run_zsh_as_sudo('pacman -Syu - -noconfirm')
    elif pkg_m == PackageManager.Yum:
        run_zsh_as_sudo('yum -y update')
        run_zsh_as_sudo('yum - y upgrade')
        run_zsh_as_sudo('yum -y install epel-release')
    elif pkg_m == PackageManager.Apt:
        run_zsh_as_sudo('apt update')
    elif pkg_m == PackageManager.Brew:
        run_zsh('brew update')
    else:
        log("not support your platform:" + str(pkg_m))
    # todo choco
