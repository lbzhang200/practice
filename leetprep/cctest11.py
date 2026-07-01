# =============================================================================
# LINKED LISTS — FULL INTRO + PRACTICE SET
# =============================================================================
# Read the full intro before attempting problems.
# Answer key at the bottom.
# =============================================================================


# =============================================================================
# WHAT IS A LINKED LIST?
# =============================================================================
#
# A linked list is a sequence of nodes where each node holds:
#   1. A value
#   2. A pointer to the next node
#
# Unlike an array, elements are NOT stored in contiguous memory — they're
# scattered anywhere in memory, and the pointers are what link them together.
#
#   Array:   [1][2][3][4][5]     ← elements sit next to each other in memory
#   Linked:  1→2→3→4→5→None     ← elements can be anywhere, connected by pointers
#
# The last node points to None — that's how you know you've reached the end.
#
# ─────────────────────────────────────────────────────────────────────────────
# HOW TO DEFINE A NODE IN PYTHON
# ─────────────────────────────────────────────────────────────────────────────
#
#   class ListNode:
#       def __init__(self, val=0, next=None):
#           self.val = val
#           self.next = next
#
# Building a linked list 1→2→3:
#
#   head = ListNode(1)
#   head.next = ListNode(2)
#   head.next.next = ListNode(3)
#
# Traversing it:
#
#   curr = head
#   while curr:
#       print(curr.val)
#       curr = curr.next
#
# ─────────────────────────────────────────────────────────────────────────────
# ARRAY vs LINKED LIST — when each is better
# ─────────────────────────────────────────────────────────────────────────────
#
#              ARRAY          LINKED LIST
# read by index  O(1)       O(n) — must traverse from head
# insert/delete  O(n)       O(1) — just redirect pointers
# search         O(n)       O(n) — must traverse
# memory         contiguous  scattered (extra space for pointers)
#
# KEY INSIGHT: linked lists are not about being FASTER at searching —
# they're about making INSERT and DELETE cheap by just rewiring pointers
# instead of shifting elements.
#
# ─────────────────────────────────────────────────────────────────────────────
# WHAT PROBLEMS ARE LINKED LISTS GOOD FOR?
# ─────────────────────────────────────────────────────────────────────────────
#
# 1. Reversal problems — reverse the whole list or a portion of it
# 2. Cycle detection — does the list loop back on itself?
# 3. Finding the middle — what's the middle node?
# 4. Merging — combine two sorted linked lists
# 5. Removing nodes — delete the nth node from the end, remove duplicates
#
# ─────────────────────────────────────────────────────────────────────────────
# THE PATTERNS — and how they map to what you already know
# ─────────────────────────────────────────────────────────────────────────────
#
# TWO POINTERS (slow/fast — also called tortoise and hare):
#   Same idea as two pointers in arrays, but you move through .next
#   instead of incrementing indices.
#
#   fast moves 2 steps at a time, slow moves 1:
#
#   slow, fast = head, head
#   while fast and fast.next:
#       slow = slow.next
#       fast = fast.next.next
#
#   When fast reaches the end, slow is at the MIDDLE.
#   If fast ever equals slow again (after starting), there's a CYCLE.
#
# POINTER MANIPULATION:
#   Most linked list operations come down to redirecting .next pointers.
#   The key skill is doing this WITHOUT losing track of nodes —
#   always save a reference to the next node before you overwrite it.
#
#   # reversing — the core three-pointer pattern:
#   prev = None
#   curr = head
#   while curr:
#       next_node = curr.next   # save next BEFORE overwriting
#       curr.next = prev        # reverse the pointer
#       prev = curr             # move prev forward
#       curr = next_node        # move curr forward
#   return prev   # prev is the new head
#
# DUMMY NODE:
#   For problems involving insertions or deletions at the head of the list,
#   a dummy node simplifies edge cases. It's a fake node that sits before
#   the real head so you never have to treat the head differently.
#
#   dummy = ListNode(0)
#   dummy.next = head
#   # ... do your work ...
#   return dummy.next   # the real head of the result
#
# ─────────────────────────────────────────────────────────────────────────────
# SIGNAL WORDS IN PROBLEMS
# ─────────────────────────────────────────────────────────────────────────────
# "reverse", "cycle", "middle", "nth from end", "merge", "remove",
# "detect loop", "palindrome linked list"
#
# =============================================================================


