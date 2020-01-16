def accumulate(lst):
    """
    >>> l = [1, 5, 13, 4]
    >>> accumulate(l)
    23
    >>> l
    [1, 6, 19, 23]
    >>> deep_l = [3, 7, [2, 5, 6], 9]
    >>> accumulate(deep_l)
    32
    >>> deep_l
    [3, 10, [2, 7, 13], 32]
    """

    total = 0
    for ele in lst:
        if type(ele) == list:
            total += accumulate(ele)

        else:
            ele += total
            total = ele

    return total


def make_pingpong_tracker():
    """Return a funtion that returns the next value in the pingpong
     sequence each time it is called.
     >>> output = []
     >>> x = make_pingpong_tracker()
     >>> for _ in  range(9):
     ...   output += [x()]
     >>> output
     [1, 2, 3, 4, 5, 6, 7, 6, 5]
     """

    index, curr, add = 1, 0, True

    def pingpong_tracker():
        nonlocal add, index, curr

        if add:
            curr += 1
        else:
            curr -= 1

        if should_switch(index):
            add = not add
        index += 1

        return curr

    return pingpong_tracker


def should_switch(index):
    string = str(index)
    return index % 7 == 0 or '7' in string
