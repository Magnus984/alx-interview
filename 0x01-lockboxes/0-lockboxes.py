#!/usr/bin/python3
"""Lockboxes
"""

def canUnlockAll(boxes):
    """Determine whether all the boxes in a list,
    which contain keys (indices) to other boxes,
    can be unlocked, assuming that the first box is already unlocked.
    """
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    return n == len(seen_boxes)
