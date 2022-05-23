from typing import List


class Solution:
    # 4. Median of Two Sorted Arrays
    # Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
    # The overall run time complexity should be O(log (m+n)).
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = 0
        b = len(nums1) - 1
        c = 0
        d = len(nums2) - 1
        cur_size = len(nums1) + len(nums2)
        while cur_size > 2:
            a_val = nums1[a] if len(nums1) > 0 else 1000001
            c_val = nums2[c] if len(nums2) > 0 else 1000001
            if a_val < c_val:
                nums1.pop(0)
                b -= 1
            else:
                nums2.pop(0)
                d -= 1

            b_val = nums1[b] if len(nums1) > 0 else -1000001
            d_val = nums2[d] if len(nums2) > 0 else -1000001
            if b_val > d_val:
                nums1.pop()
                b -= 1
            else:
                nums2.pop()
                d -= 1
            cur_size = len(nums1) + len(nums2)
        return sum(nums1 + nums2) / cur_size


def test(test_function, expected_result, *function_arguments):
    print("Testing function: {}".format(test_function.__name__))
    print("Using arguments: {}".format(function_arguments))
    print("Expected Result: {}".format(expected_result))
    print("Actual Result: {}".format(test_function(*function_arguments)))
    assert expected_result == test_function(*function_arguments)
    print("Passed ✓\n")


def main():
    test(Solution().findMedianSortedArrays, 2.0, [1, 3], [2])
    test(Solution().findMedianSortedArrays, 2.5, [1, 2], [3, 4])
    test(Solution().findMedianSortedArrays, 4.0, [1, 3, 5], [2, 5, 10])
    test(Solution().findMedianSortedArrays, 0.0, [0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 1])


if __name__ == "__main__":
    main()
