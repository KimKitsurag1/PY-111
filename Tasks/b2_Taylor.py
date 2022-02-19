"""
Taylor series
"""
from typing import Union


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    sum_ = 1 + x
    elem = x
    for i in range(2, 10):
        elem = (elem * x) / i
        sum_ += elem

    print(x)
    return sum_


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    sum_ = x
    elem = x
    signum = -1
    for i in range(3, 30,2):
        elem = (elem*x*x)/(i*(i-1))*(signum)
        sum_ += elem
    print(x)
    return sum_
