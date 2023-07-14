#!/usr/bin/env python3
# Day 38

'''
Python script that uses the AWS SDK (boto3) to list secrets in AWS Secrets Manager 
Make sure you have the Boto3 library installed (pip install boto3) and the appropriate AWS credentials configured on your system to run this script successfully. 
'''

import subprocess

def run_aws_cli_command(command):
    try:
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        return output.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing AWS CLI command: {e}")
        return None

# Example: List all secrets using AWS CLI
aws_cli_command = 'aws secretsmanager list-secrets --query "SecretList[*].Name" --output text'
secrets_output = run_aws_cli_command(aws_cli_command)

if secrets_output:
    secrets_list = secrets_output.split()
    for secret in secrets_list:
        print(f"Secret Name: {secret}")

