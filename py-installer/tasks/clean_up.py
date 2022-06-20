from ..utils.run_bash import run_zsh
from ..utils.color_log import log

def clean_up():
    log("cleaning up")
    run_zsh('brew cleanup --prune=all')
    run_zsh('yarn cache clean')
    #run_zsh('npm cache clean --force')
