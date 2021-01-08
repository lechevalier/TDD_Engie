import unittest


LIST_SCORES = ["Love", "Fifteen", "Thirty", "Forty"]


class TennisGame(object):
    def __init__(self):
        self.scores = {
            "player1": 0,
            "player2": 0,
        }

    def get_score(self):
        return " - ".join(LIST_SCORES[score] for score in self.scores.values())

    def won_score(self, player_name):
        self.scores[player_name] += 1


class TestTennisGame(unittest.TestCase):
    def test_get_score_should_return_love_love_when_game_not_started(self):
        game = TennisGame()
        self.assertEqual("Love - Love", game.get_score())

    def test_get_score_should_return_fifteen_love_when_player1_scored_once(self):
        game = TennisGame()
        game.won_score("player1")
        self.assertEqual("Fifteen - Love", game.get_score())

    def test_get_score_should_return_love_fifteen_when_player2_scored_once(self):
        game = TennisGame()
        game.won_score("player2")
        self.assertEqual("Love - Fifteen", game.get_score())

    def test_get_score_should_return_thirty_love_when_player1_scored_twice(self):
        game = TennisGame()
        game.won_score("player1")
        game.won_score("player1")
        self.assertEqual("Thirty - Love", game.get_score())

    def test_get_score_should_return_thirty_love_when_player1_scored_twice(self):
        game = TennisGame()
        game.won_score("player1")
        game.won_score("player1")
        self.assertEqual("Thirty - Love", game.get_score())


if __name__ == '__main__':
    unittest.main()
