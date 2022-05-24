if exists("b:current_syntax")
    finish
endif

syn keyword PyControl for while if elif else try except finally continue break
syn keyword PyFunctionExit return yield raise assert
syn keyword PyInclude import from 

syn match PyString +".\{-}"+
syn match PyString +'.\{-}'+
syn match PyComment '#.*$'
syn region PyDocstring start=+"""+ end=+"""+ 
syn region PyDocstring start=+'''+ end=+'''+ 

syn match PyDecorator "@\(\w\|\.\)\+"


" function / class definitions
syn keyword PyDefKw def class contained
syn match PyDefName '^\s*\(def\|class\) \w*' contained contains=PyDefKw
syn match PyDefinitionFull '^\s*\(def\|class\) \w\+' contains=PyDefName
syn match PyDefinitionFull '^\s*\(def\|class\) \w\+' contains=PyDefName


hi! link PyComment Comment
hi! link PyDecorator String
hi! link PyInclude Include
hi! link PyDefName DefinitionName
hi! link PyDefKw DefinitionClass
hi! link PyDocstring Documentation
hi! link PyFunctionExit FunctionExit
hi! link PyControl ControlFlow
hi! link PyString String
hi! link PyKeyword KeyWord

syn sync minlines=250

let b:current_syntax = "mycolors"
