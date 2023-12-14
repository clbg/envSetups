if exists('g:loaded_charlie_plugin') | finish | endif " prevent loading file twice
let s:save_cpo = &cpo " save user coptions
set cpo&vim           " reset them to defaults
" command to run our plugin
command! CharlieRun lua require("hello").hello.sayHelloWorld()
command! CharlieGame lua require("hello").game.start_game()
let &cpo = s:save_cpo " and restore after
unlet s:save_cpo
let g:loaded_alpha = 1
