#!/bin/bash
echo "linking .ssh/confg file"
mkdir -p $HOME/.ssh
ln -sf $HOME/envSetups/linuxSetup/linkFiles/HOME-.ssh-config $HOME/.ssh/config
 
echo "linking .zshrc file"
ln -sf $HOME/envSetups/linuxSetup/linkFiles/HOME-.zshrc $HOME/.zshrc
touch $HOME/.zshrc_local
mkdir -p $HOME/.config/pip

echo "linking .config/pip/pip.conf"
ln -sf $HOME/envSetups/linuxSetup/linkFiles/HOME-.config-pip-pip.conf $HOME/.config/pip/pip.conf

echo "linking home/bin"
ln -sf $HOME/envSetups/linuxSetup/bin $HOME/
mkdir -p $HOME/bin_local

echo "adding pulic key to authorized keys"


key_path=$HOME/envSetups/linuxSetup/linkFiles/key.pub 

f=$(cat $key_path)
if ! grep -qi "$f" $HOME/.ssh/authorized_keys; then
	cat $key_path >> $HOME/.ssh/authorized_keys
	echo "appending key"
else 
	echo "key exists continue"
fi
