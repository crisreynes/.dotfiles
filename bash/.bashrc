# .bashrc
# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# Source .bash_aliases
if [ -f ~/.bash_aliases ]; then
	. ~/.bash_aliases
fi

# my settings
PS1='\[\e[38;5;229m\][\[\e[38;5;120m\]\u\[\e[38;5;222m\]@\[\e[38;5;159m\]\h \[\e[38;5;212m\]\W\[\e[38;5;229m\]] \[\e[38;5;183m\]> \[\e[0m\]'

# Set vi mode
set -o vi
# Binds
bind -m vi-command 'Control-l: clear-screen'
bind -m vi-insert 'Control-l: clear-screen'

neofetch
