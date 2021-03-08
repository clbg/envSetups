from ..utils.run_bash import run_zsh
from ..utils.soft_link import soft_link
from ..utils.color_log import log 
def setup_zsh():
    log("Setting up ZSH")
    log("Installing Oh my ZSH")
    run_zsh('rm -rf ~/ohmyzsh')
    install_oh_my_zsh()
    link_zsh_files()
    chsh()
    log("Setting up ZSH done")

def install_oh_my_zsh():
    run_zsh('git -C ~  clone https://github.com/ohmyzsh/ohmyzsh.git')
    run_zsh('zsh ~/ohmyzsh/tools/install.sh',True)

def link_zsh_files():
    log('Linking files update your zshrc')
    soft_link('~/envSetups/linuxSetup/linkFiles/HOME-.zshrc', '~/.zshrc')

def chsh():
    log("changing default shell to zsh")
    run_zsh('chsh -s /bin/zsh')
    

