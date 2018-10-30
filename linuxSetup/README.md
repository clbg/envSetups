# bin
some programs in this folder, which is soft linked to $HOME/bin through linkFiles/link.sh

# linkFiles
linkFiles are some config files you should replace with on your system, their filenames indicate where you should put them.
every file in this folder is named by their target paths,
linked by "-" and all UPPER LETTERS should be replaced by environmental  variables

for example, the file named "HOME-.config-pip-pip.conf"

first, replace "-" to / and add a"$" before UPPER LETTERS

whose filename  becomes "$HOME/config/pip/pip.conf", which is exactly the path you shold put it to.

in fact you don't need to do these manually,
all these linking works are done by link.sh including the job linking the 'bin' folder

# shellSetup
installing ohmyzsh using ohmyzsh-install script on github

# install.sh
a universal script, can be run on various linux distributions theoretically,

though only ubuntu, arch and kali can run correctly currently.

it's an entrypoint for all the installing jobs

which do jobs including :
 - updating sourcelist to mirrors in tuna.tsinghua.edu.cn or neusoft.edu.cn which are all ipv6-ready
 - installing common tools like git zsh curl wget for following jobs
 - cloneing envSetup (this repo) to $HOME and link the files in linkFiles and install ohmyzsh

# exampleOneLineInstall
if curl or wget is installed, a one-line bash script can be executed to get full install.sh and run it

otherwise, you may have to copy-paste or transfer it to machine, and run it 


