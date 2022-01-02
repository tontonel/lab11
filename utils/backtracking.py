def initialize():
    """
    init function
    :return:
    """
    return -1


def get_next_elem(solution):
    """
    returns the next element
    :return:
    """
    return solution[-1] + 1


def backtracking(solution, exist, consistent, is_solution, get_next = get_next_elem, init = initialize):
    """
    generate all solution
    :param is_solution:
    :param solution:
    :param init
    :param exist:
    :param consistent:
    :param get_next:
    :return:
    """
    solution.append(init())
    solution[-1] = get_next(solution)
    while exist(solution):
        if consistent(solution):
            if is_solution(solution):
                yield solution[:]
            else:
                yield from backtracking(solution[:], exist, consistent, is_solution, get_next, init)
        solution[-1] = get_next(solution)
