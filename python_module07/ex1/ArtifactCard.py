from ex0.Card import Card, CardType


class ArtifactCard(Card):

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        durability: int,
        effect: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self.durability: int = durability
        self.effect: str = effect
        self.type: str = CardType.ARTIFACT.value

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        }

    def activate_ability(self) -> dict:
        if self.durability <= 0:
            return {"error": "Artifact is destroyed!"}
        self.durability -= 1
        return {
            "artifact": self.name,
            "effect": self.effect,
            "durability_remaining": self.durability
        }
