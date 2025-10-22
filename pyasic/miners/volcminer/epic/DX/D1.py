from pyasic.device.algorithm.hashrate.unit.scrypt import ScryptUnit
from pyasic.device.algorithm.scrypt import ScryptHashRate
from pyasic.miners.backends import ePIC
from pyasic.miners.device.models import D1


class ePICVolcMinerD1(ePIC, D1):
    sticker_hashrate = ScryptHashRate(rate=15.15, unit=ScryptUnit.GH)
