#!/usr/bin/env bash

check_is_arch(){
	echo "checking if your system is Arch"
	local n=$(exe "cat /etc/issue" | sed -n "/Arch/p" | wc -l)
	if [ $n == 1 ]; then
		echo "fond arch in /etc/issue"
		return 0
	else
		echo "not fond arch in /etc/issue"
		return 1
	fi
}

check_sys(){
    local checkType=$1
    local value=$2

    local release=''
    local systemPackage=''

    if [[ -f /etc/redhat-release ]]; then
        release="centos"
        systemPackage="yum"
    elif  check_is_arch ;then
	echo "your system is arch!, using pacman!"
        release="arch"
        systemPackage="pacman"
    elif grep -Eqi "Kali GNU" /etc/issue; then	    
	echo "your system is kali gnu, using apt!"
	release="kali"
	systemPackage="apt"
    elif grep -Eqi "ubuntu" /etc/issue; then
	echo "your system is ubuntu , using apt!"
        release="ubuntu"
        systemPackage="apt"
    elif grep -Eqi "debian|raspbian" /etc/issue; then
        release="debian"
        systemPackage="apt"
    elif grep -Eqi "centos|red hat|redhat" /etc/issue; then
        release="centos"
        systemPackage="yum"
    elif grep -Eqi "debian|raspbian" /proc/version; then
        release="debian"
       systemPackage="apt"
    elif grep -Eqi "centos|red hat|redhat" /proc/version; then
        release="centos"
        systemPackage="yum"
    fi

    if [[ "${checkType}" == "sysRelease" ]]; then
        if [ "${value}" == "${release}" ]; then
            return 0
        else
            return 1
        fi
    elif [[ "${checkType}" == "packageManager" ]]; then
        if [ "${value}" == "${systemPackage}" ]; then
            return 0
        else
            return 1
        fi
    fi
}


exe(){
	if [ `whoami` == 'root' ];then
		$1
	else
		sudo $1
	fi
}


update_source(){
	if check_sys sysRelease arch; then
		#todo sed multiple times ?
		exe `sed '1 iServer = https://mirrors.tuna.tsinghua.edu.cn/archlinux/$repo/os/$arch' -i /etc/pacman.d/mirrorlist `
		exe "pacman -Syu --noconfirm"
	elif check_sys sysRelease kali; then
		exe `sed -e "s/http\.kali\.org/mirrors.neusoft.edu.cn/g" -i /etc/apt/sources.list `
		exe "apt update "
	elif check_sys sysRelease ubuntu ; then
		exe `sed -e "s/archive\.ubuntu\.com/mirrors.tuna.tsinghua.edu.cn/g" -i /etc/apt/sources.list `
		exe "apt update"
	fi

}

install_soft(){
	if check_sys packageManager pacman; then
		exe "pacman -S tmux vim git zsh  openssh --noconfirm"
	elif check_sys packageManager apt; then
	    	exe 'apt -y install tmux vim git zsh ssh curl wget '
	fi
}


clone_env(){
	cd ~
	if  [ -e envSetups ]; then
		git -C envSetups pull
	else
		git clone https://github.com/pengchengbuaa/envSetups.git
	fi
}

echo "111111 updating sorce"
update_source
echo "222222 installing software"
install_soft
echo "333333 cloneing envsetup"
clone_env


echo "444444 installing zsh"
sh ~/envSetups/linuxSetup/shellSetup/ohmyzsh-install
echo "555555 copying linkfiles"
sh ~/envSetups/linuxSetup/linkFiles/link.sh
