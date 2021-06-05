from ..installerConfig import InstallerConfig
from ..utils.color_log import log
from ..utils.package_manager import PackageManager, update_source
from ..utils.run_bash import exit_install, export_env, run_zsh, run_zsh_as_sudo
from ..utils.running_platform import Distribution

def install_homebrew(installerConfig:InstallerConfig):
    #Install brew if not exist
    if run_zsh('command -v brew', True)!=0:
        log('brew not found, installing hoembrew...')

        if(installerConfig.is_mirror_cn()):
            # setup mirror if cn
            #https://mirrors.tuna.tsinghua.edu.cn/help/homebrew/
            brew_type = "homebrew" if installerConfig.dist == Distribution.MacOS else "linuxbrew"
            export_env('HOMEBREW_BREW_GIT_REMOTE',"https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git")
            export_env('HOMEBREW_CORE_GIT_REMOTE',f'https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/${brew_type}-core.git')
            export_env('HOMEBREW_BOTTLE_DOMAIN',f'https://mirrors.tuna.tsinghua.edu.cn/${brew_type}-bottles')

        run_zsh('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')

        log('installing hoembrew done...')
        exit_install('brew installed, please get a new zsh. then rerun install script')
    else:
        log('brew found')

def prepare_package_manager(installerConfig:InstallerConfig):
    install_homebrew(installerConfig)
    update_source(installerConfig.get_native_package_manager())
    update_source(installerConfig.get_secondary_package_manager())
 
def install_packages(installerConfig:InstallerConfig):
    prepare_package_manager(installerConfig)
    #with native installer
    native_pkg_m = installerConfig.get_native_package_manager()
    native_install_pkg_list = installerConfig.get_native_package_manager_install_list()
    install_packages_with_package_manager(native_install_pkg_list, native_pkg_m)
    #with secondary installer
    secondary_pkg_m  = installerConfig.get_secondary_package_manager()
    secondary_install_pkg_list = installerConfig.get_secondary_package_manager_install_list()
    
    install_packages_with_package_manager(secondary_install_pkg_list,secondary_pkg_m)
        
def install_packages_with_package_manager(package_list: str, pkg_m: PackageManager):
    '''install a list of package with package manager'''
    log('installing package list:')
    if bool(package_list.strip()):
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
    else:
        log('empty list, returning')
 


        # TODO choco

#def install_pacakges_with_pip(package_list:str, pkg_m: PackageManager):
#    log('installing package list with pip3:')
#    log(package_list)
#    run_zsh_as_sudo(f'pip3 install {package_list}')
#    #if pkg_m == PackageManager.Yum:
#    #    run_zsh_as_sudo('pip3 install git+https://github.com/jeffkaufman/icdiff.git')
#    log('installing done')
#

