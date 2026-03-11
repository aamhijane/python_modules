from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets if available_targets else ["Enemy Player"]

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        sorted_hand = sorted(hand, key=lambda c: c.cost)
        available_mana = 10
        cards_played = []
        mana_used = 0
        damage_dealt = 0

        for card in sorted_hand:
            if card.is_playable(available_mana - mana_used):
                game_state = {"available_mana": available_mana - mana_used}
                card.play(game_state)
                cards_played.append(card.name)
                mana_used += card.cost
                damage_dealt += card.cost

        targets = self.prioritize_targets(battlefield)

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets,
            "damage_dealt": damage_dealt,
        }
