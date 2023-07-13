#!/usr/bin/env python3
# Day 38

'''
Python script that uses the AWS SDK (boto3) to monitor AWS Secrets Manager  and returns the replication status of the specified secret 
(set as an environment variable)
Make sure you have the Boto3 library installed (pip install boto3) and the appropriate AWS credentials configured on your system to run this script successfully. Update the secret_name variable with the name of the secret you want to monitor.
'''

import os
import boto3

def get_secret_replication_status(secret_name):
    client = boto3.client('secretsmanager')
    response = client.describe_secret(SecretId=secret_name)
    
    replication_status = response.get('ReplicationStatus')
    
    if isinstance(replication_status, dict):
        replication_status = replication_status.get('Status')
    
    return replication_status

# Get secret_name from environment variable
secret_name = os.environ.get('SECRET_NAME')

if secret_name is None:
    print("Please set the SECRET_NAME environment variable.")
else:
    replication_status = get_secret_replication_status(secret_name)
    print(f"Replication status for secret '{secret_name}': {replication_status}")
    print("") 
    print(f'{replication_status}')

