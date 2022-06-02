class Solution:
    # 9. Palindrome Number
    # Given an integer x, return true if x is palindrome integer.
    # An integer is a palindrome when it reads the same backward as forward.
    # For example, 121 is a palindrome while 123 is not.
    # Solve it without converting the integer to a string
    def isPalindrome(self, x: int) -> bool:
        # Simple cases
        if x < 0:
            return False
        if x < 10:
            return True

        # parse digits from number
        digits = []
        while x > 0:
            digits.append(x % 10)
            x //= 10

        # check palindrome
        while len(digits) > 1:
            if digits[0] != digits[-1]:
                return False
            digits = digits[1:-1]

        return True


def test(test_function, expected_result, *function_arguments):
    print("Testing function: {}".format(test_function.__name__))
    print("Using arguments: {}".format(function_arguments))
    print("Expected Result: {}".format(expected_result))
    print("Actual Result: {}".format(test_function(*function_arguments)))
    assert expected_result == test_function(*function_arguments)
    print("Passed ✓\n")


def main():
    test(Solution().isPalindrome, True, 121)
    test(Solution().isPalindrome, False, -121)
    test(Solution().isPalindrome, False, 10)
    test(Solution().isPalindrome, True, 0)
    test(Solution().isPalindrome, True, 1)
    test(Solution().isPalindrome, True, 11)
    test(Solution().isPalindrome, True, 123454321)
    test(Solution().isPalindrome, True, 1234554321)
    test(Solution().isPalindrome, False, 123421)
    test(Solution().isPalindrome, False, 1000021)


if __name__ == "__main__":
    main()
