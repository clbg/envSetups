# envSetups
some scripts to set up my computer 

## prequesite

### macOS

#### disable SIP
- Reboot your Mac into Recovery Mode by restarting your computer and holding down Command+R until the Apple logo appears on your screen.
- Click Utilities > Terminal.
- In the Terminal window, type in `csrutil disable` and press Enter.
- Restart your Mac.

## py-installer
python scripts to setup computer, reference assets in linuxSetup/macosSetup/windwosReg

make sure you have pip3 installed before run 
```
curl -sL chengpeng.space/i | bash

```

## linuxSetup
assets for linux

## macosSetup
assets for macos

## windowsReg
some reg files with config on windows

## CheatSheets

### switching from https to git
```
git remote set-url origin git@github.com:pengchengbuaa/envSetups.git
```
### switching to tunna mirror of brew
```
git -C "$(brew --repo)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git
git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git
git -C "$(brew --repo homebrew/cask)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-cask.git
git -C "$(brew --repo homebrew/cask-fonts)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-cask-fonts.git
git -C "$(brew --repo homebrew/cask-drivers)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-cask-drivers.git
git -C "$(brew --repo homebrew/cask-versions)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-cask-versions.git
```

### hi-DPI
```
bash -c "$(curl -fsSL https://raw.githubusercontent.com/xzhih/one-key-hidpi/master/hidpi.sh)"
```

