```
filetype off
set rtp+=~/.vim/bundle/vundle
call vundle#rc()

if filereadable(expand("~/.vimrc.bundles"))
    source ~/.vimrc.bundles
endif

set number
set ruler
set showcmd
set ai
set cursorline
set ignorecase
set incsearch
set hls
set helplang=cn
set backspace=indent,eol,start
syntax on
color dracula


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"                 c,c++按F7编译运行
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"map <F7> :call CompileRunGcc()<CR>
map go :call CompileRunGcc()<CR>
func! CompileRunGcc()
    exec "w"
    if $filetype == "c"
        exec  "!gcc % -o %<"
        exec  "! ./%<"
        "exec "!make"
        "exec "! ./build"
    elseif &filetype == "cpp"
        exec "!g++ -std=c++11 % -o %< -I /Users/wangyf/Myinclude -L /Users/wangyf/Mylib -ljsoncpp -lcurl -lboost_system"
        exec "! ./%<"
        "exec "!make"
        "exec "! ./build"
    elseif &filetype == "java"
        exec "!javac %"
        exec "!java %<"
    elseif &filetype == "sh"
        :!bash ./%
    elseif &filetype == "py"
        exec "!python %"
    endif 
endfunc

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"                  NERDTree            
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"Close vim if the only window left opened
let NERDTreeIgnore=['\~$', '\.pyc$', '\.swp$']
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTreeType") && b:NERDTreeType == "primary") | q | endif
nmap <C-I> :NERDTreeToggle<cr>


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"                  YouCompleteMe                            *
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

let g:ycm_global_ycm_extra_conf = '~/.vim/bundle/YouCompleteMe/third_party/ycmd/cpp/ycm/.ycm_extra_conf.py'
set completeopt=longest,menu   "让vim的补全菜单行为与一般IDE一致
autocmd InsertLeave * if pumvisible() == 0|pclose|endif    "离开插入模式后自动关闭预览窗口
"回车即选中当前项
"inoremap <expr> <CR>        pumvisible() ? "\<C-y>" : "\<CR>"
"上下左右键的行为   会显示其他信息
inoremap <expr> <Down>      pumvisible() ? "\<C-n>" : "\<Down>"
inoremap <expr> <Up>        pumvisible() ? "\<C-p>" : "\<Up>"
inoremap <expr> <PageDown>  pumvisible() ? "\<PageDown>\<C-p>\<C-n>" : "\<PageDown>"
inoremap <expr> <PageUp>   pumvisible() ? "\<PageUp>\<C-p>\<C-n>" : "\<PageUp>"
"youcompleteme  默认tab  s-tab 和自动补全冲突
"let g:ycm_key_list_select_completion=['<c-n>']
"let g:ycm_key_list_select_completion = ['<Down>']
"let g:ycm_key_list_previous_completion=['<c-p>']
"let g:ycm_key_list_previous_completion = ['<Up>']
let g:ycm_confirm_extra_conf=0 "关闭加载.ycm_extra_conf.py提示

let g:ycm_collect_identifiers_from_tags_files=1    " 开启 YCM 基于标签引擎
let g:ycm_min_num_of_chars_for_completion=1    " 从第2个键入字符就开始罗列匹配项
let g:ycm_cache_omnifunc=0    " 禁止缓存匹配项,每次都重新生成匹配项
let g:ycm_seed_identifiers_with_syntax=1    " 语法关键字补全
nnoremap <F5> :YcmForceCompileAndDiagnostics<CR>    "force recomile with syntastic
"nnoremap <leader>lo :lopen<CR>    "open locationlist
"nnoremap <leader>lc :lclose<CR>    "close locationlist
inoremap <leader><leader> <C-x><C-o>
"在注释输入中也能补全
let g:ycm_complete_in_comments = 1
"在字符串输入中也能补全
let g:ycm_complete_in_strings = 1
"注释和字符串中的文字也会被收入补全
let g:ycm_collect_identifiers_from_comments_and_strings = 0
"跳转到定义处
nnoremap <leader>jd :YcmCompleter GoToDefinitionElseDeclaration<CR> 
let g:ycm_error_symbol = '✗'
let g:ycm_warning_symbol = '⚠'


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""    Yggdroot/indentLine    """""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let g:indentLine_char = '¦'
let g:indentLine_enabled = 1
let g:autopep8_disable_show_diff=1
set tabstop=2
set shiftwidth=2
set expandtab


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""    tmhedberg/SimpylFold  **********
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set foldmethod=indent 
set foldlevel=99
nnoremap <space> za 
let g:SimpylFold_docstring_preview=1


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""    scrooloose/nerdcommenter   **********
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let mapleader=","
filetype plugin on
"map <F6> <leader>ci<CR>
map <space> <leader>ci<CR>


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"           taglist.vim
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
map <C-O> :TagbarToggle<CR>
let Tlist_WinWidth=1
let Tlist_Exit_OnlyWindow=1


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"           ctrlp.vim
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
map <F5> :CtrlP<CR>


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"           powerline
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"set rtp+=/Users/wangyf/Library/Python/2.7/lib/python/site-packages/powerline/bindings/bash/powerline.sh
"set nocompatible 
"set t_Co=256
"let g:minBufExplForceSyntaxEnable=1
"python from powerline.vim import setup as powerline_setup
"python powerline_setup()
"python del powerline_setup 
"set laststatus=2
"set guifont=Source\ Code\ Pro\ for\ Powerline:h12
"set noshowmode


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"           minibuf
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"let g:miniBufExplMapWindowNavVim=1
"let g:miniBufExplMapWindowNavArrows=1
"let g:miniBufExplMapCTabSwitchBufs=1
"let g:miniBufExplModSelTarget=1
noremap <C-J> <C-W>j
noremap <C-K> <C-W>k
noremap <C-H> <C-W>h
noremap <C-L> <C-W>l


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"           airline
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"let g:airline_theme="luna"
let g:airline#extensions#tabline#enabled=1
let g:airline#extensions#tabline#buffer_nr_show=1
nnoremap <C-N> :bn<CR>
nnoremap <C-M> :bp<CR>
```
