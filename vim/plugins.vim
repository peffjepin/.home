let g:enable_ycm=1

call plug#begin()
Plug 'itchyny/lightline.vim'
Plug 'tikhomirov/vim-glsl'
Plug 'vim-syntastic/syntastic'
Plug 'Chiel92/vim-autoformat'
Plug 'airblade/vim-gitgutter'
Plug 'airblade/vim-rooter'
Plug 'junegunn/fzf.vim'
if g:enable_ycm
    Plug 'ycm-core/YouCompleteMe'
endif
call plug#end()

" code formatting and linting
let g:syntastic_python_checkers = ['flake8']
let g:syntastic_c_checkers = ['gcc']
let g:formatters_python = ['black']
let g:autoformat_autoindent = 0
let g:autoformat_retab = 0
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 0
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 1 

" syntastic suggested default config
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

" visual aid for indentation
let g:indentLine_char = "."

if g:enable_ycm
    nnoremap <F5> :YcmCompleter RefactorRename 
    let g:ycm_autoclose_preview_window_after_completion=1
    let g:ycm_confirm_extra_conf = 0
endif

let g:lightline = {
    \ 'colorscheme': 'mycolors',
    \ 'active': {
    \   'left': [ [ 'readonly', 'absolutepath', 'modified', ] ],
    \   'right':[ [ 'lineinfo' ],
    \             [ 'percent'  ] ],
    \ }
    \ }

" when live resourcing vimrc the statusline breaks
" this disabling and renabling fixes that problem
call lightline#disable()  
call lightline#enable()

let g:rooter_patters = ['.git']
