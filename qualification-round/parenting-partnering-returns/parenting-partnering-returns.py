# Solution to first qualification problem, "Parenting Partnering Returns".
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020bdf9

from sys import stdin, argv

DEBUG_ENABLED = "-d" in argv


def debug(msg):
    if DEBUG_ENABLED:
        print("Debug: {}".format(msg))


def could_do_task(task_list, this_task) -> bool:
    """Could the parm person still do the task defined by its parm start and end times?"""
    can_do_it = True
    (task_start, task_end) = this_task

    for (test_start, test_end) in task_list:

        for minute in range(0, 1441):
            if (task_start <= minute <= task_end) and (test_start <= minute <= test_end)\
                    and task_end != test_start\
                    and test_end != task_start:
                can_do_it = False


        # if ((task_start == test_start and task_end == test_end)
        #     or (test_start < task_end < test_end)
        #         or (test_start < task_start < test_end)
        #         or (task_start < test_end < task_end)
        #         or (task_start < test_start < task_end)):
        #     can_do_it = False


    return can_do_it


num_cases = int(stdin.readline())

for case in range(1, num_cases + 1):
    num_activities = int(stdin.readline())
    debug('num_activities = ' + str(num_activities))

    # Make a list of the activities. [(start time, end time)].
    activities = []
    for each_activity in range(1, num_activities + 1):
        this_activity = list(stdin.readline().split(' '))
        activities.append((int(this_activity[0]), int(this_activity[1])))

    possible = True
    solution = ''
    c = []
    j = []

    for task in activities:
        if could_do_task(c, task):                      # Could C do it?
            c.append(task)
            solution += 'C'
        elif could_do_task(j, task):                    # Could J do it?
            j.append(task)
            solution += 'J'
        else:
            possible = False

    if not possible:
        print('Case #{}: IMPOSSIBLE'.format(case))
    else:
        print('Case #{}: {}'.format(case, solution))
