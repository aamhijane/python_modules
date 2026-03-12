from ex0.Card import Card, CardType
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        health: int,
        mana: int
    ) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power: int = attack_power
        self.health: int = health
        self.mana: int = mana
        self.type: str = CardType.ELITE.value

    # Combatable (Abstract Interface)
    def attack(self, target) -> dict:
        return {
            'attacker': self.name,
            'target': target.name,
            'damage': self.attack_power,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_blocked: int = min(self.health, incoming_damage)
        damage_taken: int = incoming_damage - damage_blocked
        return {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': damage_blocked,
            'still_alive': self.health >= damage_taken
        }

    def get_combat_stats(self) -> dict:
        return {
            'attack': self.attack_power,
            'health': self.health
        }

    # Magical (Abstract Interface)
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': self.cost
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {
            'channeled': amount,
            'total_mana': self.mana
        }

    def get_magic_stats(self) -> dict:
        return {
            'mana': self.mana,
            'cost': self.cost
        }

    # EliteCard (Multiple Inheritance: Card + Combatable + Magical)
    def play(self, game_state: dict) -> dict:
        _ = game_state
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card deployed with combat and magic abilities"
        }
