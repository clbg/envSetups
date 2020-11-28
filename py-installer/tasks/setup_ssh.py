from ..utils.run_bash import run_bash, run_bash_as_sudo
from ..utils.soft_link import soft_link
from ..utils.color_log import log

PUBLIC_KEY_PATH = r'$HOME/envSetups/linuxSetup/linkFiles/key.pub'

def setup_ssh():
    log("Setting up ssh")
    log('Linking files')
    link_ssh_config_files()
    append_public_key()
    log("Setting up ssh done")


def append_public_key():
    log('appending key')
    if run_bash(f'grep -qiFf  {PUBLIC_KEY_PATH} /$HOME/.ssh/authorized_keys') != 0:
        log("appending key")
        run_bash(f'cat {PUBLIC_KEY_PATH} >> $HOME/.ssh/authorized_keys')
    else:
        log("key exists already, continue")


def link_ssh_config_files():
    log("linking .ssh/config file")
    run_bash('mkdir -p $HOME/.ssh')
    soft_link('~/envSetups/linuxSetup/linkFiles/HOME-.ssh-config', '~/.ssh/config')
    run_bash('touch ~/.ssh/config_local')

def setup_ssh_server():
    '''todo options for server'''
    run_bash_as_sudo(
        r"sed - i  's/^#\(AllowAgentForwarding\ yes\)/\1/' / etc/ssh/sshd_config")
