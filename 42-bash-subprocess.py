#!/usr/bin/env python3
# Day 42

"""
you can run bash commands within Python using the subprocess module. The subprocess module allows you to execute arbitrary commands, including bash commands, from within a Python script.
"""

import subprocess

def run_bash_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing bash command: {e}")
        return None

# Example: Run 'ls' command
bash_command = 'ls -l'
output = run_bash_command(bash_command)

if output:
    print(output)

