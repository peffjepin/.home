let mapleader = " "

if exists("g:enable_pydocs")
    nnoremap <Leader><Leader> :AsyncRun curl -X POST "localhost:5000/docs/pyc/?doc=<cword>"<CR>
endif

nnoremap <Leader>i <C-]>
nnoremap <Leader>o <C-o>
nnoremap <Leader>w :w<CR>
nnoremap <Leader>q :q<CR>
nnoremap <Leader>wq :wq<CR>
nnoremap <Leader>Q :q!<CR>
nnoremap <Leader>vc :sp $MYVIMRC<CR>
nnoremap <Leader>so :source $MYVIMRC<CR>
nnoremap <Leader>f :Autoformat<CR>
nnoremap <F9> :lfirst<CR>
nnoremap <F10> :lnext<CR>
nnoremap <F12> :setlocal spell! spelllang=en_us<CR>

nnoremap <Leader>h <C-w><h>
nnoremap <Leader>l <C-w><l>
nnoremap <Leader>j <C-w><j>
nnoremap <Leader>k <C-w><k>

" run script
nnoremap <Leader><CR> :!python3 %<CR>

" from the cursor, delete the remainder of the line and paste it 
" at the start of the next line
nnoremap <Leader>br i<CR><Esc>ji<Backspace><Esc>^

" copy to and from system keyboard (ctrl+c, ctrl+v) outside of vim
" note: this wont work with vim-minimal
nnoremap <Leader>y "+y
nnoremap <Leader>p "+p

" escape normal mode with jj/kk
inoremap jj <Esc>
inoremap kk <Esc>

" separate shell command options to new lines
nnoremap <C-Down> ^/<Space>-<CR>f-i\<CR><Esc>
nnoremap <C-Up> I<Backspace><Backspace><Backspace><Backspace><Space><Esc>
" reload the current buffer
nnoremap <C-r> :edit %<CR>
inoremap <C-p> @property<CR>def (self):<Esc>Bi
inoremap <C-f> @pytest.fixture<CR>def ():<Esc>Bi
nnoremap <C-s> :%s//g<Left><Left>

nnoremap <C-m> gg/import<CR>
