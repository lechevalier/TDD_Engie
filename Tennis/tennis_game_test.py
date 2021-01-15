from dataclasses import dataclass


@dataclass
class Player(object):
    name: str
    points: int = 0

    def __lt__(self, other):
        return self.points < other.points

    def won_point(self) -> None:
        self.points += 1


class TennisGame(object):
    LIST_SCORES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self):
        self.player1 = Player("player1")
        self.player2 = Player("player2")

    def get_player(self, name: str) -> Player:
        return self.player1 if self.player1.name == name else self.player2

    def get_regular_score(self) -> str:
        score1 = self.LIST_SCORES[self.player1.points]
        score2 = self.LIST_SCORES[self.player2.points]
        return f"{score1} - {score2}"

    def all_opponent_cases(self):
        return [(self.player1, self.player2), (self.player2, self.player1)]

    def get_score(self):
        for (winner, loser) in self.all_opponent_cases():

            diff = winner.points - loser.points

            if winner.points >= 3 and loser.points >= 3:
                if diff == 0:
                    return "Deuce"
                elif diff == 1:
                    return f"Advantage {winner.name}"
                else:
                    return f"Win for {winner.name}"
            if winner.points == 4:
                return f"Win for {winner.name}"

        return self.get_regular_score()

    def won_point(self, player_name):
        self.get_player(player_name).won_point()


class TestTennisGame:
    def test_get_score_should_return_love_love_when_game_not_started(self):
        game = TennisGame()
        assert game.get_score() == "Love - Love"

    def test_get_score_should_return_fifteen_love_when_player1_scored_once(self):
        game = TennisGame()
        game.won_point("player1")
        assert game.get_score() == "Fifteen - Love"

    def test_get_score_should_return_love_fifteen_when_player2_scored_once(self):
        game = TennisGame()
        game.won_point("player2")
        assert game.get_score() == "Love - Fifteen"

    def test_get_score_should_return_thirty_love_when_player1_scored_twice(self):
        game = TennisGame()
        game.won_point("player1")
        game.won_point("player1")
        assert game.get_score() == "Thirty - Love"

    def test_get_score_should_return_deuce_when_player1_and_player2_scored_three_times_both(self):
        game = TennisGame()
        game.won_point("player1")
        game.won_point("player1")
        game.won_point("player1")
        game.won_point("player2")
        game.won_point("player2")
        game.won_point("player2")
        assert game.get_score() == "Deuce"

    def test_get_score_should_return_advantage_player1_when_player1_scores_a_point_after_deuce(self):
        game = TennisGame()
        game.won_point("player1")
        game.won_point("player1")
        game.won_point("player1")
        game.won_point("player2")
        game.won_point("player2")
        game.won_point("player2")
        game.won_point("player1")
        assert game.get_score() == "Advantage player1"

    def test_get_score_should_return_win_player1_when_player1_scores_four_points(self):
        game = TennisGame()
        game.won_point("player1")
        game.won_point("player1")
        game.won_point("player1")
        game.won_point("player1")
        assert game.get_score() == "Win for player1"

    def test_get_score_should_return_win_player2_when_player2_scores_four_points(self):
        game = TennisGame()
        game.won_point("player2")
        game.won_point("player2")
        game.won_point("player2")
        game.won_point("player2")
        assert game.get_score() == "Win for player2"

    def test_get_score_should_return_advantage_player1_when_player1_scores_two_points_after_deuce(self):
        game = TennisGame()
        game.won_point("player1")
        game.won_point("player1")
        game.won_point("player1")
        game.won_point("player2")
        game.won_point("player2")
        game.won_point("player2")
        game.won_point("player1")
        game.won_point("player1")
        assert game.get_score() == "Win for player1"

