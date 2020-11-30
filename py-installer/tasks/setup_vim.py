from ..utils.run_bash import run_bash, run_bash_as_sudo
from ..utils.soft_link import soft_link
from ..utils.running_platform import Distribution
from ..utils.color_log import log

def setup_vim(dist:Distribution):
    install_neovim()
    setup_vimrc()
    install_vim_plug()
    update_vim_plug()


def install_neovim():
    log("TODO install neovim...")
    #TODO


def setup_vimrc():
    run_bash('mkdir -p ~/.config/nvim')
    run_bash('mkdir -p ~/.vim/undodir')
    soft_link('~/envSetups/linuxSetup/linkFiles/HOME-.vimrc','~/.vimrc')
    soft_link('~/.vimrc','~/.config/nvim/init.vim')


def install_vim_plug():
    # for vim
    run_bash('curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim')
    # for neovim
    run_bash(r"sh -c 'curl -fLo \"${XDG_DATA_HOME:-$HOME/.local/share}\"/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'")
    
def update_vim_plug():
    # https://github.com/junegunn/vim-plug/issues/225
    #for vim
    run_bash(r"vim -E -s -u '~/.vimrc'  +PlugInstall +qall")
    #for nvim
    # TODO
    run_bash('nvim --headless +PlugInstall +qall')