# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 is None and list2 is None:
            return
        new_list = ListNode()
        merged_list_ptr = new_list

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                merged_list_ptr.val = list1.val
                list1 = list1.next
            else:
                merged_list_ptr.val = list2.val
                list2 = list2.next

            if list1 is not None or list2 is not None:
                merged_list_ptr.next = ListNode()
                merged_list_ptr = merged_list_ptr.next

        while list1 is not None:
            merged_list_ptr.val = list1.val
            list1 = list1.next
            if list1 is not None or list2 is not None:
                merged_list_ptr.next = ListNode()
                merged_list_ptr = merged_list_ptr.next

        while list2 is not None:
            merged_list_ptr.val = list2.val
            list2 = list2.next
            if list1 is not None or list2 is not None:
                merged_list_ptr.next = ListNode()
                merged_list_ptr = merged_list_ptr.next

        return new_list


tests = [
    (
        ([1, 2, 4], [1, 3, 4]),
        [1, 1, 2, 3, 4, 4],
    ),
    (
        ([1, 2, 4], [1, 3, 4]),
        [1, 1, 2, 3, 4, 4],
    ),
    (
        ([1, 2, 4], [1, 3, 4]),
        [1, 1, 2, 3, 4, 4],
    ),
]
