#!/usr/bin/python3
"""Minimum operations
"""


def minOperations(n):
    """Calculate the minimum number of operations required
    to achieve exactly n 'H' characters.
    """
    if not isinstance(n, int):
        return 0
    operations_count = 0
    clipboard = 0
    done = 1
    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            operations_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            operations_count += 2
        elif clipboard > 0:
            done += clipboard
            operations_count += 1
    return operations_count
