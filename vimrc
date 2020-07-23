python3 from powerline.vim import setup as powerline_setup
python3 powerline_setup()
python3 del powerline_setup
set laststatus=2 " Always display the statusline in all windows
set showtabline=2 " Always display the tabline, even if there is only one tab
set noshowmode " Hide the default mode text (e.g. -- INSERT -- below the statusline)
set t_Co=256

:set relativenumber

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Remap ESC to ii. Credit to Derek Taylor (DistroTube):
" https://gitlab.com/dwt1/dotfiles/-/blob/master/.vimrc
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
:imap ii <Esc>

