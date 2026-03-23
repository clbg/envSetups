# Machine Setup Prompt

> This document describes how to set up a fresh machine.
> An AI agent with terminal access can execute this directly.
> It replaces the `py-installer` Python scripts.
>
> **Execution order matters** — follow the numbered sections sequentially.

## 0. Prerequisites

The bootstrap script `py-installer/install.sh` handles cloning this repo and installing git/python3/zsh/curl.
After that, this document takes over.

Assume:
- This repo is cloned at `~/envSetups`
- `git`, `zsh`, `curl` are available
- The user's OS is either **macOS** or **Linux** (Ubuntu/Debian/Amazon Linux)

Detect the OS first and adapt all commands accordingly.

---

## 1. Package Manager

### macOS
- Install Homebrew if not present: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
- After install, ensure brew is on PATH (eval shellenv for `/opt/homebrew/bin/brew` or `/usr/local/bin/brew`)
- `brew update`

### Linux (Ubuntu/Debian)
- `sudo apt update`
- Use `apt` as primary package manager
- Also install Homebrew (Linuxbrew) for cross-platform packages

### Linux (Amazon Linux)
- `sudo yum -y update`
- Also install Homebrew (Linuxbrew)

### CN Mirror (if env var `CN=Y`)
- Set Homebrew mirror to Tsinghua:
  - `HOMEBREW_BREW_GIT_REMOTE=https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git`
  - `HOMEBREW_CORE_GIT_REMOTE=https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git`
  - `HOMEBREW_BOTTLE_DOMAIN=https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles`

---

## 2. Install Packages

### Common packages (all platforms, via brew)
```
htop fortune fzf tmux vim git curl wget rsync autojump the_silver_searcher icdiff tldr bat direnv starship zoxide ripgrep tree ncdu stow mise
```

> `stow` is included for future dotfile management migration (see TODO at bottom).

### macOS GUI apps (via `brew install --cask`)
```
iterm2 karabiner-elements kindle telegram wechat deepl raycast
```

---

## 3. Shell — Zsh + Oh My Zsh

