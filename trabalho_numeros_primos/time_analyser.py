import random
import time
import csv

from src.RandomGenerators.blum_blum_shub import BlumBlumShub as BBS
from src.RandomGenerators.linear_congruential_generator import LinearCongruentialGenerator as LCG
from src.PrimarityCheckers.miller_rabin import MillerRabin as MR

SIZES = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]


def main():
    # Generate random binaries of each size using BBS
    bbs = BBS()
    with open('bbs_runtimes.csv', 'w', newline='') as csv_runtimes, \
            open('bbs_binaries.csv', 'w', newline='') as csv_binaries:
        csvwriter_runtimes = csv.writer(csv_runtimes)
        csvwriter_binaries = csv.writer(csv_binaries)

        csvwriter_runtimes.writerow(['SIZE', 'RUNTIME'])
        csvwriter_binaries.writerow(['SIZE', 'RESULT'])
        for size in SIZES:
            runtime = 0
            bbs.size = size

            # for _ in range(10):
            bbs.seed = int(time.time())
            result = bbs.generate()
            runtime += bbs.time

            csvwriter_runtimes.writerow([size, runtime])
            csvwriter_binaries.writerow([size, result])
            print(size, 'bits:', runtime)
            time.sleep(random.randint(1, 5))  # so the seed won't be the same as the previous

    # Generate random binaries of each size using LCG
    lcg = LCG()
    with open('lcg_runtimes.csv', 'w', newline='') as csv_runtimes, \
            open('lcg_binaries.csv', 'w', newline='') as csv_binaries:
        csvwriter_runtimes = csv.writer(csv_runtimes)
        csvwriter_binaries = csv.writer(csv_binaries)

        csvwriter_runtimes.writerow(['SIZE', 'RUNTIME'])
        csvwriter_binaries.writerow(['SIZE', 'RESULT'])
        for size in SIZES:
            runtime = 0
            lcg.size = size

            # for _ in range(10):
            lcg.seed = int(time.time())
            result = lcg.generate()
            runtime += lcg.time

            csvwriter_runtimes.writerow([size, runtime])
            csvwriter_binaries.writerow([size, result])
            print(size, 'bits:', runtime)
            time.sleep(random.randint(1, 5))  # so the seed won't be the same as the previous

    mr = MR()
    with open('bbs_binaries.csv', 'r') as csvinput, open('miller_rabin_runtimes.csv', 'w', newline='') as csv_runtimes:
        csvwriter = csv.writer(csv_runtimes)

        csvwriter.writerow(['SIZE', 'RESULT', 'RUNTIME'])
        lines = csvinput.readlines()
        for line in lines[1:]:
            binary = line.split(',')[1].strip()
            print('size:', len(binary))
            mr.n = int(binary, 2)
            result = mr.is_prime()
            csvwriter.writerow([len(binary), result, mr.time])


if __name__ == '__main__':
    main()
