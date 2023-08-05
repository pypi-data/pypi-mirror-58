from zephyrus_sc2_parser.events.base_event import BaseEvent


class AbilityEvent(BaseEvent):
    @classmethod
    async def create(cls, summary_stats, *args):
        await super().create(*args)
        self = AbilityEvent()
        self.summary_stats = summary_stats

    async def parse_event(self):
        player = self.player
        event = self.event
        summary_stats = self.summary_stats

        if not player:
            return

        elif self.type == 'NNet.Game.SCmdEvent':
            if event['m_abil']:
                if event['m_abil']['m_abilLink'] and type(event['m_abil']['m_abilCmdIndex']) is int:
                    ability = (
                        event['m_abil']['m_abilLink'],
                        event['m_abil']['m_abilCmdIndex']
                    )
                else:
                    ability = None
                player.active_ability = ability

                if player.active_ability and player.active_ability[0] == 183:
                    summary_stats['inject_count'][player.player_id] += 1
        else:
            if player.active_ability and player.active_ability[0] == 183:
                summary_stats['inject_count'][player.player_id] += 1

        return summary_stats
