#!/usr/bin/env bash
#
# envSetups Bootstrap Script
# Supports: Ubuntu/Debian, macOS, Amazon Linux
# Usage: curl -sL chengpeng.space/i | bash
#

set -euo pipefail

#========================
# Colors
#========================
RED='\033[0;31m' GREEN='\033[0;32m' YELLOW='\033[1;33m' NC='\033[0m'
log()   { echo -e "${GREEN}[✓]${NC} $*"; }
warn()  { echo -e "${YELLOW}[!]${NC} $*"; }
fatal() { echo -e "${RED}[✗]${NC} $*" >&2; exit 1; }

#========================
# Detect system
#========================
detect_system() {
    local os_id="unknown"
    local os_version="0"
    
    if [ "$(uname -s)" = "Darwin" ]; then
        os_id="macos"
        os_version=$(sw_vers -productVersion 2>/dev/null | cut -d. -f1 || echo "0")
    elif [ -f /etc/os-release ]; then
        # shellcheck disable=SC1091
        source /etc/os-release
        os_id="${ID}"
        os_version="${VERSION_ID%%.*}"
    fi
    
    # Export for Python to use
    export ENV_SETUP_OS="${os_id}"
    export ENV_SETUP_VERSION="${os_version}"
    
    log "System: ${os_id} ${os_version}"
}

#========================
# Install dependencies
#========================
install_deps() {
    local os_id="${ENV_SETUP_OS}"
    
    log "Installing dependencies..."
    
    case "${os_id}" in
        ubuntu|debian)
            sudo apt-get update -qq || fatal "apt update failed"
            sudo apt-get install -y git python3 zsh curl || fatal "apt install failed"
            ;;
        amzn)
            sudo yum install -y git python3 zsh curl || fatal "yum install failed"
            ;;
        macos)
            # Check Homebrew
            if ! command -v brew &>/dev/null; then
                log "Installing Homebrew..."
                /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" || fatal "Homebrew install failed"
                
                # Configure Homebrew PATH
                if [ -f /opt/homebrew/bin/brew ]; then
                    eval "$(/opt/homebrew/bin/brew shellenv)"
                elif [ -f /usr/local/bin/brew ]; then
                    eval "$(/usr/local/bin/brew shellenv)"
                fi
            fi
            brew install git python3 zsh || fatal "brew install failed"
            ;;
        *)
            fatal "Unsupported system: ${os_id}"
            ;;
    esac
}

#========================
# Manage repository
#========================
manage_repo() {
    local repo_dir="${HOME}/envSetups"
    local repo_url="${REPO_URL:-https://github.com/clbg/envSetups.git}"
    
    if [ -d "${repo_dir}/.git" ]; then
        # Check for local changes
        if ! git -C "${repo_dir}" diff-index --quiet HEAD -- 2>/dev/null; then
            warn "Local changes detected in ${repo_dir}"
            warn "Using local version (skipping remote update)"
            warn "To sync with remote later, run:"
            warn "  cd ${repo_dir} && git status"
            log "Continuing with local version..."
        else
            log "Checking for updates..."
            # Fetch to check if remote has changes
            git -C "${repo_dir}" fetch origin 2>/dev/null || true

            # Check if we're behind remote
            local local_commit=$(git -C "${repo_dir}" rev-parse HEAD)
            local remote_commit=$(git -C "${repo_dir}" rev-parse origin/master 2>/dev/null || echo "")

            if [ -n "${remote_commit}" ] && [ "${local_commit}" != "${remote_commit}" ]; then
                log "Remote has updates, pulling..."
                if git -C "${repo_dir}" pull; then
                    log "Repository updated successfully ✓"
                else
                    warn "Pull failed, continuing with current version"
                fi
            else
                log "Already up to date ✓"
            fi
        fi
    else
        log "Cloning repository..."
        git clone "${repo_url}" "${repo_dir}" || fatal "Clone failed"
    fi
    
    cd "${repo_dir}" || fatal "Cannot cd to ${repo_dir}"
    
    # Configure git
    git config user.name 'charlie' 2>/dev/null || true
    git config user.email 'spam@chengpeng.space' 2>/dev/null || true
}

#========================
# Run Python installer
#========================
run_installer() {
    log "Running Python installer..."
    cd "${HOME}/envSetups" || fatal "envSetups not found"
    python3 -m py-installer.install || fatal "Python installer failed"
}

#========================
# Main
#========================
main() {
    log "=========================================="
    log "  envSetups Installer"
    log "=========================================="
    
    detect_system
    install_deps
    manage_repo
    run_installer
    
    log "=========================================="
    log "  ✅ Installation completed!"
    log "=========================================="
    log ""
    log "Next: Restart terminal or run: source ~/.zshrc"
}

main "$@"
