from ..utils.run_bash import run_zsh
from ..utils.color_log import log

def setup_fzf():
    log("setting up fzf with brew")
    run_zsh('brew install fzf ')
    run_zsh('$(brew --prefix)/opt/fzf/install --all')
