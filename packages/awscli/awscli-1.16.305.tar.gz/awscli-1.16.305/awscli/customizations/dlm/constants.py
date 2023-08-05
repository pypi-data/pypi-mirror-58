# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

# Declare all the constants used by Lifecycle in this file

# Lifecycle role names
LIFECYCLE_DEFAULT_ROLE_NAME = "AWSDataLifecycleManagerDefaultRole"

# Lifecycle role arn names
LIFECYCLE_DEFAULT_MANAGED_POLICY_NAME = "AWSDataLifecycleManagerServiceRole"

POLICY_ARN_PATTERN = "arn:{0}:iam::aws:policy/service-role/{1}"

# Assume Role Policy definitions for roles
LIFECYCLE_DEFAULT_ROLE_ASSUME_POLICY = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "",
            "Effect": "Allow",
            "Principal": {"Service": "dlm.amazonaws.com"},
            "Action": "sts:AssumeRole"
        }
    ]
}
