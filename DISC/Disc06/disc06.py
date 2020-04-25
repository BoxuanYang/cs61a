from lab.lab07.lab07 import Link


def sum_sums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_sums(a)
    14
    """
    if lnk.rest is Link.empty:
        return lnk.first

    else:
        return lnk.first + sum_sums(lnk.rest)



