from Bowling.bowling import Game
from typing import List
import pytest

class TestBowling:

    def rolls(self, pins: List[int]):
        game = Game()
        for pin in pins:
            game.roll(pin)
        return game

    def test_score_should_return_0_when_all_missed(self):
        assert self.rolls([0] * 20).score() == 0

    def test_score_should_return_total_number_of_pins_knocked(self):
        assert self.rolls([1] * 20).score() == 20

    def test_roll_should_raise_error_when_more_than_10_pins_knocked(self):
        with pytest.raises(ValueError):
            self.rolls([11])

    def test_roll_should_raise_error_when_10_frames_exceeded(self):
        with pytest.raises(ValueError):
            self.rolls([0] * 21)

    def test_roll_should_raise_error_when_a_frame_exceeds_10(self):
        with pytest.raises(ValueError):
            self.rolls([2, 9])

    def test_roll_three_times_when_spare_is_done_on_tenth_frame(self):
        assert self.rolls([0] * 18 + [1, 9, 0])

    def test_roll_three_times_when_strike_is_done_on_tenth_frame(self):
        assert self.rolls([0] * 18 + [10, 0, 0])
