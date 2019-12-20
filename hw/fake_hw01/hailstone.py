def hailstone(n):
    """
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    count = 1
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            print(n)
            count += 1

        else:
            n = 3 * n + 1
            print(n)
            count += 1

    return count
