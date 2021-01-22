from typing import List


class Game:
    def __init__(self):
        self.frames: List[List[int]] = []

    def roll(self, pins: int):
        if len(self.frames) == 10 and len(self.frames[-1]) == 2:
            raise ValueError
        if pins > 10:
            raise ValueError

        if self.frames and len(self.frames[-1]) == 1:
            if self.frames[-1][0] + pins <= 10:
                self.frames[-1].append(pins)
            else:
                raise ValueError
        else:
            self.frames.append([pins])

    def score(self) -> int:
        return sum(sum(frame) for frame in self.frames)
