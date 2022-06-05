"""MillerRabin"""
import sys
import timeit


class MillerRabin:
    """Miller-Rabin algorithm"""
    def __init__(self, n: int):
        self.n = n

    def is_prime(self) -> bool:
        """Is number 'n' a prime?"""
        m, k = self.find_parameters()
        a = 2
        b = (a ** m) % self.n

        if (b == 1) or ((b - self.n) == -1):
            return True

        for _ in range(k):
            b = (b ** 2) % self.n
            if b == 1:
                return False
            elif (b - self.n) == -1:
                return True

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
    num = int(sys.argv[1], 2)
    print(num)

    start = timeit.default_timer()
    print(MillerRabin(num).is_prime())
    stop = timeit.default_timer()

    print('Time: ', stop - start)
