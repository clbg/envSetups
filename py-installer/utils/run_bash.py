'''running bash commands'''
import os
import subprocess
from sys import stdin
from ..utils.color_log import info
from ..utils.color_log import err,log

def run_zsh_as_sudo(cmd):
    '''run zsh command with sudo'''
    return run_zsh(f'sudo {cmd}')

def run_zsh(cmd):
    '''run zsh command'''
    info(f'running zsh:  {cmd}')

    process = subprocess.run('zsh' , input = bytes(cmd,'utf-8'), shell=True,check=False )

    return process.returncode
