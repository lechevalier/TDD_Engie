from typing import List


class Frame:
    def __init__(self):
        self.balls = []

    def roll(self, pins) -> None:
        if pins > 10:
            raise ValueError

        self.balls.append(pins)
        if self.knocked_pins > 10:
            raise ValueError

    @property
    def knocked_pins(self) -> int:
        return sum(self.balls)

    def is_strike(self) -> bool:
        return self.knocked_pins == 10 and len(self.balls) == 1

    def is_spare(self) -> bool:
        return self.knocked_pins == 10 and len(self.balls) == 2

    def is_complete(self) -> bool:
        return self.is_strike() or len(self.balls) == 2


class BonusFrame(Frame):
    def is_complete(self) -> bool:
        if not self.is_spare() and not self.is_strike():
            return super().is_complete()
        return len(self.balls) == 3


class Game:
    def __init__(self):
        self.frames: List[Frame] = [Frame()]

    def is_complete(self) -> bool:
        return len(self.frames) == 10 and self.frames[-1].is_complete()

    def roll(self, pins: int):
        if self.is_complete():
            raise ValueError

        if self.frames[-1].is_complete():
            new_frame = Frame() if len(self.frames) < 9 else BonusFrame()
            self.frames.append(new_frame)

        self.frames[-1].roll(pins)

    def score(self) -> int:
        return sum(frame.knocked_pins for frame in self.frames)
