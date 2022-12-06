import logging
from libprobe.asset import Asset
from libprobe.exceptions import CheckException


async def check_vmware(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:
    address = config.get('address')
    if not address:
        address = asset.name

    ...