syntax on

set nocompatible
set belloff=all
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent
set relativenumber
set nowrap
set smartcase
set noswapfile
set nobackup
set undodir=~/.vim/undodir
set undofile
set incsearch



" Specify a directory for plugins
" - For Neovim: stdpath('data') . '/plugged'
" - Avoid using standard Vim directory names like 'plugin'
call plug#begin('~/.vim/plugged')

"Plug 'scrooloose/nerdtree', { 'on':  'NERDTreeToggle' }

" FZF 
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'

" Theme 
Plug 'morhetz/gruvbox'

" fugitive
Plug 'tpope/vim-fugitive'
Plug 'vim-airline/vim-airline'

" Initialize plugin system
call plug#end()

set colorcolumn=120
"highlight ColorColumn ctermbg=0 guibg=lightgrey
colorscheme gruvbox
set background=dark




" Keybaord Remapping
let mapleader = " "
" resize split
map - <C-W>-
map + <C-W>+

nnoremap <leader>h :wincmd h<CR>
nnoremap <leader>j :wincmd j<CR>
nnoremap <leader>k :wincmd k<CR>
nnoremap <leader>l :wincmd l<CR>

" for fugitive
nmap <leader>gs :G<CR>

