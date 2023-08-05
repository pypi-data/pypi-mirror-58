from zephyrus_sc2_parser.events.base_event import BaseEvent


class PlayerLeaveEvent(BaseEvent):
    @classmethod
    async def create(cls, *args):
        await super().create(*args)

    async def parse_event(self):
        pass
