# Part of solution to first qualification problem, "Indicium".
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209aa0
# This program generates a dictionary of pre-calculated solutions which can be used to solve this problem
# for Test Set 1. It doesn't solve Test Set 2 :(

from sys import argv
from random import shuffle, choice

DEBUG_ENABLED = "-d" in argv


def debug(msg):
    """If program was run with -d argument, send parm string to stdout."""
    if DEBUG_ENABLED:
        print("Debug: {}".format(msg))


def calc_n(this_matrix) -> int:
    """Find out the width / height of a square matrix."""
    (this_n, _) = max(this_matrix)
    return this_n


def calc_trace(this_matrix) -> int:
    """Calculate the trace of a square matrix, which is the sum of the values on the main diagonal
    (which runs from the upper left to the lower right)."""
    trace = 0
    for p in range(1, calc_n(this_matrix) + 1):
        trace += this_matrix[p, p]
    return trace


def print_matrix(this_matrix):
    """Print out a square matrix."""
    this_n = calc_n(this_matrix)
    for row in range(1, this_n + 1):
        for col in range(1, this_n + 1):
            print(this_matrix[col, row], ' ', end='')
        print()


solutions = {}                                      # Key=(n, k}, Value=Dictionary of the matrix.

# Bigger squares have more possible Latin Squares, so need to ramp up number of experiments for them.
# Ramp up factors based on https://oeis.org/A002860
ramp_up = [161280, 576, 12, 2]

for n in range(2, 5 + 1):
    debug('n = {}'.format(n))

    matrix = {}

    if DEBUG_ENABLED:
        num_experiments = 10 * ramp_up.pop()
    else:
        num_experiments = 100 * ramp_up.pop()
    debug('num_experiments = {}'.format(num_experiments))

    for experiments in range(num_experiments):

        still_possible = True

        num_list = []                               # The numbers that will populate the matrix.
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                num_list.append(b)

        shuffle(num_list)                           # We're going to pop numbers out of the list in random order.

        matrix = {}                                 # Key=(x, y), Value=Number in that location.

        # Start by populating the diagonal.
        for diagonal in range(1, n + 1):
            matrix[diagonal, diagonal] = num_list.pop()

        # If we already have a solution for this trace score, then give up on this matrix.
        if (n, calc_trace(matrix)) in solutions:
            still_possible = False

        while still_possible and len(num_list) > 0:
            this_num = num_list.pop()

            # Figure out all of the places this number could be put.
            possible_positions = []
            for y in range(1, n + 1):
                for x in range(1, n + 1):
                    possible = True
                    if (x, y) not in matrix:
                        for dd in range(1, n + 1):
                            if (dd, y) in matrix:
                                if matrix[dd, y] == this_num:
                                    possible = False
                            if (x, dd) in matrix:
                                if matrix[x, dd] == this_num:
                                    possible = False
                    else:
                        possible = False
                    if possible:
                        possible_positions.append((x, y))
            if len(possible_positions) == 0:
                still_possible = False

            if still_possible:
                this_pos = choice(possible_positions)

                matrix[this_pos] = this_num

        if still_possible:
            k = calc_trace(matrix)

            if DEBUG_ENABLED:
                print('k = {}'.format(k))
                print_matrix(matrix)
                print()
            else:
                print('n = {}, experiments = {}'.format(n, experiments))

            solutions[n, k] = matrix
            debug('len(solutions) = {}'.format(len(solutions)))

print(solutions)
