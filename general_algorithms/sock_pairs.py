#!/usr/bin/python3

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    """
    ----------------------
    METHOD: socketMerchant
    ----------------------
    Description:
        Finds the number of pairs
        that are possible in an array.

        Credits:
            https://www.hackerrank.com/challenges/sock-merchant/problem
    Args:
        @n: len of ar
        @ar: input array
    Return:
        Number of pairs possible
    """
    sock = {}

    for color in ar:
        if color not in sock:
            sock[color] = 1
        else:
            sock[color] += 1

    pair_count = 0
    for key, val in sock.items():
        if val > 0:
            pair_count += val // 2

    return pair_count