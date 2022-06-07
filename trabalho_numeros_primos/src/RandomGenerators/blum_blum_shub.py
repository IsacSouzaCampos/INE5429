
from src.PrimarityCheckers.miller_rabin import MillerRabin
import time

Prime1 = 100000007
Prime2 = 100000213


class BlumBlumShub:
    def __init__(self, seed: int = -1, size: int = -1, p: int = Prime1, q: int = Prime2):
        self.seed = seed
        self.size = size
        self.p = p
        self.q = q
        self.m = p * q
        self.time = 0

    def generate(self) -> str:
        """Generates random numbers based on Blum Blum Shub algorithm"""
        if (self.seed == -1) or (self.size == -1):
            raise Exception('Defina um valor para \'seed\' e \'size\'')

        start = time.perf_counter_ns()

        for i in [self.p, self.q]:
            if not MillerRabin(i).is_prime():
                print('Os valores \'p\' e \'q\' devem ser ambos primos!')
                return ''

        current = self.seed
        result = '1'
        for _ in range(self.size - 1):
            current = (current * current) % self.m
            result += str(current % 2)

        stop = time.perf_counter_ns()
        self.time = (stop - start)

        return result


if __name__ == '__main__':
    # start = time.time()
    # for _ in range(100):
    #     _result = BlumBlumShub(int(time.time()), 2048).generate()
    # stop = time.time()
    # print('Runtime =', stop - start)

    _result = BlumBlumShub(int(time.time()), 1024).generate()
    print(_result)
