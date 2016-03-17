# Copyright 2016 Splunk, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"): you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
The Splunk Software Development Kit for Solutions.
"""

from splunksolutionlib import common
from splunksolutionlib import acl
from splunksolutionlib import credentials
from splunksolutionlib import kvstore
from splunksolutionlib import metadata
from splunksolutionlib import server_info
from splunksolutionlib import splunkenv
from splunksolutionlib import http_request

__all__ = ['common',
           'acl',
           'credentials',
           'kvstore',
           'metadata',
           'server_info',
           'splunkenv',
           'http_request']

__version__ = '1.0.0'