# helper class — all problems below use this
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        # helper to print list nicely for testing
        result = []
        curr = self
        while curr:
            result.append(str(curr.val))
            curr = curr.next
        return " -> ".join(result)


def build_list(values):
    # helper to build a linked list from a Python list
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


# -----------------------------------------------------------------------------
# L1. LC 206 — Reverse Linked List (Easy) | POINTER MANIPULATION
# -----------------------------------------------------------------------------
# Given the head of a linked list, reverse it and return the new head.
#
# Example:
#   Input:  1 -> 2 -> 3 -> 4 -> 5
#   Output: 5 -> 4 -> 3 -> 2 -> 1
#
# Hint: three pointers — prev, curr, next_node.
#       save next before overwriting. reverse the pointer. move forward.
#       when curr is None, prev is the new head.
# -----------------------------------------------------------------------------

def reverse_list(head):
    prev = None 
    curr = head 
    while curr:
        nextnode = curr.next
        curr.next = prev 
        prev = curr 
        curr = nextnode 
    return prev  


# -----------------------------------------------------------------------------
# L2. LC 21 — Merge Two Sorted Lists (Easy) | POINTER MANIPULATION + DUMMY
# -----------------------------------------------------------------------------
# Given the heads of two sorted linked lists, merge them into one sorted
# linked list and return the head of the merged list.
#
# Example:
#   list1: 1 -> 2 -> 4
#   list2: 1 -> 3 -> 4
#   Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4
#
# Hint: use a dummy node as a starting point so you never have to
#       special-case the head. Keep a "tail" pointer pointing to the
#       last node of the result so far. At each step, compare list1.val
#       and list2.val, attach the smaller one to tail.next, and advance.
#       When one list runs out, attach the remainder of the other.
# -----------------------------------------------------------------------------

def merge_two_lists(list1, list2):
    pass


# -----------------------------------------------------------------------------
# L3. LC 141 — Linked List Cycle (Easy) | SLOW/FAST POINTERS
# -----------------------------------------------------------------------------
# Given the head of a linked list, return True if it has a cycle.
# A cycle means some node's next pointer points back to a previous node.
#
# Example:
#   3 -> 2 -> 0 -> -4 -> (back to 2)   Output: True
#   1 -> 2                              Output: False
#
# Hint: slow moves 1 step, fast moves 2 steps. if there's a cycle,
#       fast will eventually lap slow and they'll meet.
#       if there's no cycle, fast will reach None.
# -----------------------------------------------------------------------------

def has_cycle(head):
    pass


# -----------------------------------------------------------------------------
# L4. LC 876 — Middle of the Linked List (Easy) | SLOW/FAST POINTERS
# -----------------------------------------------------------------------------
# Given the head of a linked list, return the middle node.
# If two middle nodes exist, return the second one.
#
# Example:
#   1 -> 2 -> 3 -> 4 -> 5   Output: node 3
#   1 -> 2 -> 3 -> 4        Output: node 3  (second middle)
#
# Hint: slow moves 1 step, fast moves 2 steps. when fast reaches
#       the end, slow is at the middle.
# -----------------------------------------------------------------------------

def middle_node(head):
    pass


# -----------------------------------------------------------------------------
# L5. LC 203 — Remove Linked List Elements (Easy) | POINTER MANIPULATION
# -----------------------------------------------------------------------------
# Given the head of a linked list and an integer val, remove all nodes
# with value equal to val and return the new head.
#
# Example:
#   head = 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6, val = 6
#   Output: 1 -> 2 -> 3 -> 4 -> 5
#
# Hint: use a dummy node before head to handle deletions at the head cleanly.
#       keep a "curr" pointer. if curr.next.val == val, skip it by setting
#       curr.next = curr.next.next. otherwise advance curr.
# -----------------------------------------------------------------------------

def remove_elements(head, val):
    pass


