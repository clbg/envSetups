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

# asdf - Unified runtime version manager
if [ -f /opt/homebrew/opt/asdf/libexec/asdf.sh ]; then
    # macOS Apple Silicon
    . /opt/homebrew/opt/asdf/libexec/asdf.sh
elif [ -f /usr/local/opt/asdf/libexec/asdf.sh ]; then
    # macOS Intel
    . /usr/local/opt/asdf/libexec/asdf.sh
elif [ -f ~/.asdf/asdf.sh ]; then
    # Linux (git clone)
    . ~/.asdf/asdf.sh
fi

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
