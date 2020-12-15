set -x

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color


log(){
    echo -e "${GREEN}$1 ${NC}" 
}

clone_env(){
    cd ~
    if  [ -e envSetups ]; then
        log "Pulling envSetup package"
        git -C envSetups pull
        log "Pulling done"
    else
        log "Cloning envSetup package"
        git clone https://github.com/pengchengbuaa/envSetups.git
        log "Cloning done"
    fi
}


clone_env
cd envSetups
git config user.name 'charlie'
git config user.email 'spam@chengpeng.space'
sudo pip3 install distro
python3 -m py-installer.install
