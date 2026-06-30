from aws_package import ec2_utils, s3_utils

def monitor_and_remediate(instance_id):
	cpu_high = ec2_utils.check_cpu(instance_id)
	if cpu_high:
		print("High CPU detected, scalling up")
		ec2_utils.scale_instance(instance_id)
	else:
		print("CPU Normal no action required")

def backup_logs():
	print("Uploading logs to s3")
	s3_utils.upload_logs("devops-logs", "system.log")

monitor_and_remediate("i-0abcd1234efgh5678")
backup_logs()