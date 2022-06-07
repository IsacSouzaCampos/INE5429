import random
import sys
import time


class MillerRabin:
    """Miller-Rabin algorithm"""
    def __init__(self, n: int = -1):
        self.n = n
        self.time = 0

    def is_prime(self) -> bool:
        """Is number 'n' a prime?"""
        start = time.perf_counter_ns()

        if self.n == -1:
            self.time = time.perf_counter_ns() - start
            raise Exception('Escolha um numero maior que 0')
        if self.n in [1, 2]:
            return True
        if (self.n % 2) == 0:
            return False

        m, k = self.find_parameters()
        a = random.randint(2, self.n - 2)
        b = (a ** m) % self.n

        if (b == 1) or ((b - self.n) == -1):
            self.time = time.perf_counter_ns() - start
            return True

        for _ in range(k):
            b = (b ** 2) % self.n
            if b == 1:
                self.time = time.perf_counter_ns() - start
                return False
            elif (b - self.n) == -1:
                self.time = time.perf_counter_ns() - start
                return True

        self.time = time.perf_counter_ns() - start
        return False

    def find_parameters(self) -> tuple:
        """Find parameters 'm' and 'k'"""
        m = self.n - 1
        k = 0
        while True:
            temp = m / 2
            if not temp.is_integer():
                break
            m = temp
            k += 1

        return int(m), k


if __name__ == '__main__':
    print(MillerRabin(int(sys.argv[1])).is_prime())
