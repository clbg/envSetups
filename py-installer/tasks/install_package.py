from ..utils.package_manager import PackageManager, update_source
from ..utils.running_platform import Distribution
from ..utils.run_bash import run_bash_as_sudo, run_bash
from ..utils.color_log import log

COMMON_PACKAGES_TO_INSTALL = "tmux vim git zsh curl wget mosh htop rsync neovim nodejs npm fzf"
PM_PKGLIST_DICT = {
   # silver_searcher is code searcher https://github.com/ggreer/the_silver_searcher#installing
    PackageManager.Pacman: f'{COMMON_PACKAGES_TO_INSTALL} openssh autojump python-pynvim the_silver_searcher',
    PackageManager.Apt: f'{COMMON_PACKAGES_TO_INSTALL} openssh-server autojump python3-neovim silversearcher-ag',
    PackageManager.Yum: f'{COMMON_PACKAGES_TO_INSTALL} openssh autojump-zsh python36-neovim the_silver_searcher',
    PackageManager.Brew: f'{COMMON_PACKAGES_TO_INSTALL} the_silver_searcher'
}

PIP_PKG_LIST = 'icdiff'

def install_packages(dist:Distribution, pkg_m: PackageManager):
    pkg_list = PM_PKGLIST_DICT[pkg_m]
    update_source(pkg_m)
    install_packages_with_package_manager(pkg_list, pkg_m)
    install_pacakges_with_pip(PIP_PKG_LIST, pkg_m)
    if dist == Distribution.Amazon:
        install_fzf_for_amzn()
        
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
    # todo choco

def install_pacakges_with_pip(package_list:str, pkg_m: PackageManager):
    log('installing package list with pip3:')
    log(package_list)
    run_bash_as_sudo(f'pip3 install {package_list}')
    if pkg_m == PackageManager.Yum:
        run_bash_as_sudo('pip3 install git+https://github.com/jeffkaufman/icdiff.git')
    log('installing done')

def install_fzf_for_amzn():
    log('installing fzf for amazon linux 2')
    run_bash('git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf')
    run_bash('~/.fzf/install')
