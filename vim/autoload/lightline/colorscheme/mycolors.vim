let s:p = {'normal': {}}
let s:p.normal.left = [ [ $xCS_FOREGROUND, $xCS_STRUCTURE_c, $CS_FOREGROUND, $CS_STRUCTURE_c] ]
let s:p.normal.right = [ [ $xCS_FOREGROUND, $xCS_STRUCTURE_c, $CS_FOREGROUND, $CS_STRUCTURE_c] ]
let s:p.normal.middle = [ [ $xCS_FOREGROUND, $xCS_STRUCTURE_c, $CS_FOREGROUND, $CS_STRUCTURE_c] ]
let g:lightline#colorscheme#mycolors#palette = lightline#colorscheme#fill(s:p)
