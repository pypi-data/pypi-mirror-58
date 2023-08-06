# briar_repl

python repl cli chat client to be used with briar-headless:

https://code.briarproject.org/briar/briar/tree/master/briar-headless

currently it features:
* contact listing
* contact adding
* direct chat with contacts
* briar link display
* command help

in two modes:
* command mode (blue bottom bar)
* chat mode    (green bottom bar)

commands in chat mode are called by prepending `/` so a `/back` brings you back to command mode

commands are autocompleted thanks to the amazing prompt_toolkit package

https://github.com/prompt-toolkit/python-prompt-toolkit
