'''running bash commands'''
import os
import sys
import subprocess
from sys import stdin
from ..utils.color_log import info
from ..utils.color_log import err,log
import pprint
import shlex

def run_zsh_as_sudo(cmd):
    '''run zsh command with sudo'''
    return run_zsh(f'sudo {cmd}')

def run_zsh(cmd):
    '''run zsh command'''
    info(f'running zsh:  {cmd}')

    process = subprocess.run('zsh' , input = bytes(cmd,'utf-8'), shell=True,check=False )

    return process.returncode

def source_file(filePath, savedVar=[]):
    '''source a file'''
    info(f'sourceing file: {filePath} with saving variables: {savedVar}')
    inherited_var_string = ''
    for var in savedVar:
        inherited_var_string = inherited_var_string + f'{var}={os.environ[var]} '

    info(f'inheriting variables: {inherited_var_string}')
    command = shlex.split(f"env -i {inherited_var_string} zsh -c 'source {filePath} && env'")
    proc = subprocess.Popen(command, stdout = subprocess.PIPE)
    for line in proc.stdout:
      (key, _, value) = line.decode().partition("=")
      key = key.strip()
      value = value.strip()
      log(f'exporting key: {key}, value:{value} valueEnd')
      os.environ[key] = value
    proc.communicate()
    log('full env:')
    pprint.pprint(dict(os.environ))

def export_env(env_name, env_value):
    log(f'exporting env {env_name} with value {env_value}')
    os.environ[env_name] = env_value

def exit_install(message):
    err(message)
    sys.exit()

