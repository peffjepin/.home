if exists(s:initialized)
    finish
endif

func PhoneIn(timer)
    let word_under_cursor = expand("<cword>")
    strcmd = "!curl -X POST localhost:5000/docs/pyc/?doc=".word_under_cursor
    silent exec strcmd
endfunc

let timer = timer_start(500, 'PhoneIn', {'repeat': -1})

let s:initialized = 1
