HISTFILE=$ZDOTDIR/history
HISTSIZE=10000
SAVEHIST=10000
bindkey -v
autoload -Uz compinit
compinit
# End of lines added by install setup

# Setup environment variables
export KTCFG=$HOME/.config/kitty/kitty.conf
export QTCFG=$HOME/.config/qtile/config.py
export QTLOG=$HOME/.local/share/qtile/qtile.log
export BACKGROUND=$HOME/.config/background
export VENV_HOME=$HOME/virtual_environments

# Source other files
source $ZDOTDIR/colorscheme
source $ZDOTDIR/paths
source $ZDOTDIR/plugins
source $ZDOTDIR/functions
source $ZDOTDIR/aliases
