"""Detect running platform - zero external dependencies version"""
import os
import platform
from enum import Enum


class Distribution(Enum):
    """Supported distributions"""
    Amazon = "amzn"
    Arch = "arch"
    Debian = "debian"
    MacOS = "macos"
    Ubuntu = "ubuntu"
    Windows = "windows"
    Unknown = "unknown"


def get_distribution() -> Distribution:
    """Get distribution information (from env var or system detection)"""
    
    # Priority 1: Read from environment variable (injected by install.sh)
    os_id = os.environ.get("ENV_SETUP_OS", "").lower()
    if os_id:
        try:
            return Distribution(os_id)
        except ValueError:
            pass
    
    # Priority 2: Detect from system
    system = platform.system()
    
    if system == "Windows":
        return Distribution.Windows
    
    if system == "Darwin":
        return Distribution.MacOS
    
    if system == "Linux":
        return _detect_linux_distro()
    
    return Distribution.Unknown


def _detect_linux_distro() -> Distribution:
    """Detect Linux distribution by reading /etc/os-release"""
    try:
        with open("/etc/os-release", "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("ID="):
                    distro_id = line.strip().split("=")[1].strip('"').strip("'")
                    try:
                        return Distribution(distro_id)
                    except ValueError:
                        # Unknown distro, but we can still try to work with it
                        return Distribution.Unknown
    except FileNotFoundError:
        pass
    
    return Distribution.Unknown


def get_major_version() -> str:
    """Get system major version number"""
    
    # Priority 1: Read from environment variable (injected by install.sh)
    version = os.environ.get("ENV_SETUP_VERSION", "")
    if version:
        return version
    
    # Priority 2: Detect from system
    system = platform.system()
    
    if system == "Darwin":
        # macOS: Parse from platform.mac_ver()
        mac_version = platform.mac_ver()[0]
        if mac_version:
            return mac_version.split(".")[0]
        return "0"
    
    if system == "Linux":
        return _detect_linux_version()
    
    return "0"


def _detect_linux_version() -> str:
    """Detect Linux distribution version by reading /etc/os-release"""
    try:
        with open("/etc/os-release", "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("VERSION_ID="):
                    version_id = line.strip().split("=")[1].strip('"').strip("'")
                    # Return major version only
                    return version_id.split(".")[0]
    except FileNotFoundError:
        pass
    
    return "0"
