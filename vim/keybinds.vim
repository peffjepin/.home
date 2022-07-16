let mapleader = " "

nnoremap <Leader>i <C-]>
nnoremap <Leader>o <C-o>
nnoremap <Leader>w :w<CR>
nnoremap <Leader>q :q<CR>
nnoremap <Leader>wq :wq<CR>
nnoremap <Leader>WQ :wq!<CR>
nnoremap <Leader>Q :q!<CR>
nnoremap <Leader>vc :sp $MYVIMRC<CR>
nnoremap <Leader>so :source $MYVIMRC<CR>
nnoremap <Leader>f :Autoformat<CR>
nnoremap <F9> :lfirst<CR>
nnoremap <F10> :lnext<CR>
nnoremap <F12> :setlocal spell! spelllang=en_us<CR>
nnoremap r :redo<CR>

nnoremap <Leader>h <C-w><h>
nnoremap <Leader>l <C-w><l>
nnoremap <Leader>j <C-w><j>
nnoremap <Leader>k <C-w><k>

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
nnoremap <C-s> :%s//g<Left><Left>

" fuzzy finding
nnoremap <S-Tab> :Files<CR>
nnoremap <Leader>/ :Rg<CR>

" copy to xclip default system keyboard
vnoremap <S-Y> :w !xclip -selection c<CR><CR>gvy
vnoremap <S-D> :!xclip -selection c<CR><CR>
nnoremap <S-Y><S-Y> yy:call system('xclip -selection c', @0)<CR>
nnoremap <S-D><S-D> yy:call system('xclip -selection c', @0)<CR>dd

nnoremap { {{
nnoremap } }}
nnoremap n nzz
nnoremap N Nzz

inoremap <C-p> @property<CR>def (self):<Esc>Bi
inoremap <C-f> @pytest.fixture<CR>def ():<Esc>Bi
inoremap <C-t> def test_<CR><Tab>raise NotImplementedError()<Esc>kA():<Esc>2hi
nnoremap test idef test_<CR><Tab>raise NotImplementedError()<Esc>kA():<Esc>2hi

nnoremap <Leader><Leader>pt i@pytest.mark.parametrize("param1", (val1,))<CR>def test_(param1):<CR>    raise NotImplementedError()<Esc>kF_a
