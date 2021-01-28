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
Plug 'lervag/vimtex'
Plug 'chrisbra/csv.vim'
Plug 'SirVer/ultisnips'
Plug 'junegunn/goyo.vim'
Plug 'majutsushi/tagbar'
Plug 'preservim/nerdtree'
Plug 'tpope/vim-fugitive'
Plug 'honza/vim-snippets'
Plug 'junegunn/limelight.vim'
Plug 'vim-airline/vim-airline'
Plug 'jmcantrell/vim-virtualenv'
Plug 'norcalli/nvim-colorizer.lua'
Plug 'hynek/vim-python-pep8-indent'
Plug 'vim-airline/vim-airline-themes'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'numirias/semshi', {'do': ':UpdateRemotePlugins'}

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
let g:tex_flavor='latex'
autocmd BufRead,BufNewFile /tmp/calcurse*,~/.calcurse/notes/* set filetype=markdown
autocmd BufWritePre * %s/\s\+$//e " Automatically delete all trailing whitespace on save.
autocmd BufRead,BufNewFile *.md set spell spelllang=en_us
autocmd BufRead,BufNewFile *.tex set spell spelllang=en_us

" LaTeX and vimtex settings
let g:vimtex_compiler_latexmk = {
    \ 'options' : [
    \   '-pdf',
    \   '-shell-escape',
    \   '-verbose',
    \   '-file-line-error',
    \   '-synctex=1',
    \   '-interaction=nonstopmode',
    \ ],
    \}

" Miguel Grinberg's configs
" https://gist.github.com/miguelgrinberg/527bb5a400791f89b3c4da4bd61222e4
" indent/unindent with tab/shift-tab
nmap <Tab> >>
imap <S-Tab> <Esc><<i
nmap <S-Tab> <<

" coc.nvim settings
let g:coc_node_path = '/usr/bin/node'

" use <tab> for trigger completion and navigate to the next complete item
function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~ '\s'
endfunction

inoremap <silent><expr> <Tab>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<Tab>" :
      \ coc#refresh()

" Casey Houser's config
" https://www.maketecheasier.com/turn-vim-word-processor/
func! WordProcessor()
    " movement changes
    map j gj
    map k gk
    " formatting text
    setlocal formatoptions=1
    setlocal noexpandtab
    setlocal wrap
    setlocal linebreak
    " spelling and thesaurus
    setlocal spelllang=en_us
    set thesaurus+=/home/jayascript/.config/nvim/thesaurus/mthesaur.txt
endfu
com! WP call WordProcessor()

" Goyo and Limelight config
func! s:goyo_enter()
    set noshowmode
    set noshowcmd
    set scrolloff=999
    Limelight
    let b:quitting=0
    let b:quitting_bang=0
    autocmd QuitPre <buffer> let b:quitting=1
    cabbrev <buffer> q! let b:quitting_bang=1 <bar> q!
    call WordProcessor()
endfunction

func! s:goyo_leave()
    set showmode
    set showcmd
    set scrolloff=5
    Limelight!
    " Quit Vim if this is the only remaining buffer
    if b:quitting && len(filter(range(1, bufnr('$')), 'buflisted(v:val)'))==1
        if b:quitting_bang
            qa!
        else
            qa
        endif
    endif
endfunction

autocmd! User GoyoEnter call <SID>goyo_enter()
autocmd! User GoyoLeave call <SID>goyo_leave()
