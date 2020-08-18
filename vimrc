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

" basic
:imap ii <Esc>
set tabstop=4
set expandtab
set shiftwidth=4
set softtabstop=4
set encoding=utf-8
set fileencoding=utf-8
set number relativenumber " Show scrolling line nums
set spell spelllang=en_us

" plugins
let need_to_install_plugins = 0
if empty(glob('~/.vim/autoload/plug.vim'))
    silent !curl -fLo ~/.vim/autoload/plug.vim --create-dirs
        \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
    "autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
    let need_to_install_plugins = 1
endif

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
Plug 'jmcantrell/vim-virtualenv'
Plug 'tpope/vim-fugitive'

" List ends here. Plugins become visible to Vim after this call.
call plug#end()

if need_to_install_plugins == 1
    echo "Installing plugins..."
    silent! PlugInstall
    echo "Done!"
    q
endif

" theme
syntax on
set encoding=utf-8
colorscheme onedark
filetype plugin indent on
let g:onedark_termcolors = 256

" syntax highlighting
:set termguicolors
let g:python_highlight_all = 1
let g:Hexokinase_highlighters = ['foregroundfull']

" vim-latex-live-preview config
let g:livepreview_previewer = 'evince'
let g:livepreview_engine = 'xelatex'
map <Leader>p :LLPStartPreview<CR>

" toggle panes
map <Leader>n :NERDTreeToggle<CR>
nmap <Leader>t :TagbarToggle<CR>

" powerline config
" Credit to Paul W. Frields (Fedora Magazine):
" https://fedoramagazine.org/add-power-terminal-powerline/
python3 from powerline.vim import setup as powerline_setup
python3 powerline_setup()
python3 del powerline_setup
set laststatus=2 " Always display the statusline in all windows
set showtabline=2 " Always display the tabline, even if there is only one tab
set noshowmode " Hide the default mode text (e.g. -- INSERT -- below the statusline)
set t_Co=256

" Luke Smith's configs
" https://lukesmith.xyz/
set wildmode=longest,list,full
set splitbelow splitright

" Shortcutting split navigation, saving a keypress:
map <C-h> <C-w>h
map <C-j> <C-w>j
map <C-k> <C-w>k
map <C-l> <C-w>l

" Calcurse markdown setting
autocmd BufRead,BufNewFile /tmp/calcurse*,~/.calcurse/notes/* set filetype=markdown

" Automatically delete all trailing whitespace on save.
autocmd BufWritePre * %s/\s\+$//e

" Miguel Grinberg's configs
" https://gist.github.com/miguelgrinberg/527bb5a400791f89b3c4da4bd61222e4
" indent/unindent with tab/shift-tab
nmap <Tab> >>
imap <S-Tab> <Esc><<i
nmap <S-tab> <<

" wrap toggle
setlocal nowrap
noremap <silent> <Leader>w :call ToggleWrap()<CR>
function ToggleWrap()
    if &wrap
        echo "Wrap OFF"
        setlocal nowrap
        set virtualedit=all
        silent! nunmap <buffer> <Up>
        silent! nunmap <buffer> <Down>
        silent! nunmap <buffer> <Home>
        silent! nunmap <buffer> <End>
        silent! iunmap <buffer> <Up>
        silent! iunmap <buffer> <Down>
        silent! iunmap <buffer> <Home>
        silent! iunmap <buffer> <End>
    else
        echo "Wrap ON"
        setlocal wrap linebreak nolist
        set virtualedit=
        setlocal display+=lastline
        noremap  <buffer> <silent> <Up>   gk
        noremap  <buffer> <silent> <Down> gj
        noremap  <buffer> <silent> <Home> g<Home>
        noremap  <buffer> <silent> <End>  g<End>
        inoremap <buffer> <silent> <Up>   <C-o>gk
        inoremap <buffer> <silent> <Down> <C-o>gj
        inoremap <buffer> <silent> <Home> <C-o>g<Home>
        inoremap <buffer> <silent> <End>  <C-o>g<End>
    endif
endfunction
