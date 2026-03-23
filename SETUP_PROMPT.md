# Machine Setup Prompt

> This document describes how to set up a fresh machine.
> An AI agent with terminal access can execute this directly.
> It replaces the `py-installer` Python scripts.
>
> **Execution order matters** — sections are grouped by dependency.
> Steps within the same group can run in parallel.
>
> When executing each step, **quote the corresponding section** from this document
> so the user can see which instruction is being followed.
>
> **Record timing** for each step into `setup_timing.md` (markdown table with columns:
> Step, Description, Duration, Status) for post-setup analysis.
>
> Dotfiles are managed with [GNU Stow](https://www.gnu.org/software/stow/).
> All dotfile packages live in `~/envSetups/dotfiles/`.
> Running `stow <package>` from that directory creates symlinks into `$HOME`.

## Start Here

When this document is loaded, the agent should:

1. Ask the user: **Local or remote execution?**
2. If remote, ask for: SSH key path, username, host IP
3. Print the SSH command back to the user so they can connect from another terminal:
   ```
   ssh -i <key_path> <user>@<host>
   ```
4. Test the connection (`ssh -o ConnectTimeout=10 ...`)
5. Detect OS (`uname -a`, `/etc/os-release`)
6. Then proceed with §0 onwards

## 0. Prerequisites

The bootstrap script `py-installer/install.sh` handles cloning this repo and installing git/zsh/curl.
After that, this document takes over.

Assume:
- This repo is cloned at `~/envSetups`
- `git`, `zsh`, `curl`, `stow` are available
- The user's OS is either **macOS** or **Linux** (Ubuntu/Debian/Amazon Linux)

Detect the OS first and adapt all commands accordingly.

### Cloning the repo on a remote machine

The local repo uses SSH remote (`git@github.com:clbg/envSetups.git`), but a fresh
remote machine won't have GitHub SSH keys. Clone via HTTPS instead:

```
if [ -d ~/envSetups ]; then
  git -C ~/envSetups pull
else
  git clone https://github.com/clbg/envSetups.git ~/envSetups
fi
```

### Remote execution via SSH

When the target machine is remote (e.g. a cloud VPS), the agent can SSH from the
local machine to execute all commands. Use the SSH key and IP provided by the user:

```
SSH="ssh -i <key_path> <user>@<host>"
$SSH "<command>"
```

All subsequent steps prefix commands with `$SSH` instead of running locally.

---

## 1. Package Manager + Packages

### Desired packages

These tools should be installed. The agent decides HOW based on the OS:

```
htop fortune fzf tmux vim git curl wget rsync autojump the_silver_searcher
icdiff tldr bat direnv starship zoxide ripgrep tree ncdu stow mise neovim
```

### macOS GUI apps (via `brew install --cask`)
```
iterm2 karabiner-elements kindle telegram wechat deepl raycast
```

### Installation strategy

The agent should follow this priority at runtime:

1. **Prefer the native package manager** (apt/yum) — it's faster and has no dependency chain overhead.
   - Run `apt-cache show <pkg>` or equivalent to check availability before installing.
   - Some package names differ across distros (e.g. `bat` → `bat` on Debian 13+ but may need alias from `batcat` on older Ubuntu; `the_silver_searcher` → `silversearcher-ag` on apt; `fortune` → `fortune-mod`).
   - The agent should resolve name differences dynamically, not from a hardcoded mapping.
2. **Fall back to Homebrew** for anything the native package manager doesn't have.
   - On macOS, brew is the primary (and only) package manager.
   - On Linux, only install Linuxbrew if there are packages that apt/yum can't provide.
3. **Skip already-installed packages** — check `command -v <pkg>` first for idempotency.
4. **mise** has its own installer (`curl https://mise.jdx.dev/install.sh | sh`) — prefer that on Linux over brew.

### Linux pre-flight

- `sudo apt update` (or `yum update`)
- Install build essentials if needed: `build-essential procps file`
- On low-memory instances (< 1GB RAM, check with `free -m`), add swap:
  ```
  sudo fallocate -l 2G /swapfile && sudo chmod 600 /swapfile
  sudo mkswap /swapfile && sudo swapon /swapfile
  grep -q swapfile /etc/fstab || echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
  ```

### Homebrew (if needed)

- **macOS**: Install if not present: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
- **Linux**: Only install Linuxbrew if native package manager can't cover the package list.
  ```
  NONINTERACTIVE=1 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```
  Then: `eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"` and `brew install gcc`

### CN Mirror (if env var `CN=Y`)
- Set Homebrew mirror to Tsinghua:
  - `HOMEBREW_BREW_GIT_REMOTE=https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git`
  - `HOMEBREW_CORE_GIT_REMOTE=https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git`
  - `HOMEBREW_BOTTLE_DOMAIN=https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles`

---

## Group A — No package manager dependency (run in parallel with §1)

### A1. Shell — Zsh

1. If zsh is not the default shell, run `chsh -s /bin/zsh`
2. Stow zsh config:
   ```
   cd ~/envSetups/dotfiles && stow -t ~ zsh
   ```
3. Symlink bin scripts:
   ```
   ln -sf ~/envSetups/linuxSetup/bin ~/bin_local
   ```

### A2. Dotfiles — GNU Stow

All dotfile packages are in `~/envSetups/dotfiles/`. Each subdirectory is a stow package
that mirrors the home directory structure.

#### Link all common dotfiles
```
cd ~/envSetups/dotfiles
stow -R -t ~ zsh vim nvim ssh starship
```

#### macOS only
```
cd ~/envSetups/dotfiles
stow -R -t ~ karabiner
```

#### Linux desktop only
```
cd ~/envSetups/dotfiles
stow -R -t ~ i3
```

#### CN mirror only
```
cd ~/envSetups/dotfiles
stow -R -t ~ pip
```

#### Stow package reference

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

### A3. SSH (additional setup beyond stow)

The SSH config file is linked by stow above. Additional steps:

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
   grep -qiFf ~/envSetups/linuxSetup/key.pub ~/.ssh/authorized_keys 2>/dev/null || \
     cat ~/envSetups/linuxSetup/key.pub >> ~/.ssh/authorized_keys
   ```

### A4. Git Config

Configure git identity (run inside `~/envSetups`):
```
git config user.email "i@chengpeng.space"
git config user.name "Cheng Peng"
```

### A5. Runtime Version Manager — mise (Linux only, no brew needed)

On Linux, mise can be installed independently:
```
curl https://mise.jdx.dev/install.sh | sh
```
This installs a single Rust binary to `~/.local/bin/mise`.

On macOS, use `brew install mise` (part of §1).

The `.zshrc` already has:
```
eval "$(mise activate zsh)"
```

#### Install runtimes
```
mise use --global python@3.12
mise use --global node@22
```

> mise downloads prebuilt binaries — no compilation needed.

#### Per-project versions
Create a `.mise.toml` in any project directory:
```toml
[tools]
python = "3.11"
node = "20"
```
mise auto-switches when you `cd` into the directory.

#### Relationship with direnv
- **mise** = which Python/Node/etc binary to use (runtime versions)
- **direnv** = which env vars to set per directory (`.envrc` files)
- They work together without conflict. Both are loaded in `.zshrc`.

---

## 2. Post-install Steps (after §1 completes)

### 2.1 Neovim setup

The nvim config is linked by stow in A2. Additional steps:

1. Create vim undo directory:
   ```
   mkdir -p ~/.vim/undodir
   ```

> The config uses LazyVim — plugins auto-install on first launch (`nvim`).

### 2.2 fzf Shell Integration

Run the fzf installer for key bindings and completion:
```
# Find fzf install script — location depends on how fzf was installed
FZF_INSTALL=$(find /usr -name install -path "*/fzf/*" 2>/dev/null | head -1)
[ -z "$FZF_INSTALL" ] && FZF_INSTALL=$(brew --prefix 2>/dev/null)/opt/fzf/install
[ -f "$FZF_INSTALL" ] && $FZF_INSTALL --all
```

### 2.3 Cleanup

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

