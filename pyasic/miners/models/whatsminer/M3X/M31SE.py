# ------------------------------------------------------------------------------
#  Copyright 2022 Upstream Data Inc                                            -
#                                                                              -
#  Licensed under the Apache License, Version 2.0 (the "License");             -
#  you may not use this file except in compliance with the License.            -
#  You may obtain a copy of the License at                                     -
#                                                                              -
#      http://www.apache.org/licenses/LICENSE-2.0                              -
#                                                                              -
#  Unless required by applicable law or agreed to in writing, software         -
#  distributed under the License is distributed on an "AS IS" BASIS,           -
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.    -
#  See the License for the specific language governing permissions and         -
#  limitations under the License.                                              -
# ------------------------------------------------------------------------------

from pyasic.miners.makes import WhatsMinerMake


class M31SEV10(WhatsMinerMake):
    raw_model = "M31SE V10"
    expected_chips = 82
    expected_fans = 2


class M31SEV20(WhatsMinerMake):
    raw_model = "M31SE V20"
    expected_chips = 78
    expected_fans = 2


class M31SEV30(WhatsMinerMake):
    raw_model = "M31SE V30"
    expected_chips = 78
    expected_fans = 2