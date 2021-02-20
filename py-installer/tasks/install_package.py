import sys
from ..utils.package_manager import PackageManager, update_source
from ..utils.running_platform import Distribution
from ..utils.run_bash import run_zsh_as_sudo, run_zsh
from ..utils.color_log import log,err
from ..installerConfig import InstallerConfig

PM_PKGLIST_DICT = {
   # silver_searcher is code searcher https://github.com/ggreer/the_silver_searcher#installing
    PackageManager.Pacman: 'python-pynvim ',
    PackageManager.Apt: 'python3-neovim ',
    PackageManager.Yum: '',
    PackageManager.Brew: 'google-chrome iterm2 karabiner-elements kicad kindle telegram wechat',
    PackageManager.LinuxBrew: ''
}

PIP_PKG_LIST = ''

BREW_BUNDLE_FILE = '~/envSetups/macosSetup/configFiles/BrewFile'

def prepare_package_manager(dist:Distribution, pkg_m:PackageManager):
    if pkg_m == PackageManager.Brew or pkg_m== PackageManager.LinuxBrew:
        #Install brew if not exist
        if run_zsh('command -v brew')!=0:
            log('installing hoembrew...')
            install_homebrew()
            log('installing hoembrew done...')
    # TODO choco
 
def install_packages(installerConfig:InstallerConfig):
    dist = installerConfig.dist
    pkg_m = installerConfig.get_dist_package_manager()
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
        run_zsh_as_sudo(f'pacman -s {package_list} --noconfirm')
    if pkg_m == PackageManager.Apt:
        run_zsh_as_sudo(f'apt -y install {package_list}')
    if pkg_m == PackageManager.Yum:
        run_zsh_as_sudo(f'yum -y install {package_list}')
    if pkg_m == PackageManager.Brew:
        run_zsh(f'brew install {package_list}')
    if pkg_m == PackageManager.LinuxBrew:
        run_zsh(f'brew install {package_list}')
    # TODO choco

def install_pacakges_with_pip(package_list:str, pkg_m: PackageManager):
    log('installing package list with pip3:')
    log(package_list)
    run_zsh_as_sudo(f'pip3 install {package_list}')
    if pkg_m == PackageManager.Yum:
        run_zsh_as_sudo('pip3 install git+https://github.com/jeffkaufman/icdiff.git')
    log('installing done')

def install_homebrew():
    run_zsh('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
