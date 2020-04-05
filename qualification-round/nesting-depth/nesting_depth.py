# Solution to first qualification problem, "Nesting Depth".
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9f

from sys import stdin, argv

DEBUG_ENABLED = "-d" in argv


def debug(msg):
    if DEBUG_ENABLED:
        print("Debug: {}".format(msg))


num_cases = int(stdin.readline())
debug('num_cases = ' + str(num_cases))


for case in range(1, num_cases + 1):
    debug('case = ' + str(case))

    s = stdin.readline().strip()
    debug('s = ' + str(s))

    # Make a list of digits and their consecutive occurrences.
    digits = []
    previous_digit = 'x'                                # Ensures first digit checked will be different from previous.
    run_of_same = 0                                     # Home many consecutive digits int his run of same digits?
    for this_digit in s:
        if this_digit == previous_digit:                # Start of a new run.
            run_of_same += 1
        else:
            if previous_digit != 'x':                   # Was there a previous run?
                digits.append((int(previous_digit), run_of_same))    # If so, add it to the list.

            run_of_same = 1                             # Start the new run.
            previous_digit = this_digit

    # Add the last run to the list.
    digits.append((int(previous_digit), run_of_same))
    debug('digits.append(({}, {}))'.format(previous_digit, run_of_same))

    # Parse each list of digits, producing output string.
    current_depth = 0                                   # Current parenthesis depth.
    output = ''
    for (digit, run_of_same) in digits:
        debug('(digit, run_of_same) = ({}, {})'.format(digit, run_of_same))

        delta = digit - current_depth
        debug('delta = {}'.format(delta))
        current_depth = digit

        if delta > 0:
            output = output + '(' * delta
        if delta < 0:
            output = output + ')' * abs(delta)
        output = output + str(digit) * run_of_same

    # Finally, close any remaining open brackets.
    debug('current_depth = {}'.format(current_depth))
    if current_depth > 0:
        output = output + ')' * current_depth

    print("Case #{}: {}".format(case, output))
