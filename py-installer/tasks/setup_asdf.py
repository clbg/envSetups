"""Setup asdf - unified runtime version manager"""
from ..utils.run_bash import run_zsh
from ..utils.color_log import log, warn
from ..utils.running_platform import Distribution
from ..installerConfig import InstallerConfig


def setup_asdf(config: InstallerConfig):
    """Install and configure asdf for Python, Node.js, etc."""
    log("Setting up asdf (unified runtime manager)...")
    
    # 1. Check if asdf is already installed
    if run_zsh('command -v asdf', ignore_error=True) == 0:
        log("asdf already installed, checking for updates...")
        update_asdf(config.dist)
    else:
        log("Installing asdf...")
        install_asdf(config.dist)
    
    # 2. Install plugins
    install_plugins(config)
    
    # 3. Install runtimes
    install_runtimes(config)
    
    log("asdf setup completed ✓")


def install_asdf(dist: Distribution):
    """Install asdf based on distribution"""
    if dist == Distribution.MacOS:
        # Use Homebrew on macOS
        run_zsh('brew install asdf')
    else:
        # Use git clone on Linux
        run_zsh('git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.14.0', 
                ignore_error=True)  # Ignore if already exists


def update_asdf(dist: Distribution):
    """Update asdf to latest version"""
    if dist == Distribution.MacOS:
        run_zsh('brew upgrade asdf', ignore_error=True)
    else:
        run_zsh('cd ~/.asdf && git fetch && git checkout $(git describe --tags `git rev-list --tags --max-count=1`)',
                ignore_error=True)


def install_plugins(config: InstallerConfig):
    """Install asdf plugins for different runtimes"""
    log("Installing asdf plugins...")
    
    runtimes = config.get_asdf_runtimes()
    for plugin in runtimes.keys():
        log(f"Adding plugin: {plugin}")
        # Ignore errors if plugin already exists
        run_zsh(f'asdf plugin add {plugin}', ignore_error=True)


def install_runtimes(config: InstallerConfig):
    """Install runtime versions defined in config"""
    log("Installing runtimes (this may take a while)...")
    
    runtimes = config.get_asdf_runtimes()
    
    for plugin, versions in runtimes.items():
        log(f"Installing {plugin} versions: {', '.join(versions)}")
        
        for version in versions:
            # Check if version is already installed
            if run_zsh(f'asdf list {plugin} | grep -q {version}', ignore_error=True) == 0:
                log(f"  {plugin} {version} already installed ✓")
            else:
                log(f"  Installing {plugin} {version}...")
                run_zsh(f'asdf install {plugin} {version}')
        
        # Set global version to the first in the list
        global_version = versions[0]
        log(f"Setting global {plugin} version to {global_version}")
        run_zsh(f'asdf global {plugin} {global_version}')
