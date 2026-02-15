import time
import random
from typing import Generator


def game_event_generator(count: int) -> Generator[dict, None, None]:
    """Generates a stream of random game events."""

    players = ["alice", "bob", "charlie", "david", "eve"]
    actions = [
        "killed monster", "found treasure", "leveled up", "joined party"]

    for i in range(1, count + 1):
        event = {
            "id": i,
            "player": random.choice(players),
            "level": random.randint(1, 20),
            "action": random.choice(actions)
        }
        yield event


def fibonacci_gen(n: int) -> Generator[int, None, None]:
    """
    Generates the first n numbers of the Fibonacci sequence.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def is_prime(num: int) -> bool:
    """Helper to check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_gen(n: int) -> Generator[int, None, None]:
    """
    Generates the first n prime numbers.
    """
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1


def main() -> None:
    """Main execution function for the Stream Wizard."""
    print("=== Game Data Stream Processor ===")
    num_events = 1000
    print(f"Processing {num_events} game events...")

    start_time = time.time()

    # Statistics counters
    total_events = 0
    high_level_players = 0
    treasure_events = 0
    levelup_events = 0

    for event in game_event_generator(num_events):
        total_events += 1

        if total_events <= 3:
            print(f"Event {event['id']}: Player {event['player']} "
                  f"(level {event['level']}) {event['action']}")
        elif total_events == 4:
            print("...")

        # Process analytics
        if event['level'] >= 10:
            high_level_players += 1
        if event['action'] == "found treasure":
            treasure_events += 1
        if event['action'] == "leveled up":
            levelup_events += 1

    end_time = time.time()

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {levelup_events}")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {end_time - start_time:.3f} seconds")

    print("\n=== Generator Demonstration ===")

    fib_list = [str(x) for x in fibonacci_gen(10)]
    print(f"Fibonacci sequence (first 10): {', '.join(fib_list)}")

    prime_list = [str(x) for x in prime_gen(5)]
    print(f"Prime numbers (first 5): {', '.join(prime_list)}")


if __name__ == "__main__":
    main()
