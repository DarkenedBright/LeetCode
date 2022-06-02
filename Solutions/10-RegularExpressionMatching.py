class Solution:
    # 10. Regular Expression Matching
    # Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
    # - '.' Matches any single character.
    # - '*' Matches zero or more of the preceding element.
    # The matching should cover the entire input string (not partial).
    def isMatch(self, s: str, p: str) -> bool:
        if s == p:
            return True
        if len(p) == 0:
            return False

        # If second char is "*", greedily match preceding char, giving back where needed.
        if len(p) > 1 and p[1] == '*':
            zero_more_char = p[0]
            p = p[2:]

            while len(s) > 0:
                if self.isMatch(s, p):
                    return True
                if zero_more_char != '.' and s[0] != zero_more_char:
                    return False
                s = s[1:]
            return self.isMatch(s, p)
        else:
            if len(s) == 0:
                return False
            return (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])


def test(test_function, expected_result, *function_arguments):
    print("Testing function: {}".format(test_function.__name__))
    print("Using arguments: {}".format(function_arguments))
    print("Expected Result: {}".format(expected_result))
    print("Actual Result: {}".format(test_function(*function_arguments)))
    assert expected_result == test_function(*function_arguments)
    print("Passed ✓\n")


def main():
    test(Solution().isMatch, False, "aa", "a")
    test(Solution().isMatch, True, "aa", "a*")
    test(Solution().isMatch, True, "ab", ".*")
    test(Solution().isMatch, True, "aaabjks", "a*.*")
    test(Solution().isMatch, True, "testaaa", "testa*")
    test(Solution().isMatch, False, "testaaab", "testa*")
    test(Solution().isMatch, True, "", ".*")
    test(Solution().isMatch, True, "", "")
    test(Solution().isMatch, False, "ab", ".*c")
    test(Solution().isMatch, True, "aaa", "a*a")
    test(Solution().isMatch, True, "mississippi", "mis*is*ip*.")
    test(Solution().isMatch, False, "aaa", "aaaa")
    test(Solution().isMatch, True, "ab", ".*..c*")
    test(Solution().isMatch, True, "aabcbcbcaccbcaabc", ".*a*aa*.*b*.c*.*a*")


if __name__ == "__main__":
    main()
