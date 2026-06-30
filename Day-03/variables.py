# Day-03: Variables in Python
# Advanced AWS DevOps Oriented Examples
# Author: Rajesh

import re

# -------------------------------
# 1. Basic Web Server Config (Level-1)
# -------------------------------
server_name = "my_server"
port = 80
is_http_enabled = True
max_connections = 1000

print(f"Server Name: {server_name}")
print(f"Port:, {port}")
print(f"HTTP Enabled:, {is_http_enabled}")
print(f"Max Connections;, {max_connections}") 

# Update Configuration
port = 483
is_http_enabled = False
print(f"Updated port: {port} , HTTP Enabled: {is_http_enabled}")

# -------------------------------
# 2. EC2 Resource Variables 
# -------------------------------
instance_id = "i-0abcd1234efgh5678"
region = "us-east-1"
instance_type = "t2.micro"
print(f"Instance {instance_id} in {region} running as {instance_type}")

# -------------------------------
# 3. Scope Control 
# -------------------------------
account_id = "123456789012" #Global Variables
def get_bucket_name(env):
	bucket_name = f"{env}-logs-{account_id}"
	return bucket_name

print("Dev bucket:", get_bucket_name("dev"))
print("Prod bucket:", get_bucket_name("prod"))

# -------------------------------
# 4. Variables Driving Automation 
# -------------------------------
cpu_utilization = 80
threshold  = 70
if cpu_utilization > threshold:
	action = "scale_up"
else:
	action = "no-action"
print(f"Decision based on CPU: {action}")

# -------------------------------
# 5. Structured Configs 
# -------------------------------
config = {
	"ec2": {"instance_type": "t2.micro", "region": "us-east-1"},
	"s3":  {"bucket": "devops-logs", "versioning": True},
	"rds": {"engine": "mysql", "size": "db.t2.small"}
}
print("EC2 Config:", config["ec2"])
print("s3 Config:", config["s3"])
print("rds Config:", config["rds"])

# -------------------------------
# 6. Real-Time Monitoring & Remediation
# -------------------------------
logs = [
    "ERROR: EC2 i-12345 stopped unexpectedly",
    "WARNING: High CPU usage on i-67890",
    "INFO: Deployment successful"
]
error_count = 0
warning_count = 0

for log in logs:
	if re.search("ERROR", log):
		error_count += 1
	elif re.search("WARNING", log):
		warning_count += 1
print(f"Errors: {error_count} , Warnings: {warning_count}")

if error_count > 0:
	remediation_action = "restart_instance"
elif warning_count > 0:
	remediation_action = "scale_up"
else:
	remediation_action = "no-action"

print("Remediation Action:", remediation_action)

# -------------------------------
# 7. Advanced Variable Usage 
# -------------------------------
# Variables controlling multi-environment deployments

environments = ["dev", "staging", "prod"]
deployment_status = {}
for env in environments:
    if env == "staging":
        deployment_status[env] = "failed"
    else:
        deployment_status[env] = "success"

print("Deployment status:", deployment_status)

# Conditional remediation based on variable values
for env, status in deployment_status.items():
    if status == "failed":
        print(f"🚨 Remediate deployment in {env} environment")