LIST_SCORES = ["Love", "Fifteen", "Thirty", "Forty"]


class TennisGame(object):
    def __init__(self):
        self.scores = {
            "player1": 0,
            "player2": 0,
        }

    def get_score(self):
        diff = abs(int.__sub__(*self.scores.values()))
        advantage = max(self.scores, key=self.scores.get)
        if all(score >= 3 for score in self.scores.values()):
            if diff == 0:
                return "Deuce"
            elif diff == 1:
                return f"Advantage {advantage}"
            else:
                return f"Win for {advantage}"
        if self.scores[advantage] == 4:
            return f"Win for {advantage}"
        return " - ".join(LIST_SCORES[score] for score in self.scores.values())

    def won_point(self, player_name):
        self.scores[player_name] += 1


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

