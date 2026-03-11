from ex0.Card import Card


class CreatureCard(Card):

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int
    ) -> None:
        super().__init__(name, cost, rarity)
        self.attack: int = attack
        self.health: int = health
        self.type: str = "Creature"

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target: Card) -> dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({
            "type": self.type,
            "attack": self.attack,
            "health": self.health
        })
        return info
