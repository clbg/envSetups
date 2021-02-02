"""to get platform of running platform"""
from .run_bash import run_zsh
from .color_log import log
import os

def soft_link(source_file:str, target_file:str):
    """use ln -s source target 
    source_file 
    
    DO NOT USE $HOME in path
    USE ~ INSTEAD

    e.g. ln -sf ~/envSetups/linuxSetup/linkFiles/HOME-.ssh-config ~/.ssh/config
    can use soft_link('~/envSetups/linuxSetup/linkFiles/Home.ssh-config', '~/.ssh/config')
    """
    source_file =  os.path.expanduser(source_file)
    target_file =  os.path.expanduser(target_file)
    if os.path.isfile(target_file) and not os.path.islink(target_file):
        log(f'renaming {target_file} {target_file}.bak')
        os.rename(target_file, target_file+'.bak')
    run_zsh(f'ln -sf {source_file} {target_file}')
