# .bash_aliases

alias ls="eza -a --icons --group-directories-first --color=always"
alias ll="eza -la --icons --group-directories-first --color=always"
alias cp="cp -iv"
alias mv="mv -iv"
alias rm="rm -vI"
alias cat="bat"
alias cal="cal --sunday"
alias za="zathura --fork"
alias v="nvim"
alias sv="sudo nvim"
alias lf="lfcd"
alias nb="newsboat"
alias g="git"
alias ga="git add"
alias gb="git branch"
alias gc="git clone"
alias gd="git diff"
alias gs="git status"
alias gss="git status -s"
alias gp="git push"
alias gl="git pull"
alias gm="git merge"
alias gr="git remote"
alias gra="git remote add"
alias scrcpy="scrcpy  --shortcut-mod=lalt --video-codec=h265 -m1920 --max-fps=60 --screen-off-timeout=300 -S -t"

alias icat="kitten icat"
db64() {
	echo "$1" | base64 -d; echo
}
