#!/usr/bin/env python3
# Day 38

'''
Python script that uses the AWS SDK (boto3) to list secrets in AWS Secrets Manager 
Make sure you have the Boto3 library installed (pip install boto3) and the appropriate AWS credentials configured on your system to run this script successfully. 

updated version of the script that incorporates pagination to fetch and print all secrets:
'''

import boto3

def list_all_secrets():
    client = boto3.client('secretsmanager')
    paginator = client.get_paginator('list_secrets')
    response_iterator = paginator.paginate()

    for page in response_iterator:
        secrets = page['SecretList']
        for secret in secrets:
            secret_name = secret['Name']
            print(f"Secret Name: {secret_name}")

            # You can access other attributes of the secret as well
            # For example: secret_arn = secret['ARN']
            #             secret_description = secret['Description']

            # Perform any desired operations with the secret information

    # Alternatively, you can return the list of secrets
    # return secrets

# Call the function to list all secrets
list_all_secrets()

