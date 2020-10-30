class FooBarQix:
    def __init__(self, digit_map):
        self.digit_map = digit_map

    def _handle_divisors(self, number: int) -> list:
        return [v for k, v in self.digit_map.items() if number % k == 0]

    def _handle_contains(self, number: int) -> list:
        return [self.digit_map.get(int(d), "") for d in str(number)]

    def generate(self, number: int) -> str:
        result_divisors = ''.join(self._handle_divisors(number))
        result_contains = ''.join(self._handle_contains(number))
        return result_divisors + result_contains or str(number)
