# ec2_utils.py
import random

def check_cpu(instance_id, threshold=80):
    cpu = random.randint(40, 95)  # Simulated CloudWatch metric
    return cpu > threshold

def scale_instance(instance_id):
    print(f"Scaling EC2 instance {instance_id} to larger type...")
