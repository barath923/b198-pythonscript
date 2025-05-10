import boto3

accesskey = sys.argv[1]
secretkey = sys.argv[2]
region = sys.argv[3]

client = boto3.client(
    'ec2',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region=REGION_NAME
)

response = client.create_vpc(
    CidrBlock='10.10.0.0/16',
    TagSpecifications=[
        {
            'ResourceType':'vpc',
		      	'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'VPC-NEW'
                }
            ]
        }
    ]
)

print ("VPC ID: ", response['Vpc']['VpcId'])
