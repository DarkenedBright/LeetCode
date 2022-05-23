from typing import List


class Solution:
    # 1. Two Sum
    # Given an array of integers nums and an integer target,
    # return indices of the two numbers such that they add up to target.
    # You may assume that each input would have exactly one solution, and you may not use the same element twice.
    # You can return the answer in any order.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(nums)):
            cur_num = nums[i]
            if cur_num in cache:
                return [cache[cur_num], i]
            else:
                difference = target - cur_num
                cache[difference] = i
        return []


def test(test_function, expected_result, *function_arguments):
    print("Testing function: {}".format(test_function.__name__))
    print("Using arguments: {}".format(function_arguments))
    print("Expected Result: {}".format(expected_result))
    print("Actual Result: {}".format(test_function(*function_arguments)))
    assert expected_result == test_function(*function_arguments)
    print("Passed ✓\n")


def main():
    test(Solution().twoSum, [0, 1], [2, 7, 11, 15], 9)
    test(Solution().twoSum, [1, 2], [2, 7, 11, 15], 18)
    test(Solution().twoSum, [1, 3], [2, 7, 11, 15], 22)


if __name__ == "__main__":
    main()
