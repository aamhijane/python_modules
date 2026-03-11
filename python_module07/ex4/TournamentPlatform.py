from ex4.TournamentCard import TournamentCard


class TournamentPlatform:

    def __init__(self) -> None:
        self._cards: dict[str, TournamentCard] = {}
        self._matches: list[dict] = []

    def register_card(self, card: TournamentCard) -> str:
        split_name = card.name.lower().split(" ")
        card_id = split_name[0] + "_001"
        if len(split_name) > 1:
            card_id = split_name[-1] + "_001"
        self._cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self._cards.get(card1_id)
        card2 = self._cards.get(card2_id)

        if not card1 or not card2:
            return {"error": "One or both cards not found"}

        if card1.attack_power >= card2.attack_power:
            winner, loser = card1, card2
        else:
            winner, loser = card2, card1

        winner.update_wins(1)
        loser.update_losses(1)

        result = {
            "winner": self._get_id(winner),
            "loser": self._get_id(loser),
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }
        self._matches.append(result)
        return result

    def _get_id(self, card: TournamentCard) -> str:
        for card_id, c in self._cards.items():
            if c is card:
                return card_id
        return "unknown"

    def get_leaderboard(self) -> list:
        sorted_cards = sorted(
            self._cards.items(),
            key=lambda x: x[1].calculate_rating(),
            reverse=True,
        )
        leaderboard = []
        for rank, (card_id, card) in enumerate(sorted_cards, start=1):
            leaderboard.append({
                "rank": rank,
                "name": card.name,
                "rating": card.calculate_rating(),
                "record": f"{card.wins}-{card.losses}",
            })
        return leaderboard

    def generate_tournament_report(self) -> dict:
        total_cards = len(self._cards)
        matches_played = len(self._matches)
        total_rating = sum(c.calculate_rating() for c in self._cards.values())
        avg_rating = total_rating // total_cards if total_cards > 0 else 0
        return {
            "total_cards": total_cards,
            "matches_played": matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active",
        }
