# Solution to first qualification problem, "Indicium".
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209aa0

from sys import stdin, argv
from random import shuffle, choice

DEBUG_ENABLED = "-d" in argv


def debug(msg):
    if DEBUG_ENABLED:
        print("Debug: {}".format(msg))


def no_repeat_column(test_matrix, test_n: int) -> bool:
    test_passed = True
    for col in range(1, test_n + 1):
        col_set = set()
        for row in range(1, test_n + 1):
            col_set.add(test_matrix[col, row])

        if len(col_set) != test_n:
            test_passed = False
    return test_passed


def calc_trace(test_matrix, test_n: int) -> int:
    trace = 0
    for p in range(1, test_n + 1):
        trace += test_matrix[p, p]
    return trace


num_cases = int(stdin.readline())

for case in range(1, num_cases + 1):
    line_list = list(stdin.readline().split(' '))
    n = int(line_list[0])
    k = int(line_list[1])

    debug('n = {}'.format(n))
    debug('k = {}'.format(k))

    attempts_left = 10
    found_k = False
    matrix = {}

    while not found_k and attempts_left >= 0:

        # Make a random matrix.
        valid_matrix = False
        while not valid_matrix:
            matrix = {}                                 # Key=(x, y), Value=Number in that location.

            num_list = []
            for a in range(1, n + 1):
                for b in range(1, n + 1):
                    num_list.append(b)

            shuffle(num_list)
  #          print(num_list)

            still_possible = True
            while still_possible and len(num_list) > 0:

                this_num = num_list.pop()
 #               print(this_num)

                # Figure out all of the places this number could be put.
                possible_positions = []
                for y in range(1, n + 1):
                    for x in range(1, n + 1):
                        possible = True
                        if (x, y) not in matrix:
                            for dd in range(1, n + 1):
                                if (dd, y) in  matrix:
                                    if matrix[dd, y] == this_num:
                                        possible = False
                                if (x, dd) in  matrix:
                                    if matrix[x, dd] == this_num:
                                        possible = False
                        else:
                            possible = False
                        if possible:
                            possible_positions.append((x, y))
#                print(possible_positions)
                if len(possible_positions) == 0:
                    still_possible = False

                if still_possible:
                    this_pos = choice(possible_positions)

                    matrix[this_pos] = this_num

            if still_possible:
                valid_matrix = True

        if k == calc_trace(matrix, n):
            found_k = True
        attempts_left -= 1

    if not found_k:
        print('Case #{}: IMPOSSIBLE'.format(case))
    else:
        print('Case #{}: POSSIBLE'.format(case))
        for row in range(1, n + 1):
            for col in range(1, n + 1):
                print(matrix[col, row], ' ', end='')
            print()