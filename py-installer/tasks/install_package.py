import sys
from ..utils.package_manager import PackageManager, update_source
from ..utils.running_platform import Distribution
from ..utils.run_bash import run_bash_as_sudo, run_bash
from ..utils.color_log import log,err

NIX_PACKAGES_TO_INSTALL = "tmux vim git zsh curl wget mosh htop rsync \
        neovim nodejs autojump silver-searcher openssh eternal-terminal icdiff fzf"

PM_PKGLIST_DICT = {
   # silver_searcher is code searcher https://github.com/ggreer/the_silver_searcher#installing
    PackageManager.Pacman: 'python-pynvim ',
    PackageManager.Apt: 'python3-neovim ',
    PackageManager.Yum: '',
    PackageManager.Brew: 'google-chrome iterm2 karabiner-elements kicad kindle telegram wechat'
}

PIP_PKG_LIST = ''

BREW_BUNDLE_FILE = '~/envSetups/macosSetup/configFiles/BrewFile'

def prepare_package_manager(dist:Distribution, pkg_m:PackageManager):
    if pkg_m == PackageManager.Brew:
        #Install brew if not exist
        if run_bash('command -v brew')!=0:
            log('installing hoembrew...')
            install_homebrew()
            log('installing hoembrew done...')
    # TODO choco
 
def install_packages(dist:Distribution, pkg_m: PackageManager):
    install_with_nix(NIX_PACKAGES_TO_INSTALL,dist)
    pkg_list = PM_PKGLIST_DICT[pkg_m]
    prepare_package_manager(dist,pkg_m)
    update_source(pkg_m)
    install_packages_with_package_manager(pkg_list, pkg_m)
    install_pacakges_with_pip(PIP_PKG_LIST, pkg_m)
        
def install_packages_with_package_manager(package_list: str, pkg_m: PackageManager):
    '''install a list of package with package manager'''
    log('installing package list:')
    log(package_list)
    if pkg_m == PackageManager.Pacman:
        run_bash_as_sudo(f'pacman -s {package_list} --noconfirm')
    if pkg_m == PackageManager.Apt:
        run_bash_as_sudo(f'apt -y install {package_list}')
    if pkg_m == PackageManager.Yum:
        run_bash_as_sudo(f'yum -y install {package_list}')
    if pkg_m == PackageManager.Brew:
        run_bash(f'brew install {package_list}')
    # TODO choco

def install_with_nix(package_list:str,dist:Distribution):
    if run_bash('command -v nix-env')!=0:
        err('nix-env not installed, please run:')
        err('sh <(curl -L https://nixos.org/nix/install) --no-daemon ')
        err('change channel to tuna:')
        err('nix-channel --add https://mirrors.tuna.tsinghua.edu.cn/nix-channels/nixpkgs-unstable nixpkgs')
        err('nix-channel --update')
        err('add binary cache, write following to ~/.config/nix/nix.conf :')
        err('substituters = https://mirrors.tuna.tsinghua.edu.cn/nix-channels/store https://cache.nixos.org/')
        err('exiting...')
        sys.exit()
    else:
        log('found nix, installing...')
        run_bash(f'nix-env -i {package_list}')

def install_pacakges_with_pip(package_list:str, pkg_m: PackageManager):
    log('installing package list with pip3:')
    log(package_list)
    run_bash_as_sudo(f'pip3 install {package_list}')
    if pkg_m == PackageManager.Yum:
        run_bash_as_sudo('pip3 install git+https://github.com/jeffkaufman/icdiff.git')
    log('installing done')

def install_homebrew():
    run_bash('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
