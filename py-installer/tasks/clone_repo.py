import os
from ..utils.run_bash import run_bash


def clone_repo():
    home_path = os.getenv('HOME')
    os.chdir(home_path)
    if os.path.exists('envSetups'):
        print("pulling envSetup commits")
        run_bash('git -C envSetups pull')
    else:
        print('cloning envSetups repo.')
        run_bash('git clone https://github.com/pengchengbuaa/envSetups.git')
        print("cloning done.")
