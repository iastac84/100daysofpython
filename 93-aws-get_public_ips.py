import boto3

def get_public_ips_all_regions():
    ec2 = boto3.client('ec2')
    
    # Get all AWS regions
    regions = [region['RegionName'] for region in ec2.describe_regions()['Regions']]

    public_ips = []

    for region in regions:
        ec2 = boto3.client('ec2', region_name=region)
        
        # Describe instances in the current region to get their public IPs
        instances = ec2.describe_instances()

        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                if 'PublicIpAddress' in instance:
                    public_ips.append(instance['PublicIpAddress'])

    return public_ips

if __name__ == "__main__":
    public_ips = get_public_ips_all_regions()
    
    if public_ips:
        print("Public IP addresses in all AWS regions:")
        for ip in public_ips:
            print(ip)
    else:
        print("No public IP addresses found in any AWS region.")

