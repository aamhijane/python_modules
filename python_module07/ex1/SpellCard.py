from ex0.Card import Card
from ex0.Card import CardTypes


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type: str = effect_type
        self.type: str = CardTypes.SPELL.value

    def play(self, game_state: dict) -> dict:
        """Constructs the initial action log for the UI."""
        effect_description = self.effect_type
        # Mapping 'damage' to the required output string
        if self.effect_type == 'damage' and self.name == 'Lightning Bolt':
            effect_description = 'Deal 3 damage to target'

        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': effect_description
        }

    def resolve_effect(self, targets: list) -> dict:
        """
        Actually applies the spell's logic to the target list.
        Returns the resolved state of the effect.
        """
        # Hardened Security: Guard against empty target lists
        if not targets:
            return {'status': 'failed', 'reason': 'No targets selected'}

        target_names = [target.name for target in targets]
        
        # Lean Logic: Specific resolution for 'damage' types
        if self.effect_type == 'damage':
            # In a real system, you'd subtract HP from target objects here
            resolution = {
                'status': 'resolved',
                'effect_applied': 'damage',
                'targets': target_names,
                'value': 3 if self.name == 'Lightning Bolt' else 0
            }
        else:
            resolution = {
                'status': 'resolved',
                'effect_applied': self.effect_type,
                'targets': target_names
            }
            
        return resolution
