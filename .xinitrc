source ~/.home/colorscheme/env
xset r rate 250 100
xrandr --output HDMI-1-0 --mode 1920x1080 --pos 1920x0
redshift -l 45:-70 &
sxhkd -c ~/.config/sxhkd/sxhkdrc &
exec qtile start
