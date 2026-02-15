
class Player:
    """Player with achievement collections."""

    def __init__(self, name: str, achievements: set) -> None:
        """Initialize name and achievements of a player."""
        self.name: str = name
        self.achievements: set = achievements

    def __str__(self):
        """Represent player acheivements as a string format."""
        return f"Player {self.name} achievements: {self.achievements}"


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice = {
        'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {
        'level_10', 'treasure_hunter', 'boss_slayer',
        'speed_demon', 'perfectionist'}

    alice_unique = alice.difference(bob, charlie)
    bob_unique = bob.difference(alice, charlie)
    charlie_unique = charlie.difference(bob, alice)

    players = [
        Player("alice", alice),
        Player("bob", bob),
        Player("charlie", charlie)
    ]
    for player in players:
        print(player)

    all_unique = alice.union(bob, charlie)
    print("\n=== Achievement Analytics ===")
    print(f"All unique achievements: {all_unique}")
    print(f"Total unique achievements: {len(all_unique)}\n")

    common = alice.intersection(bob, charlie)
    rare = alice_unique.union(bob_unique, charlie_unique)
    print(f"Common to all players: {common}")
    print(f"Rare achievements (1 player): {rare}\n")

    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")
