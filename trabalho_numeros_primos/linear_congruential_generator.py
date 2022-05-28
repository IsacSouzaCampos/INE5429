
def linear_congruential_generator() -> list:
    """Linear Congruential Generator algorithm"""
    a = int(input('a = '))
    b = int(input('b = '))
    m = int(input('m = '))
    seed = int(input('seed = '))
    _size = int(input('Quantidade de valores a retornar: '))

    current = seed
    lst = [current]
    for _ in range(_size):
        current = ((a * current) + b) % m
        lst.append(current)

    return lst


if __name__ == '__main__':
    result = linear_congruential_generator()
    print('Resultado = ' + str(result))
