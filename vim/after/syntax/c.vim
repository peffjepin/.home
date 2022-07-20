syn keyword CControl for while if else case switch default
syn keyword CFunctionExit return goto
syn match Special +\\+
syn match Special +\\n+
syn match CArrow "->"
syn region CDocstring start=+/\*+ end=+\*/+ 

syn match CFunctionDef +\(\w*\)\?\s*\w\+[ *]*\n\?\w\+\ze(\([^=;{}]*\n\)*\s*{+
syn match CPyDocstring +PyDoc_STRVAR(\w\+,\s*\n\?\s*"\_.\{-}");+ contains=Special
syn match CPyDocstring +PyDoc_STRVAR(\w\+,\s*\n\?\s*'\_.\{-}');+ contains=Special

hi! link CDocstring Documentation
hi! link CArrow Comment
hi! link CPyDocstring Documentation
hi! link CFunctionExit FunctionExit
hi! link CFunctionDef DefinitionName
hi! link CControl ControlFlow

syn sync minlines=150

