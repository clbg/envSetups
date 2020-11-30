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


" Keybaord Remapping
let mapleader = " "

" Specify a directory for plugins
" - For Neovim: stdpath('data') . '/plugged'
" - Avoid using standard Vim directory names like 'plugin'
call plug#begin('~/.vim/plugged')
"Nerd tree
Plug 'scrooloose/nerdtree'
" FZF 
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
"{{{
  nnoremap <silent> <leader><space> :Files<CR>
  nnoremap <silent> <leader>a :Buffers<CR>
  nnoremap <silent> <leader>A :Windows<CR>
  nnoremap <silent> <leader>; :BLines<CR>
  nnoremap <silent> <leader>o :BTags<CR>
  nnoremap <silent> <leader>O :Tags<CR>
  nnoremap <silent> <leader>? :History<CR>
 " nnoremap <silent> <leader>. :AgIn 

  nnoremap <silent> K :call SearchWordWithAg()<CR>
  vnoremap <silent> K :call SearchVisualSelectionWithAg()<CR>
  nnoremap <silent> <leader>gl :Commits<CR>
  nnoremap <silent> <leader>ga :BCommits<CR>
  nnoremap <silent> <leader>ft :Filetypes<CR>
"}}}

Plug 'junegunn/fzf.vim'
" Theme 
Plug 'morhetz/gruvbox'
" fugitive
Plug 'tpope/vim-fugitive'
Plug 'vim-airline/vim-airline'

if has("nvim")
    " lsp
    "Plug 'neovim/nvim-lspconfig'
endif

"coc
if has("nvim")
    Plug 'neoclide/coc.nvim', {'branch': 'release'}
endif

call plug#end()

set colorcolumn=120
"highlight ColorColumn ctermbg=0 guibg=lightgrey
colorscheme gruvbox
set background=dark




" resize split
map - <C-W>-
map + <C-W>+

nnoremap <leader>h :wincmd h<CR>
nnoremap <leader>j :wincmd j<CR>
nnoremap <leader>k :wincmd k<CR>
nnoremap <leader>l :wincmd l<CR>

" for fugitive
nmap <leader>gs :G<CR>

" for nerdTree
map <C-n> :NERDTreeToggle<CR>

