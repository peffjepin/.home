if exists(syntax_on)
    syntax reset
endif

let g:colors_name='mycolors'

function! s:HL(group, fg, ...)
    " Optionally specify background
    if a:0 >= 1
        let bg = a:1
    else
        let bg = $CS_BACKGROUND
    endif

    if a:0 >= 2
        let sp = a:2
    else
        let sp = "NONE"
    endif

    let strcmd = "hi ".a:group." ctermbg=".bg." ctermfg=".a:fg." cterm=".sp
    execute strcmd
endfunction

call s:HL("ColorColumn",    $CS_FOREGROUND, $CS_FOREGROUND_cc)
call s:HL("SignColumn",     $CS_FOREGROUND)
call s:HL("LineNr",         $CS_STRUCTURE_c)
call s:HL("MatchParen",     $CS_IMPORTANT_CC)
call s:HL("Visual",         $CS_BACKGROUND, $CS_FOREGROUND)

call s:HL("Statement",      $CS_FOREGROUND)
call s:HL("Keyword",        $CS_INTERACTIVE_c)
call s:HL("Operator",       $CS_INTERACTIVE_c)
call s:HL("Exception",      $CS_IMPORTANT_c)
call s:HL("Repeat",         $CS_EMPHASIS_c)
call s:HL("Conditional",    $CS_EMPHASIS_c)
call s:HL("Label",          $CS_IMPORTANT_c)
call s:HL("Function",       $CS_STRUCTURE)
" PreProc: Include Define Macro PreCondit
call s:HL("PreProc",        $CS_INTERACTIVE_c)
" Constant: Character Bolean Number Float String
call s:HL("Constant",       $CS_FOREGROUND_c)
call s:HL("String",         $CS_FOREGROUND_c)
call s:HL("Comment",        $CS_FOREGROUND_cc)
" Type: StorageClass Structure Typedef
call s:HL("Type",           $CS_INTERACTIVE_c)

call s:HL("Special",        $CS_EMPHASIS_c)

call s:HL("FunctionExit",   $CS_IMPORTANT)
call s:HL("ControlFlow",    $CS_EMPHASIS)
call s:HL("DefinitionClass",$CS_STRUCTURE)
call s:HL("DefinitionName", $CS_STRUCTURE_C)
call s:HL("Documentation",  $CS_STRUCTURE_cc)


" git gutter plugin
call s:HL("GitGutterAdd",   $CS_INTERACTIVE)

" syntastic plugin
call s:HL("SyntasticError",         $CS_IMPORTANT_CC, $CS_BACKGROUND, "undercurl")
call s:HL("SyntasticErrorSign",     $CS_IMPORTANT_CC)
call s:HL("SyntasticWarning",       $CS_EMPHASIS_CC, $CS_BACKGROUND, "undercurl")
call s:HL("SyntasticWarningSign",   $CS_EMPHASIS_CC)
