#!/usr/bin/env python3
# Day 30

'''
Python script that lists all EC2 instances in a specified AWS region and outputs the Name tag, instance ID, IP address, state, and Availability Zone
Make sure you have the Boto3 library installed (pip install boto3) and the appropriate AWS credentials configured on your system to run this script successfully. Replace the region_name variable with the desired AWS region where you want to list the instances.
'''

import boto3

def list_ec2_instances(region):
    ec2_client = boto3.client('ec2', region_name=region)
    response = ec2_client.describe_instances()

    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            state = instance['State']['Name']
            private_ip = instance.get('PrivateIpAddress', 'N/A')
            name_tag = ''

            for tag in instance.get('Tags', []):
                if tag['Key'] == 'Name':
                    name_tag = tag['Value']
                    break

            instances.append({
                'Name': name_tag,
                'Instance ID': instance_id,
                'State': state,
                'Private IP': private_ip
            })

    return instances

region = 'us-west-2'
instances = list_ec2_instances(region)

for instance in instances:
    output = f"Name: {instance['Name']} | Instance ID: {instance['Instance ID']} | State: {instance['State']} | Private IP: {instance['Private IP']}"
    print(output)

