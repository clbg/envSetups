from ..utils.run_bash import run_zsh, exit_install
import os
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
    soft_link('~/envSetups/linuxSetup/bin', '~/bin_local')

def chsh():
    if 'zsh' not in os.getenv('SHELL'):
        log('zsh is not your default shell, changing with chsh')
        #run_zsh_interactive('chsh -s /bin/zsh')
        exit_install('change your default shell to zsh using `chsh -s /bin/zsh`, and re-login, then curl -sL https://chengpeng.space/i | zsh')
    else:
        log("you are under zsh")
    

