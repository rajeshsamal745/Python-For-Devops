# Day-02: Python Data Types, Strings, Numers, Regex
# AWS Devops oriented
# Author: Rajesh Kumar

import re

# ----------------
# 1. String Handling
# ----------------
arn = "arn:aws:iam::123456789012:user/abhishek"
username = arn.split("/")[-1]
print("IAM User : ", username)

# Uppercase conversion
role = "devopsadmin"
print("Normalized Role : ", role.upper())

# Lowercase conversion
role = "devOpsAdmin"
print("Lowercase role:", role.lower())

# Replace
arn = "arn:aws:iam::123456789012:user/abhishek"
print("Replace user:", arn.replace("abhishek", "rajesh"))

# Split
parts = arn.split("/")
print("Split arn:", parts)
print("Extracted IAM User:", parts[-1])

# Strip
raw = "   EC2-instance   "
print("Stripped:", raw.strip())

# Substring (slice)
region = "us-east-1"
print("Substring (first 5 chars):", region[:5])

# Concatenation for S3 bucket naming
bucket = "devops-logs"
region = "us-east-1"
s3_path = bucket + "-" + region
print("S3 Bucket Path : ", s3_path)

# Length check for resource naming
key = "project-data-backup"
if len(key) > 5:
	print("Warning: S3 key name too long")


# -----------------------
# 2. Numeric Data Types
# -----------------------
ec2_count = 6
if ec2_count > 5:
	print("Scaling required: Too many EC2 instances")
	
cpu = 74.787
print("CPU Utilization:", round(cpu, 2), "%")

drift = -5
print("Config Drift:", abs(drift))

# ----------------------
# 3. Regx for parsing
# ----------------------
log = "2026-06-27 ERROR: EC2 instance stopped"
if re.search("ERROR", log):
	print("Alert: Error detected in logs")
	
# Extract EC2 instance ID from logs
text = "Instance i-0abcd1234efgh5678 terminated"
# Findall
ids = re.findall(r"i-[0-9a-f]+", text)
print("Findall EC2 IDs:", ids)

# Match
match = re.match(r"EC2", text)
if match:
    print("Match found:", match.group())
	
# -------------------------------
# 4. Problem-Solving Attitude
# -------------------------------
# Instead of manual checks, automate:

log = [
	"2026-06-27 INFO: Deployment started",
	"2026-06-27 ERROR: S3 bucket not found",
	"2026-06-27 WARNING: High CPU usage"
]
for entry in log:
	if re.search("ERROR", entry):
		print("Error flagged:", entry)
	if re.search("WARNING", entry):
		print("Warning Detected:", entry)
