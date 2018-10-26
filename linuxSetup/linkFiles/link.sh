#!/bin/bash

echo "linking .ssh/confg file"
mkdir -p $HOME/.ssh
ln -sf $HOME/envSetups/linuxSetup/link_files/HOME-.ssh-config $HOME/.ssh/config
 
echo "linking .zshrc file"
ln -sf $HOME/envSetups/linuxSetup/link_files/HOME-.zshrc $HOME/.zshrc
mkdir -p $HOME/.config/pip

echo "linking .config/pip/pip.conf"
ln -sf $HOME/envSetups/linuxSetup/link_files/HOME-.config-pip-pip.conf $HOME/.config/pip/pip.conf
