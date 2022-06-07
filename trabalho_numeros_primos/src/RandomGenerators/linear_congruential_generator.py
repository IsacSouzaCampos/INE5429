
from random import Random
import time


class LinearCongruentialGenerator:
    def __init__(self, seed: int = -1, size: int = -1, a: int = 48271,
                 b: int = Random().randint(0, 1000), m: int = 2147483647):
        self.seed = seed
        self.size = size
        self.a = a
        self.b = b
        self.m = m
        self.time = 0

    def generate(self) -> str:
        """Linear Congruential Generator algorithm"""
        if (self.seed == -1) or (self.size == -1):
            raise Exception('Defina um valor para \'seed\' e \'size\'')

        start = time.perf_counter_ns()

        current = self.seed
        result = '1'
        for _ in range(self.size):
            current = ((self.a * current) + self.b) % self.m
            result += str(current % 2)

        stop = time.perf_counter_ns()
        self.time = (stop - start)

        return result


if __name__ == '__main__':
    _result = LinearCongruentialGenerator(int(time.time()), 1024).generate()
    print('Resultado =', str(_result), '\n', int(_result, 2))
