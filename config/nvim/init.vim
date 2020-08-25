"""""""""""""""""""""""""""""""""""""""""""""""""
" ,---.   .--.,---.  ,---..-./`) ,---.    ,---. "
" |    \  |  ||   /  |   |\ .-.')|    \  /    | "
" |  ,  \ |  ||  |   |  .'/ `-' \|  ,  \/  ,  | "
" |  |\_ \|  ||  | _ |  |  `-'`"`|  |\_   /|  | "
" |  _( )_\  ||  _( )_  |  .---. |  _( )_/ |  | "
" | (_ o _)  |\ (_ o._) /  |   | | (_ o _) |  | "
" |  (_,_)\  | \ (_,_) /   |   | |  (_,_)  |  | "
" |  |    |  |  \     /    |   | |  |      |  | "
" '--'    '--'   `---`     '---' '--'      '--' "
"                                               "
"""""""""""""""""""""""""""""""""""""""""""""""""

" basic
:imap ii <Esc>
set tabstop=4
set expandtab
set shiftwidth=4
set softtabstop=4
set encoding=utf-8
set fileencoding=utf-8
set number relativenumber " Show scrolling line nums

" Plugins will be downloaded under the specified directory.
call plug#begin('~/.config/nvim/plugged')

" Declare the list of plugins.
Plug 'majutsushi/tagbar'
Plug 'preservim/nerdtree'
Plug 'tpope/vim-fugitive'
Plug 'vim-airline/vim-airline'
Plug 'jmcantrell/vim-virtualenv'
Plug 'norcalli/nvim-colorizer.lua'
Plug 'hynek/vim-python-pep8-indent'
Plug 'vim-airline/vim-airline-themes'
Plug 'numirias/semshi', {'do': ':UpdateRemotePlugins'}
Plug 'xuhdev/vim-latex-live-preview', {'for': 'tex'}

" List ends here. Plugins become visible to Vim after this call.
call plug#end()

" theme
syntax on
set t_co=256
set encoding=utf-8
colorscheme fairyfloss
filetype plugin indent on
let g:airline_theme='fairyfloss'

" syntax highlighting
:set termguicolors
lua require'colorizer'.setup()
let g:python_highlight_all = 1
let g:Hexokinase_highlighters = ['foregroundfull']

" vim-latex-live-preview config
let g:livepreview_previewer = 'evince'
let g:livepreview_engine = 'xelatex'
map <Leader>p :LLPStartPreview<CR>

" toggle panes
map <Leader>n :NERDTreeToggle<CR>
nmap <Leader>t :TagbarToggle<CR>

" Luke Smith's configs.  "
" https://lukesmith.xyz/ "
set wildmode=longest,list,full
set splitbelow splitright

" Shortcutting split navigation, saving a keypress:
map <C-h> <C-w>h
map <C-j> <C-w>j
map <C-k> <C-w>k
map <C-l> <C-w>l

" File type settings
autocmd BufRead,BufNewFile /tmp/calcurse*,~/.calcurse/notes/* set filetype=markdown
autocmd BufWritePre * %s/\s\+$//e " Automatically delete all trailing whitespace on save.
autocmd BufRead,BufNewFile *.md set spell spelllang=en_us
autocmd BufRead,BufNewFile *.tex set spell spelllang=en_us

" Miguel Grinberg's configs
" https://gist.github.com/miguelgrinberg/527bb5a400791f89b3c4da4bd61222e4
" indent/unindent with tab/shift-tab
nmap <Tab> >>
imap <S-Tab> <Esc><<i
nmap <S-Tab> <<
