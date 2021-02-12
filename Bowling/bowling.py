from typing import List


class BonusStack:
    def __init__(self, bonus_1: int, bonus_2: int):
        self.bonus_1 = bonus_1
        self.bonus_2 = bonus_2

    def increment_after_spare(self):
        self.bonus_1 += 1

    def increment_after_strike(self):
        self.bonus_1 += 1
        self.bonus_2 += 1

    def consume(self, times):
        if times == 2:
            self.bonus_1, self.bonus_2 = 0, 0
        if times == 1:
            self.bonus_1, self.bonus_2 = self.bonus_2, 0

    def to_list(self):
        return self.bonus_1, self.bonus_2


class Frame:
    def __init__(self, bonus_rolls):
        self.balls = []
        self.bonus_rolls = bonus_rolls.to_list()

    def roll(self, pins) -> None:
        if pins > 10:
            raise ValueError

        self.balls.append(pins)
        self.is_complete()

    @property
    def knocked_pins(self) -> int:
        return sum(self.balls)

    @property
    def score(self):
        return self.knocked_pins + sum(ball * bonus for ball, bonus in zip(self.balls, self.bonus_rolls))

    def is_strike(self) -> bool:
        return self.knocked_pins == 10 and len(self.balls) == 1

    def is_spare(self) -> bool:
        return self.knocked_pins == 10 and len(self.balls) == 2

    def is_complete(self) -> bool:
        if self.knocked_pins > 10:
            raise ValueError
        return self.is_strike() or len(self.balls) == 2


class BonusFrame(Frame):
    def is_complete(self) -> bool:
        if sum(self.balls[:2]) < 10:
            return len(self.balls) == 2
        return len(self.balls) == 3


class Game:
    def __init__(self):
        self.bonus_stack = BonusStack(0, 0)
        self.frames: List[Frame] = [Frame(self.bonus_stack)]

    def create_frame(self):
        if self.frames[-1].is_spare():
            self.bonus_stack.increment_after_spare()
        elif self.frames[-1].is_strike():
            self.bonus_stack.increment_after_strike()
        frame_clz = BonusFrame if len(self.frames) == 9 else Frame
        return frame_clz(self.bonus_stack)

    def is_complete(self) -> bool:
        return len(self.frames) == 10 and self.frames[-1].is_complete()

    def roll(self, pins: int):
        if self.is_complete():
            raise ValueError

        if self.frames[-1].is_complete():
            self.bonus_stack.consume(len(self.frames[-1].balls))
            self.frames.append(self.create_frame())

        self.frames[-1].roll(pins)

    def score(self) -> int:
        return sum(frame.score for frame in self.frames)
