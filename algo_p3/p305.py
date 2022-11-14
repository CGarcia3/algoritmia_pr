import numpy as np
import itertools

from typing import List, Tuple, Dict, Callable, Iterable, Union


def split(t: np.ndarray) -> Tuple[np.ndarray, int, np.ndarray]:
    """
    Splits a given array into two arrays each containing
    the smaller and bigger values in regard to the first element
    of the array.

    **Params:** array (The array to split)

    **Return:** Tuple(array, int, array) (The two arrays that result
    after the split, and the value used to split the array)
    """

    if (t is None):
        print("Array is empty")
        return None

    p = t[0]
    arr_left = [u for u in t if u < p]
    arr_right = [u for u in t if u > p]

    return (arr_left, p, arr_right)


def qsel(t: np.ndarray, k: int) -> Union[int, None]:
    """
    Recursive function that finds the k-th element of the
    given array if it was ordered.

    **Params:** array, int (The array containing the values,
    and the k index)

    **Return:** int (element in the k-th position)
    """

    if (k < 0 or t is None):
        print("K is smaller than 0 or array is empty")
        return None

    if len(t) == 1:
        return t[0]

    arr_left, p, arr_right = split(t)
    m = len(arr_left)

    if k == m:
        return p
    elif k < m:
        return qsel(arr_left, k)
    elif k > m:
        return qsel(arr_right, k-m-1)


def qsel_nr(t: np.ndarray, k: int) -> Union[int, None]:
    """
    Implementation of the qsel function without the tail
    recursion.

    **Params:** array, int (The array containing the values,
    and the k index)

    **Return:** int (element in the k-th position)
    """

    if (k < 0 or t is None):
        print("K is smaller than 0 or array is empty")
        return None

    if len(t) == 1:
        return t[0]
    else:
        arr_left, p, arr_right = split(t)
        m = len(arr_left)

        if k == m:
            ret = p
        elif k < m:
            ret = qsel_nr(arr_left, k)
        elif k > m:
            ret = qsel_nr(arr_right, k-m-1)

    return ret


def split_pivot(t: np.ndarray, mid: int) -> Tuple[np.ndarray, int, np.ndarray]:
    pass


def pivot5(t: np.ndarray) -> int:
    pass


def qsel5_nr(t: np.ndarray, k: int) -> Union[int, None]:
    pass


if __name__ == "__main__":
    t = np.array([4, 2, 7, 1, 5, 9])
    k = 2
    li = 4

    a = qsel(t, k)
    b = qsel(t, li)
    c = qsel_nr(t, k)
    d = qsel_nr(t, li)

    print(a, b, c, d)
