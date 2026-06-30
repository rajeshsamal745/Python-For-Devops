# __init__.py
# Day-04: AWS Package Initialization
# Author: Rajesh

# Import key modules so they are available directly from aws_package
from . import ec2_utils
from . import s3_utils
from . import iam_utils

# Define what gets exported when someone does: from aws_package import *
__all__ = ["ec2_utils", "s3_utils", "iam_utils"]

# Optional: Package-level helper function
def package_info():
    return {
        "name": "aws_package",
        "modules": __all__,
        "description": "Reusable AWS DevOps utilities for EC2, S3, IAM"
    }
