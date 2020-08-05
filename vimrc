""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" ,---.  ,---..-./`) ,---.    ,---..-------.        _______    "
" |   /  |   |\ .-.')|    \  /    ||  _ _   \      /   __  \   "
" |  |   |  .'/ `-' \|  ,  \/  ,  || ( ' )  |     | ,_/  \__)  "
" |  | _ |  |  `-'`"`|  |\_   /|  ||(_ o _) /   ,-./  )        "
" |  _( )_  |  .---. |  _( )_/ |  || (_,_).' __ \  '_ '`)      "
" \ (_ o._) /  |   | | (_ o _) |  ||  |\ \  |  | > (_)  )  __  "
"  \ (_,_) /   |   | |  (_,_)  |  ||  | \ `'   /(  .  .-'_/  ) "
"   \     /    |   | |  |      |  ||  |  \    /  `-'`-'     /  "
"    `---`     '---' '--'      '--'''-'   `'-'     `._____.'   "
"                                                              "
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""
" Basic Config "
"              "
""""""""""""""""

set number relativenumber " Show scrolling line nums
:imap ;; <Esc>
syntax on
set encoding=utf-8
filetype plugin indent on

"""""""""""
" Plugins "
"         "
"""""""""""

" Plugins will be downloaded under the specified directory.
call plug#begin('~/.vim/plugged')

" Declare the list of plugins.
Plug 'preservim/nerdtree'
Plug 'vim-python/python-syntax'
Plug 'joshdick/onedark.vim'
Plug 'arcticicestudio/nord-vim'
Plug 'rrethy/vim-hexokinase', { 'do': 'make hexokinase'}
Plug 'terryma/vim-multiple-cursors'
Plug 'hynek/vim-python-pep8-indent'
Plug 'majutsushi/tagbar'
Plug 'xuhdev/vim-latex-live-preview', { 'for' : 'tex' }

" List ends here. Plugins become visible to Vim after this call.
call plug#end()

let g:python_highlight_all = 1

let g:onedark_termcolors = 256
colorscheme onedark

:set termguicolors
let g:Hexokinase_highlighters = ['foregroundfull']

map <C-x> :NERDTreeToggle<CR>
nmap <F8> :TagbarToggle<CR>

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Powerline config. Credit to Paul W. Frields (Fedora Magazine): "
" https://fedoramagazine.org/add-power-terminal-powerline/       "
"                                                                "
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

python3 from powerline.vim import setup as powerline_setup
python3 powerline_setup()
python3 del powerline_setup
set laststatus=2 " Always display the statusline in all windows
set showtabline=2 " Always display the tabline, even if there is only one tab
set noshowmode " Hide the default mode text (e.g. -- INSERT -- below the statusline)
set t_Co=256

""""""""""""""""""""""""""
" Luke Smith's configs.  "
" https://lukesmith.xyz/ "
"                        "
""""""""""""""""""""""""""

set wildmode=longest,list,full
set splitbelow splitright

" Shortcutting split navigation, saving a keypress:
map <C-h> <C-w>h
map <C-j> <C-w>j
map <C-k> <C-w>k
map <C-l> <C-w>l

" Calcurse markdown setting
autocmd BufRead,BufNewFile /tmp/calcurse*,~/.calcurse/notes/* set filetype=markdown

" Copy selected text to system clipboard (requires gvim installed).
vnoremap <C-c> '*Y: let @+=@*<CR>
map <C-p> "+P

" Automatically delete all trailing whitespace on save.
autocmd BufWritePre * %s/\s\+$//e
