import sys
from ..utils.package_manager import PackageManager, update_source
from ..utils.soft_link import soft_link
from ..utils.running_platform import Distribution
from ..utils.run_bash import run_zsh_as_sudo, run_zsh
from ..utils.color_log import log,err

NIX_PACKAGES_TO_INSTALL = "tmux vim git zsh curl wget mosh rsync \
        neovim nodejs autojump silver-searcher openssh eternal-terminal icdiff fzf"

def install_nix(dist:Distribution,pkg_m:PackageManager):
    if run_zsh('command -v nix-env')!=0:
        if dist == Distribution.MacOS:
            run_zsh('sh <(curl -L https://nixos.org/nix/install)  --darwin-use-unencrypted-nix-store-volume --no-daemon')
        else:
            run_zsh('sh <(curl -L https://nixos.org/nix/install) --no-daemon ')
    else:
        log('found nix')

    run_zsh('. ~/.nix-profile/etc/profile.d/nix.sh')
    #after install 
    log('updating source to 20.09')
    if dist == Distribution.MacOS:
        run_zsh('nix-channel --remove nixpkgs')
        run_zsh('nix-channel --add https://nixos.org/channels/nixpkgs-20.09-darwin  nixpkgs')
    else:
        run_zsh('nix-channel --remove nixpkgs')
        run_zsh('nix-channel --add https://nixos.org/channels/nixos-20.09 nixpkgs')
    run_zsh('nix-channel --update')


        # TODO gen dir 
        #$ mkdir /nix
        #$ chown alice /nix
        # TODO mirror to tuna 
        # err('change channel to tuna:')
        # err('nix-channel --add https://mirrors.tuna.tsinghua.edu.cn/nix-channels/nixpkgs-unstable nixpkgs')
        # err('nix-channel --update')
        # err('add binary cache, write following to ~/.config/nix/nix.conf :')
        # err('substituters = https://mirrors.tuna.tsinghua.edu.cn/nix-channels/store https://cache.nixos.org/')
        # err('exiting...')
        # sys.exit()

def install_nix_darwin():
    if run_zsh('command -v darwin-rebuild')!=0:
        log('darwin-nix not found, installing:')
        run_zsh('nix-build https://github.com/LnL7/nix-darwin/archive/master.tar.gz -A installer')
        run_zsh('yes | ./result/bin/darwin-installer')
    else:
        log('darwin-nix found')

    soft_link('~/envSetups/nixSetup/HOME-.config-nixpkgs-darwin-configuration.nix', '~/.nixpkgs/darwin-configuration.nix')
    run_zsh('nix-channel --update darwin ')
    run_zsh('darwin-rebuild switch')

def install_packages_with_nix():
        run_zsh(f'nix-env -i {NIX_PACKAGES_TO_INSTALL}')

def install_home_manager(dist:Distribution, pkg_m: PackageManager):
    if run_zsh('command -v home-manager')!=0:
        log('home manager not found, installing...')
        run_zsh('nix-channel --add https://github.com/nix-community/home-manager/archive/release-20.09.tar.gz home-manager')
        run_zsh('nix-channel --update')
        run_zsh("nix-shell '<home-manager>' -A install")
    else:
        log('home manager found.')

    if dist == Distribution.MacOS:
        soft_link('~/envSetups/nixSetup/HOME-.config-nixpkgs-home.macos.nix','~/.config/nixpkgs/home.nix')
    else:
        soft_link('~/envSetups/nixSetup/HOME-.config-nixpkgs-home.linux.nix','~/.config/nixpkgs/home.nix')
    run_zsh('home-manager switch')


def setup_nix(dist:Distribution, pkg_m: PackageManager):
    install_nix(dist,pkg_m)
    if dist == Distribution.MacOS :
        install_nix_darwin()
    install_home_manager(dist,pkg_m)

    log('setting up home manager...')
    run_zsh('home-manager switch')
    log('setting up home manage done')

    install_packages_with_nix()
# Uninstall:
## nix darwin
# nix-build https://github.com/LnL7/nix-darwin/archive/master.tar.gz -A uninstaller
# ./result/bin/darwin-uninstaller
## nix

# sudo rm -rf /nix/*
# rm -rf .nix*
# rm -rf .config/nixpkgs
