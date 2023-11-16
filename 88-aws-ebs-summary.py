#!/usr/bin/env python3
# Day 88

# Count EBS volumes by type and return quantities and total size

import os
import boto3

def count_ebs_volumes():
    # Retrieve AWS profile from environment variable
    aws_profile = os.getenv('AWS_PROFILE')

    if not aws_profile:
        print("Please set AWS_PROFILE as an environment variable.")
        return

    # Initialize AWS session with specified profile
    session = boto3.Session(profile_name=aws_profile)

    # Get all AWS regions
    ec2_client = session.client('ec2')
    aws_regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

    # Dictionary to store volume counts and total sizes
    volume_info = {}

    for region in aws_regions:
        # Initialize EC2 client for the region
        ec2_client = session.client('ec2', region_name=region)

        # Retrieve all EBS volumes for the region
        response = ec2_client.describe_volumes()

        for volume in response['Volumes']:
            volume_type = volume['VolumeType']
            volume_size = volume['Size']

            if volume_type in volume_info:
                volume_info[volume_type]['count'] += 1
                volume_info[volume_type]['total_size_gb'] += volume_size
            else:
                volume_info[volume_type] = {
                    'count': 1,
                    'total_size_gb': volume_size
                }

    return volume_info

# Get EBS volume counts and total sizes for all regions
ebs_volume_info = count_ebs_volumes()

if ebs_volume_info:
    # Display the results
    for volume_type, info in ebs_volume_info.items():
        print(f"EBS Volume Type: {volume_type}")
        print(f"Number of Volumes: {info['count']}")
        print(f"Total Size (GB): {info['total_size_gb']}")
        print("-----------")
