"""get your package manager on running device"""
from enum import Enum
from .running_platform import Distribution
from .run_bash import run_bash_as_sudo, run_bash


class PackageManager(Enum):
    """This is a Package Manager Enum."""
    Apt = "apt"
    Brew = "brew"
    Choco = "choco"
    Pacman = "pacman"
    Yum = "yum"
    UnKnow = "unknow"


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
        print("Unknow Package manager in your distribution:" + str(dist))
        return PackageManager.UnKnow


def update_source(pkg_m: PackageManager):
    """update source like apt update"""
    print("Updating your source")
    if pkg_m == PackageManager.Pacman:
        run_bash_as_sudo('pacman -Syu - -noconfirm')
    if pkg_m == PackageManager.Yum:
        run_bash_as_sudo('yum -y update')
        run_bash_as_sudo('yum - y upgrade')
        run_bash_as_sudo('yum -y install epel-release')
    if pkg_m == PackageManager.Apt:
        run_bash_as_sudo('apt update')
    if pkg_m == PackageManager.Brew:
        run_bash('brew update')
    else:
        print("not support your platform:" + str(pkg_m))
    # todo choco
