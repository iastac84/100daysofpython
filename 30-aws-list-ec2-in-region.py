#!/usr/bin/env python3
# Day 30

'''
Python script that lists all EC2 instances in a specified AWS region and outputs the Name tag, instance ID, IP address, state, and Availability Zone
Make sure you have the Boto3 library installed (pip install boto3) and the appropriate AWS credentials configured on your system to run this script successfully. Replace the region_name variable with the desired AWS region where you want to list the instances.
'''

import boto3

def list_ec2_instances(region_name):
    ec2_client = boto3.client('ec2', region_name=region_name)
    response = ec2_client.describe_instances()

    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            name_tag = ''
            if 'Tags' in instance:
                for tag in instance['Tags']:
                    if tag['Key'] == 'Name':
                        name_tag = tag['Value']
                        break
            ip_address = instance.get('PrivateIpAddress', 'N/A')
            state = instance['State']['Name']
            availability_zone = instance['Placement']['AvailabilityZone']

            instances.append({
                'Instance ID': instance_id,
                'Name Tag': name_tag,
                'IP Address': ip_address,
                'State': state,
                'Availability Zone': availability_zone
            })

    return instances


# Specify the AWS region you want to list instances from
region_name = 'us-east-1'  # Replace with your desired region

# List EC2 instances in the specified region
instances = list_ec2_instances(region_name)

# Print the details of each instance
for instance in instances:
    print("Instance ID:", instance['Instance ID'])
    print("Name Tag:", instance['Name Tag'])
    print("IP Address:", instance['IP Address'])
    print("State:", instance['State'])
    print("Availability Zone:", instance['Availability Zone'])
    print()

