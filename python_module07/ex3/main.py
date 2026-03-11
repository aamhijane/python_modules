from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:
    print("=== DataDeck Game Engine ===\n")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    print("Configuring Fantasy Card Game...")
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}\n")

    engine.configure_engine(factory, strategy)

    hand_display = [
        f"{c.name} ({c.cost})" for c in engine._hand
    ]
    print("Simulating aggressive turn...")
    format_hand = str(hand_display).replace("'", "")
    print(f"Hand: {format_hand}\n")

    turn_result = engine.simulate_turn()
    print("Turn execution:")
    print(f"Strategy: {turn_result['strategy']}")
    print(f"Actions: {turn_result['actions']}\n")

    report = engine.get_engine_status()
    print(f"Game Report:\n{report}\n")
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
