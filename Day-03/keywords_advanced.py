import re
import boto3
import asyncio

# -------------------------------
# 1. Boolean, None, Logic
# -------------------------------
ec2_state = "running"
if ec2_state == "running":
	is_active = True
else:
	is_active = False
	
print("EC2 Active:", is_active)

metric = None
if metric is None:
	print("No cloudwatch metric avaiable")

# -------------------------------
# 2. Conditional Branching
# -------------------------------
cpu = 85
if cpu > 90:
	print("Critical cpu alert")
elif cpu > 80 and cpu <= 90:
	print("High cpu alert")
else:
	print("Normal CPU Usage")

# -------------------------------
# 3. Loops with Control
# -------------------------------
instances = ["i-123", "i-456", "i-789"]
for inst in instances:
	if "456" in inst:
		print("skipping instances:", inst)
		continue
	print("processing:", inst)
	if inst == "i-789":
		print("Breaking loop at:", inst)
		break

# -------------------------------
# 4. Classes & Objects
# -------------------------------
class EC2Instance:
	def __init__(self, id, state):
		self.id = id
		self.state = state
	
	def start(self):
		if self.state == "stopped":
			self.state == "running"
			print(f"Instance {self.id} started")
		else:
			print(f"Instance {self.id} already running")
instance = EC2Instance("i-123", "stopped")
instance.start()