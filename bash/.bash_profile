# .bash_profile

if [ -f ~/.bashrc ] ; then
	. ~/.bashrc
fi

if [ -d "$HOME/.cargo/bin" ] ; then
	PATH="$HOME/.cargo/bin:$PATH"
fi

if [ -d "$HOME/.local/bin" ] ; then
	PATH="$HOME/.local/bin:$PATH"
fi

if [ -d "$HOME/bin" ] ; then
	PATH="$HOME/bin:$PATH"
fi

if [ -d "/var/lib/snapd/snap/bin" ] ; then
	PATH="/var/lib/snapd/snap/bin:$PATH"
fi

if [ -d "$HOME/go/bin" ] ; then
	PATH="$HOME/go/bin:$PATH"
fi

export EXA_COLORS="\
uu=36:\
gu=37:\
sn=32:\
sb=32:\
da=34:\
ur=34:\
uw=35:\
ux=36:\
ue=36:\
gr=34:\
gw=35:\
gx=36:\
tr=34:\
tw=35:\
tx=36:"
export EDITOR="nvim"
