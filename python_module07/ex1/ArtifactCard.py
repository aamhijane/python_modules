from ex0.Card import Card
from ex0.Card import CardTypes


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        # Lean Logic: Specific artifact attributes
        self.durability: int = durability
        self.effect: str = effect
        self.type: str = CardTypes.ARTIFACT.value

    def play(self, game_state: dict) -> dict:
        """
        Executes the logic for placing an artifact on the field.
        """
        # Matches your required output format exactly
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect
        }

    def activate_ability(self) -> dict:
        """
        Triggered when the artifact's special ability is used.
        Decrements durability if applicable (Resilient Design).
        """
        if self.durability <= 0:
            return {'status': 'failed', 'reason': 'Artifact is broken'}

        # Hardened Security: Manage state change internally
        self.durability -= 1
        
        return {
            'status': 'activated',
            'effect': self.effect,
            'remaining_durability': self.durability
        }
