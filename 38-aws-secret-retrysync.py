#!/usr/bin/env python3
# Day 38

'''
Python script that uses the AWS SDK (boto3) to monitor AWS Secrets Manager
(set as an environment variable)
Make sure you have the Boto3 library installed (pip install boto3) and the appropriate AWS credentials configured on your system to run this script successfully. 
'''
import boto3
import time

def check_sync_and_retry_secrets(event, context):
    client = boto3.client('secretsmanager')
    
    secrets = client.list_secrets()['SecretList']
    
    for secret in secrets:
        secret_id = secret['Name']
        replication_status = secret.get('ReplicationStatus')
        
        if replication_status != 'Enabled':
            print(f"Secret '{secret_id}' is not enabled for replication. Retrying...")
            
            try:
                client.enable_secret_replication(SecretId=secret_id)
                time.sleep(5)  # Wait for replication to be enabled
                replication_status = client.describe_secret(SecretId=secret_id)['ReplicationStatus']
                
                if replication_status == 'Enabled':
                    print(f"Replication enabled successfully for secret '{secret_id}'.")
                else:
                    print(f"Failed to enable replication for secret '{secret_id}'.")
                
            except Exception as e:
                print(f"An error occurred while enabling replication for secret '{secret_id}': {e}")
        
        else:
            print(f"Replication is already enabled for secret '{secret_id}'.")
    
    return {
        'statusCode': 200,
        'body': 'Replication status check completed.'
    }

