from ..utils.run_bash import run_bash
from ..utils.soft_link import soft_link

def setup_zsh():
    print("Setting up ZSH")
    print("Installing Oh my ZSH")
    install_oh_my_zsh()
    print('Linking files')
    link_zsh_files()
    run_bash('rm -rf ~/ohmyzsh')
    print("Setting up ZSH done")

def install_oh_my_zsh():
    run_bash('git -C ~  clone https://github.com/ohmyzsh/ohmyzsh.git')
    run_bash('bash ~/ohmyzsh/tools/install.sh')

def link_zsh_files():
    soft_link()

def link_zsh_files():
    print("update your zshrc")
    soft_link('~/envSetups/linuxSetup/linkFiles/HOME-.zshrc', '~/.zshrc')
