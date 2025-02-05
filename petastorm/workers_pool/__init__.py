#  Copyright (c) 2017-2018 Uber Technologies, Inc.
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


class EmptyResultError(RuntimeError):
    """Exception used to signal that there are no new elements in the queue and no new elements are expected, unless
    ventilate is called again"""


class TimeoutWaitingForResultError(RuntimeError):
    """Indicates that timeout has elapsed while waiting for a result"""


class VentilatedItemProcessedMessage(object):
    """Object to signal that a worker has completed processing an item from the ventilation queue"""

class OrderedVentilatedItemProcessedMessage(VentilatedItemProcessedMessage):
    """Ventilated signal object which contains ordering metadata."""
    def __init__(self, idx):
        self.idx = idx