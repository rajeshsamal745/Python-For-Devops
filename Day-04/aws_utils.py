# aws_utils.py
import boto3

def list_s3_buckets():
    s3 = boto3.client("s3")
    return [bucket["Name"] for bucket in s3.list_buckets()["Buckets"]]

def start_instance(instance_id):
    ec2 = boto3.client("ec2")
    ec2.start_instances(InstanceIds=[instance_id])
    return f"Instance {instance_id} started"
