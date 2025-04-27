#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2023 Greg Albrecht <oss@undef.net>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""INRCOT Constants."""

__author__ = "Greg Albrecht <oss@undef.net>"
__copyright__ = "Copyright 2023 Greg Albrecht"
__license__ = "Apache License, Version 2.0"


# How long between checking for new messages at the Spot API?
DEFAULT_POLL_INTERVAL: int = 120

# How longer after producting the CoT Event is the Event 'stale' (seconds)
DEFAULT_COT_STALE: str = "600"

# Default CoT type. 'a-f-g-e-s' works in iTAK, WinTAK & ATAK...
DEFAULT_COT_TYPE: str = "a-f-g-e-s"

# Default username for Garmin MapShare, as the username is anyways ignored
DEFAULT_FEED_USERNAME: str = "InReach2TAK"