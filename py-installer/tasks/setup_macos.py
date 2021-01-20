from ..utils.run_bash import run_bash, run_bash_as_sudo
from ..utils.soft_link import soft_link
from ..utils.running_platform import Distribution
from ..utils.color_log import log

def setup_macos():
    setup_karabiner()

def setup_karabiner():
    log('setting up.confg for karabiner')
    soft_link('~/envSetups/macosSetup/linkFiles/HOME-.config-karabiner','~/.config/karabiner')

def setup_yabai():
    log('setting up yabai')
    run_bash()
#def setup_vimrc():
#    run_bash('mkdir -p ~/.config/nvim')
#    run_bash('mkdir -p ~/.vim/undodir')
#    soft_link('~/envSetups/linuxSetup/linkFiles/HOME-.vimrc','~/.vimrc')
#    soft_link('~/.vimrc','~/.config/nvim/init.vim')
#    
#def update_vim_plug():
#    # https://github.com/junegunn/vim-plug/issues/225
#    #for vim
#    run_bash(r"vim -E -s -u '~/.vimrc'  +PlugInstall +qall")
#    #for nvim
#    # TODO
#    run_bash('nvim --headless +PlugInstall +qall')
#
