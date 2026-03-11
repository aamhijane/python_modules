from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:

    def __init__(self) -> None:
        self._factory: CardFactory | None = None
        self._strategy: GameStrategy | None = None
        self._turns_simulated: int = 0
        self._total_damage: int = 0
        self._cards_created: int = 0
        self._hand: list = []

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self._factory = factory
        self._strategy = strategy
        deck = factory.create_themed_deck(3)
        self._hand = (
            deck["creatures"] + deck["spells"] + deck["artifacts"]
        )
        self._cards_created = len(self._hand)

    def simulate_turn(self) -> dict:
        if not self._factory or not self._strategy:
            raise RuntimeError(
                "Engine not configured. Call configure_engine first.")

        battlefield = ["Enemy Player"]
        result = self._strategy.execute_turn(self._hand, battlefield)

        self._turns_simulated += 1
        self._total_damage += result.get("damage_dealt", 0)

        return {
            "strategy": self._strategy.get_strategy_name(),
            "actions": result,
        }

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self._turns_simulated,
            "strategy_used": (
                self._strategy.get_strategy_name() if self._strategy else None
            ),
            "total_damage": self._total_damage,
            "cards_created": self._cards_created,
        }
