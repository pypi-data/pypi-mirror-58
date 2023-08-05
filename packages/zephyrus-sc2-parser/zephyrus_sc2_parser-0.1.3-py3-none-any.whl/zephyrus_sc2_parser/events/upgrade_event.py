from zephyrus_sc2_parser.events.base_event import BaseEvent
from zephyrus_sc2_parser.gamedata.upgrade_data import upgrades


class UpgradeEvent(BaseEvent):
    @classmethod
    async def create(cls, *args):
        await super().create(*args)

    async def parse_event(self):
        player = self.player
        event = self.event

        if event['m_upgradeTypeName'].decode('utf-8') in upgrades[player.race]:
            player.upgrades.append(event['m_upgradeTypeName'].decode('utf-8'))
