#!/bin/bash
ln -sf $HOME/envSetups/linuxSetup/link_files/HOME-.ssh-config $HOME/.ssh/config
ln -sf $HOME/envSetups/linuxSetup/link_files/HOME-.zshrc $HOME/.zshrc
mkdir -p $HOME/.config/pip
ln -sf $HOME/envSetups/linuxSetup/link_files/HOME-.config-pip-pip.conf $HOME/.config/pip/pip.conf
