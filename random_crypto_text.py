import math
import random
import sys


# Problem: Generate a "random" cryptographic block consisting of the numbers 0 through 9, using each
# number exactly five times.

def get_random_index(l):
    return math.floor(random.uniform(0, len(l)))


def print_block(l):
    # generate block of result text
    for idx, n in enumerate(l):
        sys.stdout.write(str(n))

        if (idx + 1) % 5 == 0:
            sys.stdout.write("\n")


def generate_crypto_block():
    numbers = []

    # generate list of numbers
    for i in range(0, 10):
        for n in range(0, 5):
            numbers.append(i)

    counter = len(numbers)

    while counter > 0:
        # choose random indices to swap
        idx_to_remove = get_random_index(numbers)
        idx_to_place = get_random_index(numbers)

        # swap the values
        numbers[idx_to_remove], numbers[idx_to_place] = numbers[idx_to_place], numbers[idx_to_remove]

        counter -= 1

    print_block(numbers)


generate_crypto_block()