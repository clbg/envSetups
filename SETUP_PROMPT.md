# Machine Setup Prompt

> This document describes how to set up a fresh machine.
> An AI agent with terminal access can execute this directly.
> It replaces the `py-installer` Python scripts.
>
> **Execution order matters** — follow the numbered sections sequentially.
>
> Dotfiles are managed with [GNU Stow](https://www.gnu.org/software/stow/).
> All dotfile packages live in `~/envSetups/dotfiles/`.
> Running `stow <package>` from that directory creates symlinks into `$HOME`.

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
3. Stow zsh config:
   ```
   cd ~/envSetups/dotfiles && stow -t ~ zsh
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

## 5. Dotfiles — GNU Stow

All dotfile packages are in `~/envSetups/dotfiles/`. Each subdirectory is a stow package
that mirrors the home directory structure.

### Link all common dotfiles
```
cd ~/envSetups/dotfiles
stow -t ~ zsh vim nvim ssh starship
```

### macOS only
```
cd ~/envSetups/dotfiles
stow -t ~ karabiner
```

### Linux desktop only
```
cd ~/envSetups/dotfiles
stow -t ~ i3
```

### CN mirror only
```
cd ~/envSetups/dotfiles
stow -t ~ pip
```

### Stow package reference

| Package | Creates symlink | Condition |
|---|---|---|
| `zsh` | `~/.zshrc` | all |
| `vim` | `~/.vimrc` | all |
| `nvim` | `~/.config/nvim/` | all |
| `ssh` | `~/.ssh/config` | all |
| `starship` | `~/.config/starship.toml` | all |
| `karabiner` | `~/.config/karabiner/` | macOS |
| `i3` | `~/.i3/config` | Linux desktop |
| `pip` | `~/.config/pip/pip.conf` | CN mirror |

> To unlink a package: `stow -t ~ -D <package>`
> To re-link (after changes): `stow -t ~ -R <package>`

---

## 6. SSH (additional setup beyond stow)

The SSH config file is linked by `stow ssh` above. Additional steps:

1. Create `.ssh` directory (if not exists):
   ```
   mkdir -p ~/.ssh
   ```
2. Create local override file (for machine-specific hosts):
   ```
   touch ~/.ssh/config_local
   ```
3. Append public key to authorized_keys (if not already present):
   ```
   grep -qiFf ~/envSetups/linuxSetup/linkFiles/key.pub ~/.ssh/authorized_keys 2>/dev/null || \
     cat ~/envSetups/linuxSetup/linkFiles/key.pub >> ~/.ssh/authorized_keys
   ```

---

## 7. Neovim (additional setup beyond stow)

The nvim config is linked by `stow nvim` above. Additional steps:

1. Install neovim: `brew install neovim`
2. Create vim undo directory:
   ```
   mkdir -p ~/.vim/undodir
   ```

> The nvim config uses LazyVim. Plugins will auto-install on first launch (`nvim`).

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

## 10. Cleanup

```
brew cleanup --prune=all
```

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

- [ ] Remove `py-installer/` once this prompt-based setup is validated on a fresh machine
