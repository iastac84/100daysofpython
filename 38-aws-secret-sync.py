#!/usr/bin/env python3
# Day 38

'''
Python script that uses the AWS SDK (boto3) to monitor AWS Secrets Manager and retry the sync for secrets that are not replicating:
Make sure you have the Boto3 library installed (pip install boto3) and the appropriate AWS credentials configured on your system to run this script successfully. Update the secret_name variable with the name of the secret you want to monitor.
'''

import os
import boto3
import time

def check_secret_replication(secret_name):
    client = boto3.client('secretsmanager')

    while True:
        response = client.describe_secret(SecretId=secret_name)
        replication_status = response.get('ReplicationStatus')

        if isinstance(replication_status, dict):
            replication_status = replication_status.get('Status')

        if replication_status == 'ReplicationInProgress':
            print(f"Replication in progress for secret '{secret_name}'...")
            time.sleep(5)  # Wait for 5 seconds before checking again
        elif replication_status == 'ReplicationFailed':
            print(f"Replication failed for secret '{secret_name}'. Retrying...")

            try:
                client.retry_secret_replication(SecretId=secret_name)
                print(f"Retry initiated for secret '{secret_name}'")
            except Exception as e:
                print(f"Failed to retry replication for secret '{secret_name}': {str(e)}")

            time.sleep(5)  # Wait for 5 seconds before checking again
        elif replication_status == 'ReplicationComplete':
            print(f"Replication completed for secret '{secret_name}'")
            break
        else:
            print(f"Unknown replication status '{replication_status}' for secret '{secret_name}'")
            break

# Get secret_name from environment variable
secret_name = os.environ.get('SECRET_NAME')

if secret_name is None:
    print("Please set the SECRET_NAME environment variable.")
else:
    check_secret_replication(secret_name)

