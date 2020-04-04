# Solution to first qualification problem, "Vestigium".
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020993c

from sys import stdin, argv

DEBUG_ENABLED = "-d" in argv


def debug(msg):
    if DEBUG_ENABLED:
        print("Debug: {}".format(msg))


num_cases = int(stdin.readline())
debug('num_cases = ' + str(num_cases))


for case in range(1, num_cases + 1):
    debug('case = ' + str(case))

    size = int(stdin.readline())
    debug('size = ' + str(size))

    # Read matrix values into a dictionary.
    matrix = {}                                 # Key=(x, y), Value=Number in that location.
    for row in range(1, size + 1):
        debug('row = {}'.format(row))

        line = stdin.readline().strip()
        debug('line = {}'.format(line))

        column = 1
        for number in line.split():
            matrix[(column, row)] = int(number)
            debug('matrix[({}, {})] = {}'.format(column, row, number))

            column += 1

    # Analyse the matrix.
    k, r, c = 0, 0, 0
    for alpha in range(1, size + 1):

        this_row = set()
        this_col = set()

        for beta in range(1, size + 1):
            if alpha == beta:           # On a diagonal.
                k += matrix[(alpha, beta)]

            this_row.add(matrix[(beta, alpha)])
            this_col.add(matrix[(alpha, beta)])

        if len(this_col) != size:
            c += 1

        if len(this_row) != size:
            r += 1

    print("Case #{}: {} {} {}".format(case, k, r, c))
