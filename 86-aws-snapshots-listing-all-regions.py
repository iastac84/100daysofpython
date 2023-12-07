import boto3
import botocore

def get_account_number():
    try:
        sts_client = boto3.client('sts')
        account_id = sts_client.get_caller_identity()['Account']
        return account_id
    except botocore.exceptions.ClientError as e:
        print(f"Error retrieving account number: {e}")
        return None

def list_snapshots():
    # Get the AWS account number
    account_number = get_account_number()
    if not account_number:
        return

    # Initialize the AWS EC2 client
    ec2 = boto3.client('ec2')

    # Retrieve all AWS regions
    ec2_regions = [region['RegionName'] for region in ec2.describe_regions()['Regions']]

    print("Account Number\tSnapshot ID\tName\tCreation Date\tVolume ID\tRegion\tOrphaned\tSize (GiB)\tDescription")
    print("-------------------------------------------------------------------------------------------------")

    for region in ec2_regions:
        # Create a client for each region
        ec2_region_client = boto3.client('ec2', region_name=region)

        # Retrieve all snapshots in the current region
        snapshots = ec2_region_client.describe_snapshots(OwnerIds=['self'])['Snapshots']

        # Get a list of all existing volume IDs and their regions
        volumes = ec2_region_client.describe_volumes()['Volumes']
        existing_volumes_info = {volume['VolumeId']: volume['AvailabilityZone'] for volume in volumes}

        for snapshot in snapshots:
            snapshot_id = snapshot['SnapshotId']
            creation_date = snapshot['StartTime']
            description = snapshot['Description'] if 'Description' in snapshot else 'No Description'

            # Get the VolumeId (if available) and the region
            volume_id = snapshot.get('VolumeId', 'N/A')
            region = existing_volumes_info.get(volume_id, 'N/A')

            # Get the snapshot size
            size = snapshot['VolumeSize']

            # Get the name tag (if available)
            tags = snapshot.get('Tags', [])
            name_tag = next((tag['Value'] for tag in tags if tag['Key'] == 'Name'), 'N/A')

            # Check if the snapshot is orphaned by verifying if its volume ID exists
            orphaned = "Yes" if volume_id not in existing_volumes_info else "No"

            print(f"{account_number}\t{snapshot_id}\t{name_tag}\t{creation_date}\t{volume_id}\t{region}\t{orphaned}\t{size}\t{description}")
            

if __name__ == "__main__":
    list_snapshots()

