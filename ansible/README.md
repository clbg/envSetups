## Start:
### prequisite
```
ansible-galaxy install gantsign.oh-my-zsh
```
### run
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
ansible-playbook --ask-become-pass deploy.yml -i inventory.yml
```
