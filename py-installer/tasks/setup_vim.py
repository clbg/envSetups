from ..utils.run_bash import run_zsh, run_zsh_as_sudo
from ..utils.soft_link import soft_link
from ..utils.running_platform import Distribution
from ..utils.color_log import log

def setup_vim(dist:Distribution):
    setup_vimrc()
    install_vim_plug()
    update_vim_plug()

def install_neovim():
    run_zsh('brew install --HEAD neovim')

def setup_vimrc():
    run_zsh('mkdir -p ~/.config/nvim')
    run_zsh('mkdir -p ~/.vim/undodir')
    soft_link('~/envSetups/linuxSetup/linkFiles/HOME-.vimrc','~/.vimrc')
    soft_link('~/.vimrc','~/.config/nvim/init.vim')


def install_vim_plug():
    # for vim
    run_zsh('curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim')
    # for neovim
    run_zsh(r"sh -c 'curl -fLo ${XDG_DATA_HOME:-$HOME/.local/share}/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'")
    
def update_vim_plug():
    # https://github.com/junegunn/vim-plug/issues/225
    #for nvim
    # TODO
    log('upgrading Plugd')
    run_zsh('nvim --headless +PlugUpgrade +qa')
    log('updating Plugd')
    run_zsh('nvim --headless +PlugUpdate +qa')
    log('installling Plugd')
    run_zsh('nvim --headless +PlugInstall +qa')

