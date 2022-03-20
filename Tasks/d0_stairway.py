from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    i = 2
    sum_prev=0
    sum_prev_prev=0
    sum_prev += stairway[i - 1]
    sum_prev_prev += stairway[i - 2]
    sum_current = stairway[i]+min(sum_prev,sum_prev_prev)
    last_index = len(stairway) - 1
    while i < last_index:
        i+=1
        sum_prev_prev=sum_prev
        sum_prev=sum_current
        sum_current=stairway[i]+min(sum_prev,sum_prev_prev)
    return sum_current

    print(stairway)
    return 0
