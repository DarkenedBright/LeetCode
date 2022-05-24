class Solution:
    # 7. Reverse Integer
    # Given a signed 32-bit integer x, return x with its digits reversed.
    # If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
    # Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
    def reverse(self, x: int) -> int:
        ret = 0
        int_max = 2 ** 31 - 1
        int_min = -2 ** 31
        while x != 0:
            if x > 0:
                mod_val = x % 10
                x = x // 10
                if ret > int_max / 10 or (ret == int_max / 10 and mod_val > 7):
                    return 0
                ret = ret * 10 + mod_val
            else:
                mod_val = (10 - x % 10) % 10
                d = 0 if x % 10 == 0 else 1
                x = x // 10 + d
                if ret < int_min / 10 or (ret == int_min / 10 and mod_val > 8):
                    return 0
                ret = ret * 10 - mod_val
        return ret


def test(test_function, expected_result, *function_arguments):
    print("Testing function: {}".format(test_function.__name__))
    print("Using arguments: {}".format(function_arguments))
    print("Expected Result: {}".format(expected_result))
    print("Actual Result: {}".format(test_function(*function_arguments)))
    assert expected_result == test_function(*function_arguments)
    print("Passed ✓\n")


def main():
    test(Solution().reverse, 321, 123)
    test(Solution().reverse, -321, -123)
    test(Solution().reverse, 21, 120)
    test(Solution().reverse, 0, 2147483645)
    test(Solution().reverse, 0, -2147483645)
    test(Solution().reverse, -1, -10)


if __name__ == "__main__":
    main()
