class Solution:
    # 8. String to Integer (atoi)
    # Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer
    # (similar to C/C++'s atoi function).
    # The algorithm for myAtoi(string s) is as follows:
    # - Read in and ignore any leading whitespace.
    # - Check if the next character (if not already at the end of the string) is '-' or '+'.
    #       Read this character in if it is either. This determines if the final result is negative or positive
    #       respectively. Assume the result is positive if neither is present.
    # - Read in next the characters until the next non-digit character or the end of the input is reached.
    #       The rest of the string is ignored.
    # - Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read,
    #       then the integer is 0. Change the sign as necessary (from step 2).
    # - If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it
    #       remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater
    #       than 231 - 1 should be clamped to 231 - 1.
    # - Return the integer as the final result.
    # Note:
    # - Only the space character ' ' is considered a whitespace character.
    # - Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
    def myAtoi(self, s: str) -> int:
        #Assume only 32-bit

        # Remove leading whitespace
        s = s.lstrip()

        if len(s) == 0:
            return 0

        # Determine positive/negative and remove character if present
        is_positive = True
        if s[0] == '-' or s[0] == '+':
            is_positive = False if s[0] == '-' else True
            s = s[1:]

        # Read in digits until there are no more. Account for integer "overflow" for 32-bits
        answer = 0
        for c in s:
            if not c.isdigit():
                break
            cur_digit = ord(c) - ord('0')

            # Handle 32-bit overflow
            if is_positive and answer > (2 ** 31 - 1) // 10:
                answer = 2 ** 31 - 1
                break
            if not is_positive and answer < (-2 ** 31) // 10:
                answer = -2 ** 31
                break
            if answer == 214748364 and cur_digit > 7:
                cur_digit = 7
            if answer == -214748364 and cur_digit > 8:
                cur_digit = 8

            answer *= 10

            if is_positive:
                answer += cur_digit
            else:
                answer -= cur_digit

        return answer


def test(test_function, expected_result, *function_arguments):
    print("Testing function: {}".format(test_function.__name__))
    print("Using arguments: {}".format(function_arguments))
    print("Expected Result: {}".format(expected_result))
    print("Actual Result: {}".format(test_function(*function_arguments)))
    assert expected_result == test_function(*function_arguments)
    print("Passed ✓\n")


def main():
    test(Solution().myAtoi, 42, "42")
    test(Solution().myAtoi, -42, "   -42")
    test(Solution().myAtoi, 4193, "4193 with words")
    test(Solution().myAtoi, 0, "")
    test(Solution().myAtoi, 2147483647, "2147483648")
    test(Solution().myAtoi, 2147483647, "2147483647")
    test(Solution().myAtoi, -2147483648, "-2147483649")
    test(Solution().myAtoi, -2147483648, "-2147483648")


if __name__ == "__main__":
    main()
