from typing import List, Dict, Set, Any


def get_high_scorers(data: List[Dict[str, Any]], threshold: int) -> List[str]:
    """
    Uses list comprehension to filter players above a certain score.
    """
    return [player['name'] for player in data if player['score'] > threshold]


def get_doubled_scores(data: List[Dict[str, Any]]) -> List[int]:
    """
    Uses list comprehension to transform every score (doubling it).
    """
    return [player['score'] * 2 for player in data]


def get_player_score_map(data: List[Dict[str, Any]]) -> Dict[str, int]:
    """
    Uses dict comprehension to create a mapping of name: score.
    """
    return {player['name']: player['score'] for player in data}


def get_achievement_counts(data: List[Dict[str, Any]]) -> Dict[str, int]:
    """
    Uses dict comprehension to map player names
    to the count of their achievements.
    """
    return {p['name']: len(p['achievements']) for p in data}


def get_unique_achievements(data: List[Dict[str, Any]]) -> Set[str]:
    """
    Uses set comprehension to find all unique achievements across all players.
    """
    return {ach for player in data for ach in player['achievements']}


def main() -> None:
    """
    Main function demonstrating the power of Python comprehensions.
    """
    # Raw Game Data
    raw_data = [
        {"name": "alice", "score": 2300,
         "achievements": [
             "first_kill", "level_10", "boss_slayer"], "region": "north"},
        {"name": "bob", "score": 1800,
         "achievements": [
             "first_kill", "level_5"], "region": "east"},
        {"name": "charlie", "score": 2150,
         "achievements": [
             "first_kill", "level_10", "collector"], "region": "north"},
        {"name": "diana", "score": 2050,
         "achievements": [
             "boss_slayer", "speedrun"], "region": "central"}
    ]

    print("=== Game Analytics Dashboard ===")

    # --- List Comprehension Examples ---
    print("\n=== List Comprehension Examples ===")
    high_scorers = get_high_scorers(raw_data, 2000)
    doubled = get_doubled_scores(raw_data)
    active_regions_list = [p['region'] for p in raw_data]

    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {doubled}")
    print(f"Region stream: {active_regions_list}")

    # --- Dict Comprehension Examples ---
    print("\n=== Dict Comprehension Examples ===")
    player_scores = get_player_score_map(raw_data)
    ach_counts = get_achievement_counts(raw_data)

    # Categorizing scores: high if > 2000 else medium
    categories = {
            p['name']:
            ("high" if p['score'] > 2000 else "medium") for p in raw_data}

    print(f"Player scores: {player_scores}")
    print(f"Achievement counts: {ach_counts}")
    print(f"Score categories: {categories}")

    # --- Set Comprehension Examples ---
    print("\n=== Set Comprehension Examples ===")
    unique_players = {p['name'] for p in raw_data}
    unique_ach = get_unique_achievements(raw_data)
    active_regions = {p['region'] for p in raw_data}

    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_ach}")
    print(f"Active regions: {active_regions}")

    # --- Combined Analysis ---
    print("\n=== Combined Analysis ===")
    total_players = len(unique_players)
    all_scores = [p['score'] for p in raw_data]
    avg_score = sum(all_scores) / total_players if total_players > 0 else 0

    # Finding top performer (one with max score)
    top_score = max(all_scores)
    top_player = [p['name'] for p in raw_data if p['score'] == top_score][0]

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {len(unique_ach)}")
    print(f"Average score: {avg_score}")
    print(f"Top performer: {top_player} ({top_score} points)")


if __name__ == "__main__":
    main()
