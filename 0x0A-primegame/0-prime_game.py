#!/usr/bin/python3
"""Prime Game Module"""


def isWinner(x, nums):
    """
    Determines the winner of a set of prime number removal games.

    Args:
        x (int): The number of rounds.
        nums (list of int): A list of integers where each integer n denotes
        a set of consecutive integers starting from 1 up to and including n.

    Returns:
        str: The winner name ("Ben" or "Maria").
        None: If the winner cannot be determined.
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    ben = 0
    maria = 0
    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        rm_multiples(a, i)
    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(lst, x):
    """
    Function that removes multiples of a prime number
    from an array of possible prime numbers.

    Args:
        lst (list of int): An array of possible prime numbers.
        x (int): The prime number to remove multiples of.

    Returns:
        None
    """
    for i in range(2, len(lst)):
        try:
            lst[i * x] = 0
        except (ValueError, IndexError):
            break
