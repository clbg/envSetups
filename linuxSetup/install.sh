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


AIRFLOW_WORKER=false
DOCKER=false

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

update_source(){
    log "Updating your source"
    #todo macos and centos/rhel
    if [[ $PKG_M == $PKG_M_PACMAN ]]; then
        sudo pacman -Syu --noconfirm
    elif [[ $PKG_M == $PKG_M_APT ]]; then
        sudo apt update
    elif [[ $PKG_M == $PKG_M_YUM ]]; then
	sudo yum -y update && yum -y upgrade
        sudo yum -y install epel-release
    fi
    log "Updating done"
}

install_soft(){
    log "Installing softwares"
    common_soft_list="tmux vim git zsh curl wget"
    
if [[ $PKG_M == $PKG_M_PACMAN ]]; then
        sudo pacman -S $common_soft_list openssh  autojump --noconfirm
    elif [[ $PKG_M == $PKG_M_APT ]]; then
        sudo apt -y install $common_soft_list openssh-server autojump curl wget
    elif [[ $PKG_M == $PKG_M_YUM ]]; then
	sudo yum -y install $common_soft_list openssh autojump-zsh
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
    git -C ~  clone https://github.com/ohmyzsh/ohmyzsh.git
    bash ~/ohmyzsh/tools/install.sh
    log "Linking files"
    sh ~/envSetups/linuxSetup/linkFiles/link.sh
    rm -rf ~/ohmyzsh
    log "Setting up ZSH done"
}


user_create(){
    log "Creating Users"
    log "Creating airflow-worker"
    sudo useradd  airflow-worker -m -s /bin/bash
    ssh_dir="/home/airflow-worker/.ssh"
    pub_key_path="$HOME/envSetups/linuxSetup/linkFiles/deploy.pub"
    sudo mkdir $ssh_dir
    if ! sudo grep -qiFf $pub_key_path  $ssh_dir/authorized_keys; then
        cat $pub_key_path | sudo tee  $ssh_dir/authorized_keys
        echo "appending key"
    else
        echo "key exists continue"
    fi
    sudo chown -R airflow-worker:airflow-worker $ssh_dir
    sudo chmod 700  $ssh_dir
    sudo su  - airflow-worker -c  "echo 'PATH=\$HOME/.local/bin:\$PATH' >> .bashrc "

}

install_docker(){
    log "installing docker"
    bash -c "$(curl -fsSL https://get.docker.com -o get-docker.sh)"

    log "install done"
}


while getopts 'wd' OPTION; do
  case "$OPTION" in
    w)
      echo "worker machine"
      AIRFLOW_WORKER=true
      ;;
    d)
      echo "docker machine"
      DOCKER=true
      ;;
    ?)
      echo "script usage: $(basename $0) [-w] " >&2
      echo " -w  : install on airflow worker machine" >&2
      echo " -d  : install docker" >&2

      exit 1
      ;;
  esac
done
shift "$(($OPTIND -1))"

log "Start env setup"
if [ "$AIRFLOW_WORKER" = true ] ; then
    user_create
fi



check_arch
update_source
install_soft
clone_env
setup_zsh

if [ "$DOCKER" = true ] ; then
    install_docker
fi

log "All Installation done! good luck && bye"

