from ex0.Card import Card, CardTypes


class CreatureCard(Card):
    """Creature card type."""

    def __init__(
            self, name: str, cost: int, rarity: str, attack: int, health: int):
        """Initialization of creature card type variables."""
        super().__init__(name, cost, rarity)
        self.attack: int = attack
        self.health: int = health
        self.type: str = CardTypes.CREATURE.value

    def play(self, game_state: dict) -> dict:
        """
        Logic for playing the card.
        Checks mana availability from game_state and returns the result.
        """
        available_mana = game_state.get('available_mana', 0)
        is_playable = available_mana >= self.cost

        if not is_playable:
            return {
                "card_played": self.name,
                "error": "Insufficient mana",
                "playable": False
            }

        # Logic for successful play
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
        }

    def attack_target(self, target: 'CreatureCard') -> dict:
        """
        Combat logic between this card and a target.
        Applies damage and returns the combat summary.
        """
        # Record damage for the result dictionary
        damage_dealt = self.attack

        # Guard against non-creature targets if necessary (Resilient Design)
        if hasattr(target, 'health'):
            target.health = max(0, target.health - damage_dealt)

        return {
            'attacker': self.name,
            'target': target.name,
            'damage_dealt': damage_dealt,
            'combat_resolved': True
        }

    def get_card_info(self) -> dict:
        base_info: dict = super().get_card_info()

        return base_info | {
            'type': self.type,
            'attack': self.attack,
            'health': self.health
        }
