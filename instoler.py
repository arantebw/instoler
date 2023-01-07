#!/usr/bin/env python

# install_vins.py
# Download and intall all of the vim plugins indicated in the vins.csv.
#
# How to execute:
# python install_vins.py ~/.dotfiles/vins.csv
#
# TODO: In coc.nvim, switch to the release branch after installation.

import sys
import os


def get_repos(file):
    with open(file, 'r') as f:
        repos = f.read()

    repos_list = repos.split('\n')

    return repos_list[:-1] # exclude last item which empty


def main(file):
    repos_list = get_repos(file)

    vins_dir = '~/.vim/pack/third-party/start/'
    for repo in repos_list:
        ssh_uri = repo.split(',')[0]
        repo_dir = vins_dir + repo.split(',')[1]
        os.system(f'git clone {ssh_uri} {repo_dir}')


if __name__ == '__main__':
    main(sys.argv[1])
