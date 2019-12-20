def all_primes(nums):
    """Given a list, return a new list which contains primes from nums.
    >>> all_primes([1, 3, 6, 7, 10, 11])
    [1, 3, 7, 11]
    """
    return [x for x in nums if is_prime(x)]


def is_prime(num):
    """
    >>> is_prime(1)
    True
    >>> is_prime(10)
    False
    """
    if num == 1:
        return True

    for x in range(2, int(num / 2) + 1):
        if num % x == 0:
            return False

    return True


def list_of_lists(lst):
    """
    >>> list_of_lists([1,2,3])
    [[0], [0, 1], [0, 1, 2]]
    >>> list_of_lists([1])
    [[0]]
    >>> list_of_lists([])
    []
    """
    my_lst = []

    for x in lst:
        l = []
        for x in range(x):
            l.append(x)
        my_lst.append(l)
    return my_lst


def sum_of_nodes(t):
    if is_leaf(t):
        return label(t)

    total = label(t)
    for branch in branches(t):
        total += sum_of_nodes(branch)
    return total


def label(tree):
    """Return the label value of a tree."""
    return tree[0]


def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]


def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)