# -----------------------------------------------------------------------------
# L6. LC 83 — Remove Duplicates from Sorted List (Easy) | POINTER MANIPULATION
# -----------------------------------------------------------------------------
# Given the head of a SORTED linked list, remove all duplicates so each
# value appears only once.
#
# Example:
#   1 -> 1 -> 2        Output: 1 -> 2
#   1 -> 1 -> 2 -> 3 -> 3   Output: 1 -> 2 -> 3
#
# Hint: compare curr.val to curr.next.val. if they're the same, skip
#       curr.next by setting curr.next = curr.next.next.
#       if different, advance curr normally.
# -----------------------------------------------------------------------------

def delete_duplicates(head):
    pass


# -----------------------------------------------------------------------------
# L7. LC 19 — Remove Nth Node From End of List (Medium) | SLOW/FAST POINTERS
# -----------------------------------------------------------------------------
# Given the head of a linked list, remove the nth node from the END
# and return the head.
#
# Example:
#   head = 1 -> 2 -> 3 -> 4 -> 5, n = 2
#   Output: 1 -> 2 -> 3 -> 5   (removed node 4, which is 2nd from end)
#
# Hint: use a dummy node. send fast pointer n+1 steps ahead of slow.
#       then move both forward together until fast reaches None.
#       now slow.next is the node to remove — set slow.next = slow.next.next.
#       why n+1? because you want slow to stop at the node BEFORE the
#       one you're deleting, so you can redirect its next pointer.
# -----------------------------------------------------------------------------

def remove_nth_from_end(head, n):
    pass


# =============================================================================
#
#
#
#   ANSWER KEY — scroll down only after attempting everything!
#
#
#
# =============================================================================
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# =============================================================================
# ANSWER KEY
# =============================================================================


# L1. Reverse Linked List — POINTER MANIPULATION
# three pointers: prev, curr, next_node.
# save next before overwriting. reverse pointer. move both forward.
# when curr is None, prev is the new head.
# Time: O(n) | Space: O(1)

def reverse_list_answer(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next   # save next BEFORE overwriting
        curr.next = prev        # reverse the pointer
        prev = curr             # move prev forward
        curr = next_node        # move curr forward
    return prev


# L2. Merge Two Sorted Lists — DUMMY NODE + POINTER MANIPULATION
# dummy node avoids special-casing the head.
# tail tracks end of result. attach smaller node, advance that list.
# attach remainder when one list runs out.
# Time: O(n + m) | Space: O(1)

def merge_two_lists_answer(list1, list2):
    dummy = ListNode(0)
    tail = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 if list1 else list2
    return dummy.next


# L3. Linked List Cycle — SLOW/FAST POINTERS
# fast moves 2 steps, slow moves 1. if cycle exists, they meet.
# if fast reaches None, no cycle.
# Time: O(n) | Space: O(1)

def has_cycle_answer(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# L4. Middle of Linked List — SLOW/FAST POINTERS
# fast moves 2 steps, slow moves 1. when fast hits end, slow is at middle.
# for even-length lists, slow lands on the SECOND middle node.
# Time: O(n) | Space: O(1)

def middle_node_answer(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


# L5. Remove Linked List Elements — DUMMY NODE
# dummy before head handles deletion of head node cleanly.
# check curr.next.val — if match, skip it. else advance curr.
# Time: O(n) | Space: O(1)

def remove_elements_answer(head, val):
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next   # skip the node
        else:
            curr = curr.next             # advance normally
    return dummy.next


# L6. Remove Duplicates from Sorted List — POINTER MANIPULATION
# compare curr.val to curr.next.val.
# if same, skip curr.next. if different, advance.
# Time: O(n) | Space: O(1)

def delete_duplicates_answer(head):
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next   # skip duplicate
        else:
            curr = curr.next             # advance
    return head


# L7. Remove Nth Node From End — SLOW/FAST POINTERS + DUMMY NODE
# dummy node handles edge case of removing the head.
# send fast n+1 steps ahead so slow stops at node BEFORE the target.
# then skip slow.next.
# Time: O(n) | Space: O(1)

def remove_nth_from_end_answer(head, n):
    dummy = ListNode(0)
    dummy.next = head
    slow, fast = dummy, dummy

    # move fast n+1 steps ahead
    for _ in range(n + 1):
        fast = fast.next

    # move both until fast reaches None
    while fast:
        slow = slow.next
        fast = fast.next

    # slow is now at the node before the one to remove
    slow.next = slow.next.next

    return dummy.next