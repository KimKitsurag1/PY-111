from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    mid_index = 0
    start_index = 0
    end_index = len(arr)

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2

        if elem == arr[mid_index]:
            while mid_index > 0 and arr[mid_index - 1] == elem:
                mid_index = mid_index - 1
            return mid_index

        if elem <= arr[mid_index]:
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1
    print(elem, arr)
    return None
