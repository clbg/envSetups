import sys
from ..utils.package_manager import PackageManager, update_source
from ..utils.soft_link import soft_link
from ..utils.running_platform import Distribution
from ..utils.run_bash import run_zsh_as_sudo, run_zsh
from ..utils.color_log import log,err

BREW_BUNDLE_FILE = '~/envSetups/macosSetup/configFiles/BrewFile'

def install_nix_darwin():
    if run_zsh('command -v darwin-rebuild', True)!=0:
        log('installing nix-darwin ...')
        run_zsh('nix-build https://github.com/LnL7/nix-darwin/archive/master.tar.gz -A installer')
        run_zsh('./result/bin/darwin-installer')
        log('installing nix-darwin done')
    log('found nix-darwin')

def install_home_manager():
    err('TOOD')
    err('following:')
    err('nix-channel --add https://github.com/nix-community/home-manager/archive/release-20.09.tar.gz home-manager\
nix-channel --update')
    err("nix-shell '<home-manager>' -A install")

def prepare_home_manager(dist:Distribution,pkg_m:PackageManager):
    if dist == Distribution.MacOS :
        install_nix_darwin()
        soft_link('~/envSetups/nixSetup/HOME-.config-nixpkgs-darwin-configuration.nix',
                '~/.nixpkgs/darwin-configuration.nix')



    #soft_link('~/envSetups/nixSetup/HOME-.config-nixpkgs-home.nix','~/.config/nixpkgs/home.nix')

def setup_home_manager(dist:Distribution, pkg_m: PackageManager):
    log('setting up home manager...')
    prepare_home_manager(dist,pkg_m)
    run_zsh('home-manager switch')
    log('setting up home manage done')
