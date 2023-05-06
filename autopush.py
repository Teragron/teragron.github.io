# -*- coding: utf-8 -*-
"""
Created on Sat May  6 01:36:27 2023

@author: ahmet
"""

import subprocess

def autopush(repo_path):
    # set up the Git commands
    commands = [
        ['git', 'add', '.'],
        ['git', 'commit', '-m', 'Auto-commit by script'],
        ['git', 'push']
    ]

    # run each Git command in a subprocess
    for cmd in commands:
        subprocess.run(cmd, cwd=repo_path)

    print("Changes pushed to GitHub.")

if __name__ == '__main__':
    # set the path to your local repository
    repo_path = 'teragron/teragron.github.io'

    # call the autopush function with the repo_path
    autopush(repo_path)
