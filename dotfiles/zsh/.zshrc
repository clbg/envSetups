if [ -e /home/linuxbrew/.linuxbrew/bin/brew ]; then 
    eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)
elif [[ -e "/opt/homebrew/bin/brew" ]]; then 
    eval $(/opt/homebrew/bin/brew shellenv)
fi

# Custom environment variables
source ~/envSetups/linuxSetup/envvar/exports
export PATH=$HOME/.toolbox/bin:$PATH

   
alias j=z  # Keep 'j' command for muscle memory
    
# Load your custom aliases
source ~/envSetups/linuxSetup/envvar/aliases
    
# ========================================
# Runtime Version Managers
# ========================================

# direnv - per-directory environment variables
eval "$(direnv hook zsh)"

# mise - runtime version manager (Python, Node, Java, etc.)
# mise manages runtimes only; direnv handles env vars
eval "$(mise activate zsh)"

# ========================================
# Additional Tools
# ========================================

# fzf - Fuzzy finder
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

# ========================================
# Local Overrides (machine-specific config)
# ========================================
if [[ -f "$HOME/.zshrc_local" ]]; then
    source ~/.zshrc_local
fi

eval "$(zoxide init zsh)"

[[ "$TERM_PROGRAM" == "kiro" ]] && . "$(kiro --locate-shell-integration-path zsh)"

[[ "$TERM_PROGRAM" != "kiro" ]] && eval "$(starship init zsh)"

# iterm2 current directory update
iterm2_cwd_update() {
  printf "\e]7;file://%s%s\a" "$HOST" "$PWD"
}

# direnv-aware iTerm2 colors (set ITERM_TAB_COLOR / ITERM_BG_COLOR in .envrc)
_direnv_iterm_color() {
  if [[ -n "$ITERM_TAB_COLOR" ]]; then
    local r=${ITERM_TAB_COLOR%%;*} g=${${ITERM_TAB_COLOR#*;}%%;*} b=${ITERM_TAB_COLOR##*;}
    printf '\033]6;1;bg;red;brightness;%s\a\033]6;1;bg;green;brightness;%s\a\033]6;1;bg;blue;brightness;%s\a' "$r" "$g" "$b"
  else
    printf '\033]6;1;bg;*;default\a'
  fi
  if [[ -n "$ITERM_BG_COLOR" ]]; then
    printf '\033]1337;SetColors=bg=%s\007' "$ITERM_BG_COLOR"
  else
    printf '\033]1337;SetColors=bg=default\007'
  fi
}

autoload -Uz add-zsh-hook
add-zsh-hook precmd iterm2_cwd_update
add-zsh-hook precmd _direnv_iterm_color

# Added by AIM CLI
export PATH="$HOME/.aim/mcp-servers:$PATH"
