import sys


class NoScoreError(Exception):
    pass


class Player:
    def __init__(self) -> None:
        self.scores_list: list = []

    def prepare_scores_list(self):
        tmp_scores: list = sys.argv[1:]
        if not tmp_scores:
            raise NoScoreError("No scores provided.")
        for score in tmp_scores:
            self.scores_list.append(int(score))

    @staticmethod
    def get_total_players(players: list) -> int:
        return len(players)

    @staticmethod
    def get_total_score(scores: list) -> int:
        return sum(scores)

    @staticmethod
    def get_average_score(scores: list) -> int:
        return sum(scores) / len(scores)

    @staticmethod
    def get_high_score(scores: list) -> int:
        return max(scores)

    @staticmethod
    def get_low_score(scores: list) -> int:
        return min(scores)

    @staticmethod
    def get_score_range(scores: list) -> int:
        return max(scores) - min(scores)


if __name__ == "__main__":

    print("=== Player Score Analytics ===")
    player = Player()

    try:
        player.prepare_scores_list()

        scores = player.scores_list
        total_players = player.get_total_players(scores)
        total_score = player.get_total_score(scores)
        average_score = player.get_average_score(scores)
        high_score = player.get_high_score(scores)
        low_score = player.get_low_score(scores)
        score_range = player.get_score_range(scores)

        print(f"Scores processed: {scores}")
        print(f"Total players: {total_players}")
        print(f"Total score: {total_score}")
        print(f"Average score: {average_score}")
        print(f"High score: {high_score}")
        print(f"Low score: {low_score}")
        print(f"Score range: {score_range}")
    except ValueError:
        print("oops, I typed ’banana’ instead of ’1000’")
    except NoScoreError as e:
        print(f"{e} Usage: python3"
              "ft_score_analytics.py <score1> <score2> ...")
