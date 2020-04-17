def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """

    def function(f=lambda x: x):
        nonlocal n
        n = f(n)
        return n

    return function


def stepper(num):
    """
    >>> s=stepper(3)
    >>> s()
    4
    >>> s()
    5
    """

    def step():
        nonlocal num
        num += 1
        return num

    return step


def add_this_many(x, el, lst):
    """
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """

    num = 0
    for li in lst:
        if li == x:
            num += 1

    n_lst = []
    for i in range(num):
        n_lst.append(el)
    lst += n_lst


def reverse(lst):
    """
    >>> x = [1]
    >>> reverse(x)
    >>> x
    [1]
    >>> x = [1, 5, 4, 2, 3]
    >>> reverse(x)
    >>> x
    [3, 2, 4, 5, 1]
    """
    for i in range(int(len(lst) / 2)):
        val = lst[i]
        t = comple = lst[len(lst) - 1 - i]
        lst[len(lst) - 1 - i] = val
        lst[i] = t


def group_by(s, fn):
    """
    >>> group_by([12,23,14,45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    """

    dicti = {}

    for element in s:
        result = fn(element)
        if result not in dicti:
            dicti[result] = [element]
        else:
            dicti[result].append(element)
    return dicti


def replace_all_deep(d, x, y):
    """
    >>> d = {1: {2: 'x', 'x': 4}, 2: {4: 4, 5: 'x'}}
    >>> replace_all_deep(d, x, y)
    >>> d
    {1: {2:'y', 'x': 4}, 2: {4: 4, 5: 'y'}}
    """
    for key in d:
        # if this is not a dictionary
        if type(d[key] != dict):
            if d[key] == x:
                d[key] = y

        # if this is a dictionary
        else:
            replace_all_deep(d[key], x, y)