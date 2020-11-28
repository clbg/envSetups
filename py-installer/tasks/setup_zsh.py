from ..utils.run_bash import run_bash
from ..utils.soft_link import soft_link
from ..utils.color_log import log 
def setup_zsh():
    log("Setting up ZSH")
    log("Installing Oh my ZSH")
    install_oh_my_zsh()
    log('Linking files')
    link_zsh_files()
    run_bash('rm -rf ~/ohmyzsh')
    log("Setting up ZSH done")

def install_oh_my_zsh():
    run_bash('git -C ~  clone https://github.com/ohmyzsh/ohmyzsh.git')
    run_bash('bash ~/ohmyzsh/tools/install.sh')

def link_zsh_files():
    log("update your zshrc")
    soft_link('~/envSetups/linuxSetup/linkFiles/HOME-.zshrc', '~/.zshrc')
