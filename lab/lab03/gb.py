#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Red-Black binary trees properties:
1. Every node is either red or black.
2. The root is black.
3. Every leaf (NIL) is black.
4. If a node is red, then both its children are black.
5. For each node, all simple paths from the node to descendant leaves contain the same number of black nodes.
How to check them?
1, 2 and 3 are easy to check.
4 is easy as well, if x.c is red, the check that x.l.c and x.r.c are black.
How about the 5?
Well, let's visit the tree, checking that the number of black nodes in each subtree is the same.
TODO: Check that the tree is a binary tree as well.
"""
COLOR_BLACK = True
COLOR_RED = False


class Node(object):
    """The node of a red black binary tree."""
    def __init__(self, value=0, parent=None, left=None, right=None, color=COLOR_BLACK):
        self.v = value
        self.p = parent
        self.l = left
        self.r = right
        self.c = color


def rb_tree():
    """Return a proper rb tree. (Cormen, Fig. 13.4.c)"""
    T = Node(7, None, None, None, COLOR_BLACK)

    l = Node(2, T, None, None, COLOR_RED)
    T.l = l
    r = Node(11, T, None, None, COLOR_RED)
    T.r = r

    ll = Node(1, l, None, None, COLOR_BLACK)
    l.l = ll
    lr = Node(5, l, None, None, COLOR_BLACK)
    l.r = lr

    lrl = Node(4, lr, None, None, COLOR_RED)
    lr.l = lrl

    rl = Node(8, r, None, None, COLOR_BLACK)
    r.l = rl
    rr = Node(14, r, None, None, COLOR_BLACK)
    r.r = rr

    rrr = Node(15, rr, None, None, COLOR_RED)
    rr.r = rrr

    return T


def fake_rb_tree():
    """Return a fake rb tree. (Cormen, ~Fig. 13.4.a)"""
    T = Node(11, None, None, None, COLOR_BLACK)

    l = Node(2, T, None, None, COLOR_RED)
    T.l = l
    r = Node(14, T, None, None, COLOR_BLACK)
    T.r = r

    ll = Node(1, l, None, None, COLOR_BLACK)
    l.l = ll
    lr = Node(7, l, None, None, COLOR_BLACK)
    l.r = lr

    lrl = Node(5, lr, None, None, COLOR_RED)
    lr.l = lrl
    lrr = Node(8, lr, None, None, COLOR_RED)
    lr.r = lrr

    lrll = Node(4, lrl, None, None, COLOR_BLACK)
    lrl.l = lrll

    rr = Node(15, r, None, None, COLOR_RED)
    r.r = rr

    return T


def red_black_tree_check(T):
    """Check that T (root node of a generic tree) is a red black binary tree."""
    return _subtree_check(T)[0]


def _subtree_check(t):
    """
    Helper check function.
    t is the root of a subtree.
    Return the result of the check and the number of black_nodes through the path to the leaves.
    """
    if not t:  # if t is a leaf
        # #check #3
        return True, 1

    if not t.p and not t.c:  # If t is the root and its color is RED
        # #check #2
        return False, 0

    if not t.c:  # if t is red #
        # check #4
        n_blacks = 0
        if (t.l and not t.l.c) or (t.r and not t.r.c): # if either of left or right is red
            return False, -1
    else:  # else(if t is BLACK), the number of black nodes to the leaves includes the same t
        n_blacks = 1

    # Check the subtrees for #5
    r, n_blacks_r = _subtree_check(t.r)
    l, n_blacks_l = _subtree_check(t.l)

    return (r and l and n_blacks_r == n_blacks_l), n_blacks_r + n_blacks


def main():
    """Build some trees and check them!"""
    T = rb_tree()
    assert red_black_tree_check(T)

    T.c = COLOR_RED
    assert not red_black_tree_check(T)
    T.c = COLOR_BLACK

    T.l.l = COLOR_RED
    assert not red_black_tree_check(T)
    T.l.l = COLOR_BLACK

    assert not red_black_tree_check(fake_rb_tree())


if __name__ == '__main__':
    main()