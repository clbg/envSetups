from ..utils.run_bash import run_bash, run_bash_as_sudo

PUBLIC_KEY_PATH = r'$HOME/envSetups/linuxSetup/linkFiles/key.pub'


def setup_ssh():
    print("Setting up ssh")
    print('Linking files')
    link_ssh_config_files()
    append_public_key()
    print("Setting up ssh done")


def append_public_key():
    if run_bash(f'grep -qiFf  {PUBLIC_KEY_PATH} /$HOME/.ssh/authorized_keys') != 0:
        print("appending key")
        run_bash(f'cat {PUBLIC_KEY_PATH} >> $HOME/.ssh/authorized_keys')
    else:
        print("key exists already, continue")


def link_ssh_config_files():
    print("linking .ssh/config file")
    run_bash('mkdir -p $HOME/.ssh')
    run_bash('cp $HOME/.ssh/config $HOME/.ssh/config.bak')
    run_bash(
        'ln -sf $HOME/envSetups/linuxSetup/linkFiles/HOME-.ssh-config $HOME/.ssh/config')


def setup_ssh_server():
    run_bash_as_sudo(
        r"sed - i  's/^#\(AllowAgentForwarding\ yes\)/\1/' / etc/ssh/sshd_config")
