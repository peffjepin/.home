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

export BG_L="#3c3836"
export BG_M="#282828"
export BG_D="#1d2021"
export FG_L="#fbf1c7"
export FG_M="#ebdbb2"
export FG_D="#d5c4a1"
export RED_L="#fb4934"
export RED_D="#cc241d"
export GREEN_L="#b8bb26"
export GREEN_D="#98971a"
export YELLOW_L="#fabd2f"
export YELLOW_D="#d79921"
export BLUE_L="#83a598"
export BLUE_D="#458588"
export PURPLE_L="#d3869b"
export PURPLE_D="#b16286"
export ORANGE_L="#fe8019"
export ORANGE_D="#d65d0e"

# Source other files
source $ZDOTDIR/paths
source $ZDOTDIR/plugins
source $ZDOTDIR/functions
source $ZDOTDIR/aliases
