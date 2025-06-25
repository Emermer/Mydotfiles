# powerlevel10k
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
 source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

source ~/.config/powerlevel10k/powerlevel10k.zsh-theme

[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

# exports
export XDG_DATA_HOME=${XDG_DATA_HOME:="$HOME/.local/share"}
export XDG_CONFIG_HOME=${XDG_CONFIG_HOME:="$HOME/.config"}
export XDG_STATE_HOME=${XDG_STATE_HOME:="$HOME/.local/state"}
export XDG_CACHE_HOME=${XDG_CACHE_HOME:="$HOME/.cache"}
export LESSHISTFILE=$XDG_CACHE_HOME/less/.lesshst
export GTK2_RC_FILES=$XDG_CONFIG_HOME/gtk-2.0/gtkrc
export CUDA_CACHE_PATH=$XDG_CACHE_HOME/nv
export GNUPGHOME=$XDG_DATA_HOME/gnupg
export TERM=alacritty


[ -d "$HOME/.local/bin" ] && PATH="$HOME/.local/bin:$PATH"
export PATH

# zsh history
export HISTFILESIZE=1000000000
export HISTSIZE=1000000000
export HISTFILE=$XDG_STATE_HOME/zsh/zsh_history
setopt INC_APPEND_HISTORY
export HISTTIMEFORMAT="[%F %T] "
setopt EXTENDED_HISTORY
setopt HIST_FIND_NO_DUPS
SAVEHIST=$HISTSIZE

# pfetch config
export PF_INFO="ascii title os de uptime pkgs"
export PF_COL1="6"
export PF_COL2="7"
export PF_COL3="7"

# zsh aliases
alias upsys="echo 'updating system packages and AUR packages' && paru && echo 'updating flatpaks' && flatpak update && echo 'uninstalling unneeded flatpak dependencies' && flatpak uninstall --unused && echo 'updating firefox profile to latest arkenfox version' && ~/.mozilla/firefox/atxl096a.arkenfox/updater.sh"
alias xdgninja="cd && cd .config/xdg-ninja/ && ./xdg-ninja.sh && echo Executing this alias has moved you to the '~/.config/xdg-ninja/' directory"
alias wget="wget --hsts-file="$XDG_DATA_HOME/wget-hsts""
alias emacsc="emacsclient -c"
alias yt-dlp-mp4='yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"'
alias yt-dlp-mp3="yt-dlp -x --audio-format mp3"
alias upff="cd ~/.mozilla/firefox/atxl096a.arkenfox/ && ./updater.sh && cd"
alias doom="~/.config/emacs/bin/doom"
alias zshr="exec zsh || source ~/.zshrc"
alias zip="zip -r "$1".zip "$1"/"

# mozilla applications wayland native support
export MOZ_ENABLE_WAYLAND=1

# Variable for unzipping main file types
extract() {
    if [[ -f $1 ]]; then  # Check if the file exists
        case "$1" in
            *.zip)    unzip "$1" ;;      # For .zip files
            *.tar.gz) tar -xvzf "$1" ;;  # For .tar.gz files
            *.7z)     7za x "$1" ;;       # For .7z files
	    *.rar)    unrar x "$1" ;;    # For .rar files
            *)        echo "Unsupported file type: $1" ;;  # For unsupported types
        esac
    else
        echo "File not found: $1"  # If the file doesn't exist
    fi
}

# startup commands
sleep 0.1 && clear
