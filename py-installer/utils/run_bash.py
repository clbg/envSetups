'''running bash commands'''
import os
from ..utils.color_log import info

def run_bash_as_sudo(cmd):
    '''run bash command with sudo'''
    return os.system(f'sudo {cmd}')

def run_bash(cmd):
    '''run bash command'''
    info(f'\t\t{cmd}')
    return os.system(cmd)
