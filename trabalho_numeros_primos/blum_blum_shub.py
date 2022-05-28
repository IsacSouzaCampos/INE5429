
def blum_blum_shub() -> list:
    """Blum-Blum-Shub algorithm"""
    p = int(input('p = '))
    q = int(input('q = '))
    seed = int(input('seed = '))
    _size = int(input('Quantidade de valores a retornar: '))

    for i in [p, q]:
        if not is_prime(i):
            print('Os valores \'p\' e \'q\' devem ser ambos primos!')
            return []

    n = p * q
    if gcd_euclides(n, seed) != 1:
        print('O MDC entre \'n\' (\'p\' * \'q\') e o \'seed\' deve ser 1!')
        return []

    current = seed
    lst = [current]
    for _ in range(_size - 1):
        current = (current * current) % n
        lst.append(current)

    return lst


def gcd_euclides(n1: int, n2: int) -> int:
    """Euclides algorithm for GCD (greatest common divisor)"""
    if n2 > n1:
        n1, n2 = swap(n1, n2)

    remainder = n1 % n2
    while remainder != 0:
        n1 = n2
        n2 = remainder
        remainder = n1 % n2

    return n2


def swap(n1: int, n2: int) -> tuple:
    """Swaps integers"""
    return n2, n1


def is_prime(n: int) -> bool:
    """Check if a number is a prime number"""
    if n in [1, 2]:
        return True
    if (n % 2) == 0:
        return False
    for i in range(3, (n - 1), 2):
        if (n % i) == 0:
            return False
    return True


if __name__ == '__main__':
    result = blum_blum_shub()
    print('Resultado = ' + str(result))
