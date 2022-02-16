# flake8: noqa
#The MIT License (MIT)
#Copyright (c) 2022-present hawk_tomy
from typing import Generator


def m(
        left: list[int],
        right: list[int]
    )-> Generator[int]:

    left.reverse()
    right.reverse()

    while left and right:
        if left[-1] < right[-1]:
            yield left.pop()
        else:
            yield right.pop()

    yield from reversed(left)
    yield from reversed(right)


def merge_sort(
        target: list[int]
    )-> list[int]:

    i = len(target) // 2

    if not i:
        return target

    a1 = merge_sort(target[:i])
    a2 = merge_sort(target[i:])
    return list(m(a1,a2))


if __name__ == '__main__':
    import tester

    tester.tester(merge_sort)






















