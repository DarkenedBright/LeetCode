from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if isinstance(other, ListNode):
            return self.val == other.val and self.next == other.next
        return False

    def __str__(self):
        ret = "["
        node = self
        while node:
            ret += "{}, ".format(node.val)
            node = node.next
        ret = ret[:-2] + "]"
        return ret


class Solution:
    # 2. Add Two Numbers
    # You are given two non-empty linked lists representing two non-negative integers.
    # The digits are stored in reverse order, and each of their nodes contains a single digit.
    # Add the two numbers and return the sum as a linked list.
    # You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode()
        current_node = ret
        carry = 0
        node_one = l1
        node_two = l2
        while node_one or node_two:
            value_one = node_one.val if node_one else 0
            value_two = node_two.val if node_two else 0
            total = value_one + value_two + carry
            mod_total = total % 10
            carry = total // 10

            new_node = ListNode(mod_total, None)
            current_node.next = new_node
            current_node = current_node.next

            node_one = node_one.next if node_one else None
            node_two = node_two.next if node_two else None
        if carry != 0:
            new_node = ListNode(carry, None)
            current_node.next = new_node
        return ret.next


def test(test_function, expected_result, *function_arguments):
    print("Testing function: {}".format(test_function.__name__))
    print("Using arguments: {}".format(function_arguments))
    print("Expected Result: {}".format(expected_result))
    print("Actual Result: {}".format(test_function(*function_arguments)))
    assert expected_result == test_function(*function_arguments)
    print("Passed ✓\n")


def main():
    test(Solution().addTwoNumbers, ListNode(7, ListNode(0, ListNode(8))), ListNode(2, ListNode(4, ListNode(3))),
         ListNode(5, ListNode(6, ListNode(4))))
    test(Solution().addTwoNumbers, ListNode(0), ListNode(0), ListNode(0))
    test(Solution().addTwoNumbers,
         ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1)))))))),
         ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))),
         ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))


if __name__ == "__main__":
    main()
