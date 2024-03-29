set -x
set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

err(){
    echo -e "${RED}$1 ${NC}" 
}

log(){
    echo -e "${GREEN}$1 ${NC}" 
}

prepare(){
    if  apt -v; then
        log "apt found installing prequisite"
        sudo apt install -y zsh git python3-pip
    else
        err "no package manager found, good luck"
    fi
}

install_distro(){
    if python3 -c 'import distro'; then 
        log 'distro found'
    else 
        log 'distro not installed, installing...'
        sudo pip3 install distro
    fi
}

clone_env(){
    cd ~
    if  [ -e envSetups ]; then
        log "Pulling envSetup package"
        git -C envSetups pull
        log "Pulling done"
    else
        log "Cloning envSetup package"
        git clone https://github.com/clbg/envSetups.git
        log "Cloning done"
    fi
}



prepare
install_distro

clone_env
cd envSetups
git config user.name 'charlie'
git config user.email 'spam@chengpeng.space'

python3 -m py-installer.install
