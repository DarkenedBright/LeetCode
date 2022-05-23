class Solution:
    # 3. Longest Substring Without Repeating Characters
    # Given a string s, find the length of the longest substring without repeating characters.
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret = 0
        character_counts = {}
        left = 0
        for right in range(len(s)):
            if s[right] in character_counts:
                left = max(left, character_counts[s[right]] + 1)
            ret = max(ret, right - left + 1)
            character_counts[s[right]] = right
        return ret

    def lengthOfLongestSubstringOriginalThought(self, s: str) -> int:
        longest_length = 0
        start_index = 0
        while start_index < len(s) - longest_length:
            length = 0
            for i in range(start_index, len(s)):
                length = i - start_index + 1
                if s[i] in s[start_index:i]:
                    length -= 1
                    break
            if length > longest_length:
                longest_length = length
            start_index += 1
        return longest_length


def test(test_function, expected_result, *function_arguments):
    print("Testing function: {}".format(test_function.__name__))
    print("Using arguments: {}".format(function_arguments))
    print("Expected Result: {}".format(expected_result))
    print("Actual Result: {}".format(test_function(*function_arguments)))
    assert expected_result == test_function(*function_arguments)
    print("Passed ✓\n")


def main():
    test(Solution().lengthOfLongestSubstring, 3, "abcabcbb")
    test(Solution().lengthOfLongestSubstring, 1, "bbbbb")
    test(Solution().lengthOfLongestSubstring, 3, "pwwkew")
    test(Solution().lengthOfLongestSubstring, 1, " ")
    test(Solution().lengthOfLongestSubstring, 2, "au")
    test(Solution().lengthOfLongestSubstring, 0, "")


if __name__ == "__main__":
    main()
