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

from pyasic.miners.backends import ePIC
from pyasic.miners.device.models import (
    BlockMiner520i,
    BlockMiner720i,
    BlockMinerELITE1,
    BlockMinerMini,
)


class ePICBlockMiner520i(ePIC, BlockMiner520i):
    pass


class ePICBlockMiner720i(ePIC, BlockMiner720i):
    pass


class ePICBlockMinerELITE1(ePIC, BlockMinerELITE1):
    pass


class ePICBlockMinerMini(ePIC, BlockMinerMini):
    pass
