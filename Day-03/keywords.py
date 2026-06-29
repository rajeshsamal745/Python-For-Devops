# Day-03: Python Keywords Summary
# Aws Devops Oriented Examples
# Author: Rajesh

import re
import boto3   

# Boolean keywords
print(True, False, None)

# Logical operators
cpu = 75
if cpu > 60 and cpu < 90:
    print("CPU usage is high")

# Conditional branching
state = "stopped"
if state == "stopped":
	print("Start EC2")
elif state == "running":
	print("Already Running")
else:
	print("Unknown state")
	
# Loops
buckets = ["devops-logs", "project-data"]
for b in buckets:
	print("Processing buckets:", b)

count = 0
while count < 2:
	print("Retry Deployment:", count)
	count += 1

# Loop Control
logs = ["WARNING", "ERROR", "INFO"]
for log in logs:
	if log == "ERROR":
		print("Error found")
		break
	else:
	    continue
	
# Functions
def get_metrics():
	return round(75.789, 2)
print("CPU Utilization:", get_metrics())

# Classes
class EC2Instance:
	def __init__(self, id, state):
		self.id = id
		self.state = state

instance = EC2Instance("i-1234", "running")
print("Instance:", instance.id, instance.state)

# Error Handeling
try:
	print("Calculating server capacity")
	server = 0
	capacity = 100/server
	print("Calculation successful")
except Exception as e:
	print("Error Caught:", e)
finally:
	print("Cleanup done")

# Context Manager
with open("config.txt", "w+") as f:
	f.write("region=us-east-1")
	f.seek(0)
	content = f.read()
	print("Config Content:", content)

# Import/from/as
from math import sqrt as square_root
print("Square root:", square_root(16))

# Scope
global_var = "AWS"
def test_scope():
	global global_var
	global_var = "Devops"
test_scope()
print("Global var:", global_var)

# Lambda
metrics = [65, 72, 82]
high = list(filter(lambda x: x > 70, metrics))
print("High metrics:", high)

# Assert
state = "Stopped"
assert state == "Stopped" , "Instance must be stopped"

# Delete
users = ["Rajesh", "Abhishek"]
del users[1]
print("Users:", users)

# Pass
def deploy_code():
	pass
print("Deployment logic will be implemented here")

# Yield (generator)
def stream_generator():
	yield "INFO: Deployment Started"
	yield "ERROR: S3 bucket not found"

for log in stream_generator():
	print("Log:", log)

# Raise
# raise RuntimeError("Simulated AWS error")

# Membership & identity
roles = ["Admin" , "Devops"]
roles_backup = ["Admin", "DevOps"]
if "Devops" in roles:
	print("Role Exist")
print(roles == roles_backup)
print("Check identity:", roles is roles)

# Async/Await (simplified demo)
import asyncio

async def fetch_ec2():
	print("Fetching ec2")
async def fetch_s3():
	print("Fetching s3")

async def main():
	await asyncio.gather(fetch_ec2(), fetch_s3())

asyncio.run(main())

