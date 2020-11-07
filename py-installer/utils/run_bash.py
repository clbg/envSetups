'''running bash commands'''
import os


def run_bash_as_sudo(cmd):
    '''run bash command with sudo'''
    return os.system(f'sudo {cmd}')


def run_bash(cmd):
    '''run bash command'''
    return os.system(cmd)
