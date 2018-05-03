# Copyright (c) 2017-present, Facebook, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##############################################################################

"""Collection of available datasets."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os


# Path to data dir
DATA_IM_DIR = os.environ['DATA_IM_DIR']
DATA_ANN_FN = os.environ['ANN_FN']

if 'DATA_RAW_DIR' in os.environ:
    DATA_RAW_DIR = os.environ['DATA_RAW_DIR']
else:
    DATA_RAW_DIR = ''

if 'DATA_DEVKIT_DIR' in os.environ:
    DATA_DEVKIT_DIR = os.environ['DATA_DEVKIT_DIR']
else:
    DATA_DEVKIT_DIR = ''

if 'IM_PREFIX' in os.environ:
    IM_PREFIX = os.environ['IM_PREFIX']
else:
    IM_PREFIX = 'image_prefix'
