#---------------------------------------------------------------------------#
#  _______      ____       .-'''-. .---.  .---. .-------.        _______    #
# \  ____  \  .'  __ `.   / _     \|   |  |_ _| |  _ _   \      /   __  \   #
# | |    \ | /   '  \  \ (`' )/`--'|   |  ( ' ) | ( ' )  |     | ,_/  \__)  #
# | |____/ / |___|  /  |(_ o _).   |   '-(_{;}_)|(_ o _) /   ,-./  )        #
# |   _ _ '.    _.-`   | (_,_). '. |      (_,_) | (_,_).' __ \  '_ '`)      #
# |  ( ' )  \.'   _    |.---.  \  :| _ _--.   | |  |\ \  |  | > (_)  )  __  #
# | (_{;}_) ||  _( )_  |\    `-'  ||( ' ) |   | |  | \ `'   /(  .  .-'_/  ) #
# |  (_,_)  /\ (_ o _) / \       / (_{;}_)|   | |  |  \    /  `-'`-'     /  #
# /_______.'  '.(_,_).'   `-...-'  '(_,_) '---' ''-'   `'-'     `._____.'   #
#                                                                           #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
#                                                                           #
# ~/.bashrc: executed by bash(1) for non-login shells.                      #
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)  #
# for examples                                                              #
#                                                                           #
# .bashrcとは(ログインした後に画面上から）bashを起動したときに読み込まれる  #
# 設定ファイルです。(https://wa3.i-3-i.info/word13649.html)                 #
#                                                                           #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# - - - EXPORTS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
set -o vi
export EDITOR=vim
export GEM_HOME="$HOME/gems"
export LC_CTYPE="en_US.UTF-8"
export PATH=/usr/local/bin:$PATH
export PATH="$HOME/gems/bin:$PATH"
source $(which virtualenvwrapper.sh)
export WORKON_HOME="$HOME/.virtualenvs"
export VIRTUALENVWRAPPER_PYTHON=$(which python3)
export VIRTUALENVWRAPPER_VIRTUALENV=$(which virtualenv)

# - - - HISTORY - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
HISTSIZE=1000
HISTFILESIZE=2000
HISTCONTROL=ignoreboth

# - - - SHOPT - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
shopt -s expand_aliases # expand aliases
shopt -s autocd # change to named directory
shopt -s cdspell # autocorrect cd misspellings
shopt -s checkwinsize # check window size after each command
shopt -s histappend # append to the history file, don't overwrite it
shopt -s cmdhist # save multi-line commands in history as a single line

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

# - - - CONDA - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/jayascript/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/jayascript/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/home/jayascript/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/jayascript/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

# - - - THEME - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

# Show git branch in terminal
git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[01;31m\]$(git_branch)\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w$(git_branch)\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# colored GCC warnings and errors
#export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

# Enable powerline
if [ -f `which powerline-daemon` ]; then
  powerline-daemon -q
  POWERLINE_BASH_CONTINUATION=1
  POWERLINE_BASH_SELECT=1
  . /usr/share/powerline/bindings/bash/powerline.sh
fi

# - - - ALIASES - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Alias definitions.
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# root privileges
alias doas="doas --"

# system
alias update="sudo apt update && sudo apt upgrade"

# navigation
alias ..='cd ..'
alias ...='cd ../..'
alias .3='cd ../../..'
alias .4='cd ../../../..'
alias .5='cd ../../../../..'

# changing ls to exa
alias ls='exa -al --grid --group-directories-first' # preferred listing
alias la='exa -a  --grid --group-directories-first'  # all files and dirs
alias ll='exa -l  --grid --group-directories-first'  # long format
alias lr='exa -laR --grid --group-directories-first' # recursive
alias l.='exa -a | egrep "^\."' # dotfiles only

# confirm before overwriting something
alias cp="cp -i"
alias mv="mv -i"
alias rm="rm -i"

# flags
alias df="df -h"
alias free="free -m"

# git
alias addnew='git add -u'
alias addup='git add .'
alias branch='git branch'
alias checkout='git checkout'
alias clone='git clone'
alias cm='git commit -m'
alias fetch='git fetch'
alias pull='git pull'
alias push='git push'
alias st='git status'
alias tag='git tag'
alias newtag='git tag -a'

# youtube-dl
alias yta-aac="youtube-dl --extract-audio --audio-format aac "
alias yta-best="youtube-dl --extract-audio --audio-format best "
alias yta-flac="youtube-dl --extract-audio --audio-format flac "
alias yta-m4a="youtube-dl --extract-audio --audio-format m4a "
alias yta-mp3="youtube-dl --extract-audio --audio-format mp3 "
alias yta-opus="youtube-dl --extract-audio --audio-format opus "
alias yta-vorbis="youtube-dl --extract-audio --audio-format vorbis "
alias yta-wav="youtube-dl --extract-audio --audio-format wav "
alias ytv-best="youtube-dl -f bestvideo+bestaudio "

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# - - - FUNCTIONS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Make and enter directory
mcdir ()
{
    mkdir -p -- "$1" &&
    cd -P -- "$1"
}
export mcdir

# Archive extraction
ex ()
{
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;;
      *.tar.gz)    tar xzf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar x $1   ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x $1      ;;
      *.deb)       ar x $1      ;;
      *.tar.xz)    tar xf $1    ;;
      *.tar.zst)   unzstd $1    ;;
      *)           echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}

# - - - MISC. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Add SSH and GPG keys to keychain
eval `keychain --eval --agents ssh,gpg id_rsa`

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"
