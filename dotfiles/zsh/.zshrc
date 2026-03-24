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
    
# Enhanced git aliases (oh-my-zsh git plugin style)
[ -f ~/.zsh_custom/git_aliases.zsh ] && source ~/.zsh_custom/git_aliases.zsh

# ========================================
# Runtime Version Managers
# ========================================

# direnv - per-directory environment variables
eval "$(direnv hook zsh)"

# mise - runtime version manager (Python, Node, etc.)
# mise manages runtimes only; direnv handles env vars
eval "$(mise activate zsh)"

# ========================================
# Additional Tools
# ========================================

# fzf - Fuzzy finder
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

# SDKMAN - Java version manager (must be at end)
export SDKMAN_DIR="$HOME/.sdkman"
[[ -s "$HOME/.sdkman/bin/sdkman-init.sh" ]] && source "$HOME/.sdkman/bin/sdkman-init.sh"

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

autoload -Uz add-zsh-hook
add-zsh-hook precmd iterm2_cwd_update
