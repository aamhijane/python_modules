from ex0.Card import Card, CardType
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
        base_rating: int = 1200,
    ) -> None:
        Card.__init__(self, name, cost, rarity)
        self.attack_power = attack
        self.health = health
        self.rating = base_rating
        self.wins = 0
        self.losses = 0
        self.type = CardType.TOURNAMENT.value

    # --- Card methods ---
    def play(self, game_state: dict) -> dict:
        available_mana = game_state.get("available_mana", 0)
        if not self.is_playable(available_mana):
            return {"error": f"Not enough mana to play {self.name}"}
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament card entered the battlefield",
        }

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.type,
            "attack": self.attack_power,
            "health": self.health,
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost

    # --- Combatable methods ---
    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target.name if hasattr(target, "name") else target,
            "damage": self.attack_power,
            "combat_type": "tournament",
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(self.health, incoming_damage)
        taken = incoming_damage - blocked
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict:
        return {
            "name": self.name,
            "attack": self.attack_power,
            "health": self.health,
        }

    # --- Rankable methods ---
    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += 16

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= 16

    def get_rank_info(self) -> dict:
        return {
            "name": self.name,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses,
            "record": f"{self.wins}-{self.losses}",
        }

    def get_tournament_stats(self) -> dict:
        return {
            **self.get_card_info(),
            **self.get_rank_info(),
        }
