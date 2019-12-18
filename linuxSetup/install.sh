DIST=
PKG_M=

DIST_ARCH="Arch"
DIST_MACOS="MacOS"
DIST_DEBIAN="Debain"
DIST_CENTOS="CentOS"
DIST_KALI="Kali"
DIST_UBUNTU="Ubuntu"
DIST_PVE="Proxmox"

PKG_M_APT="apt"
PKG_M_PACMAN="pacman"
PKG_M_YUM="yum"

log(){
    RED='\033[0;31m'
    GREEN='\033[0;32m'
    NC='\033[0m' # No Color

    echo -e "${GREEN}$1 ${NC}" 
}

set_sys_var(){
    if  grep -Eqi "manjaro|Arch" /etc/issue ; then
        DIST=$DIST_ARCH
        PKG_M=$PKG_M_PACMAN
        return 0
    elif grep -Eqi "centos|red hat|redhat" /proc/version;  then
        DIST=$DIST_CENTOS
        PKG_M=$PKG_M_YUM
        return 0
    elif grep -Eqi "Kali GNU" /etc/issue; then      
        DIST=$DIST_KALI
        PKG_M=$PKG_M_APT
    elif grep -Eqi "ubuntu" /etc/issue; then
        DIST=$DIST_UBUNTU
        PKG_M=$PKG_M_APT
    elif grep -Eqi "debian|raspbian" /etc/issue; then
        DIST=$DIST_DEBIAN
        PKG_M=$PKG_M_APT
    elif grep -Eqi "PVE" /proc/version; then
        DIST=$DIST_PVE
        PKG_M=$PKG_M_APT
    fi
}

check_arch(){
    set_sys_var
    log "Your system is $DIST"
    log "Your package manager is $PKG_M"
}

exe(){
    if [ `whoami` == 'root' ];then
        $1
    else
        sudo $1
    fi
}

update_source(){
    log "Updating your source"
    #todo macos and centos/rhel
    if [[ $PKG_M == $PKG_M_PACMAN ]]; then
        exe "pacman -Syu --noconfirm"
    elif [[ $PKG_M == $PKG_M_APT ]]; then
        exe "apt update "
    fi
    log "Updating done"
}

install_soft(){
    log "Installing softwares"
    common_soft_list="tmux vim git zsh autojump curl wget "
    
if [[ $PKG_M == $PKG_M_PACMAN ]]; then
        exe "pacman -S $common_soft_list openssh  --noconfirm"
    elif [[ $PKG_M == $PKG_M_APT ]]; then
        exe "apt -y install $common_soft_list openssh-server curl wget"
    fi
    log "Installing done"
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

setup_zsh(){
    log "Setting up ZSH"
    log "Installing Oh my ZSH"
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
    log "Linking files"
    sh ~/envSetups/linuxSetup/linkFiles/link.sh
    log "Setting up ZSH done"
}


#Start of execute"
log "Start env setup"

check_arch
update_source
install_soft
clone_env
setup_zsh


log "All Installation done! good luck && bye"