1. If zsh is not the default shell, run `chsh -s /bin/zsh` (may require re-login)
2. Install Oh My Zsh:
   ```
   rm -rf ~/ohmyzsh
   git -C ~ clone https://github.com/ohmyzsh/ohmyzsh.git
   zsh ~/ohmyzsh/tools/install.sh
   ```
   (ignore non-zero exit, it's expected)
3. Symlink zshrc:
   ```
   ln -sf ~/envSetups/linuxSetup/linkFiles/HOME-.zshrc ~/.zshrc
   ```
4. Symlink bin scripts:
   ```
   ln -sf ~/envSetups/linuxSetup/bin ~/bin_local
   ```

---

## 4. Runtime Version Manager — mise

Use [mise](https://mise.jdx.dev/) to manage Python and Node.js runtimes.
direnv continues to handle per-directory environment variables — they don't overlap.

### Install mise
- **macOS**: `brew install mise`
- **Linux**: `curl https://mise.jdx.dev/install.sh | sh`
  - This installs a single Rust binary to `~/.local/bin/mise`
  - Or via Linuxbrew: `brew install mise`

### Shell integration
The `.zshrc` already has:
```
eval "$(mise activate zsh)"
```
This is faster than shim-based approaches (asdf) — mise modifies PATH directly.

### Install runtimes
```
mise use --global python@3.12
mise use --global node@22
```

> mise downloads prebuilt binaries — no compilation needed.
> Python installs in seconds, not 15+ minutes.

### Per-project versions
Create a `.mise.toml` in any project directory:
```toml
[tools]
python = "3.11"
node = "20"
```
mise auto-switches when you `cd` into the directory.

### Relationship with direnv
- **mise** = which Python/Node/etc binary to use (runtime versions)
- **direnv** = which env vars to set per directory (`.envrc` files)
- They work together without conflict. Both are loaded in `.zshrc`.

---

## 5. SSH

1. Create `.ssh` directory:
   ```
   mkdir -p ~/.ssh
   ```
2. Symlink SSH config:
   ```
   ln -sf ~/envSetups/linuxSetup/linkFiles/HOME-.ssh-config ~/.ssh/config
   ```
3. Create local override file (for machine-specific hosts):
   ```
   touch ~/.ssh/config_local
   ```
4. Append public key to authorized_keys (if not already present):
   ```
   grep -qiFf ~/envSetups/linuxSetup/linkFiles/key.pub ~/.ssh/authorized_keys 2>/dev/null || \
     cat ~/envSetups/linuxSetup/linkFiles/key.pub >> ~/.ssh/authorized_keys
   ```

---

## 6. Neovim

1. Install: `brew install neovim`
2. Create vim undo directory:
   ```
   mkdir -p ~/.vim/undodir
   ```
3. Symlink configs:
   ```
   ln -sf ~/envSetups/linuxSetup/linkFiles/HOME-.vimrc ~/.vimrc
   ln -sf ~/envSetups/linuxSetup/linkFiles/nvim ~/.config/nvim
   ```

> The nvim config uses LazyVim. Plugins will auto-install on first launch (`nvim`).
> No need to run PackerSync or any manual plugin install step.

---

## 7. Starship Prompt

1. Already installed via brew in step 2.
2. Symlink config:
   ```
   mkdir -p ~/.config
   ln -sf ~/envSetups/linuxSetup/linkFiles/HOME-.config-starship.toml ~/.config/starship.toml
   ```

> The `.zshrc` conditionally loads starship (skips in Kiro terminal).

---

## 8. fzf Shell Integration

After brew install (step 2), run the fzf installer for key bindings and completion:
```
$(brew --prefix)/opt/fzf/install --all
```

---

## 9. Git Config

Configure git identity (run inside `~/envSetups`):
```
git config user.email "i@chengpeng.space"
git config user.name "Cheng Peng"
```

---

## 10. macOS-Specific

Only run these on macOS:

### Karabiner-Elements
```
ln -sf ~/envSetups/macosSetup/linkFiles/HOME-.config-karabiner ~/.config/karabiner
```

---

## 11. Linux-Specific

Only run these on Linux with a desktop environment:

### i3 Window Manager
```
mkdir -p ~/.i3
ln -sf ~/envSetups/linuxSetup/linkFiles/HOME-.i3-config ~/.i3/config
```

### pip CN Mirror (if env var `CN=Y`)
```
mkdir -p ~/.config/pip
ln -sf ~/envSetups/linuxSetup/linkFiles/HOME-.config-pip-pip.conf ~/.config/pip/pip.conf
```

---

## 12. Cleanup

```
brew cleanup --prune=all
```

---

## Symlink Summary

| Source (in repo) | Target (on machine) | Condition |
|---|---|---|
| `linuxSetup/linkFiles/HOME-.zshrc` | `~/.zshrc` | all |
| `linuxSetup/linkFiles/HOME-.vimrc` | `~/.vimrc` | all |
| `linuxSetup/linkFiles/nvim/` | `~/.config/nvim` | all |
| `linuxSetup/linkFiles/HOME-.ssh-config` | `~/.ssh/config` | all |
| `linuxSetup/linkFiles/HOME-.config-starship.toml` | `~/.config/starship.toml` | all |
| `linuxSetup/bin/` | `~/bin_local` | all |
| `macosSetup/linkFiles/HOME-.config-karabiner/` | `~/.config/karabiner` | macOS |
| `linuxSetup/linkFiles/HOME-.i3-config` | `~/.i3/config` | Linux desktop |
| `linuxSetup/linkFiles/HOME-.config-pip-pip.conf` | `~/.config/pip/pip.conf` | CN mirror |

---

## Environment Variables

Sourced automatically by `.zshrc`:
- `~/envSetups/linuxSetup/envvar/exports` — PATH, LANG, GOPATH, GPG_TTY
- `~/envSetups/linuxSetup/envvar/aliases` — git/ssh/vim shortcuts

---

## Local Overrides (not tracked in repo)

- `~/.zshrc_local` — machine-specific zsh config
- `~/.ssh/config_local` — machine-specific SSH hosts
- SDKMAN for Java is loaded in `.zshrc` if present, install separately if needed

---

## Other Platforms

- **Windows**: see `windowsRegs/` for registry files (dual-boot UTC time, English fonts, 小鹤双拼)

---

## TODO

- [ ] Migrate dotfiles to GNU Stow structure (replace manual `ln -sf` with `stow <package>`)
- [ ] Remove `py-installer/` once this prompt-based setup is validated on a fresh machine
