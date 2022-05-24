class Solution:
    # 6. Zigzag Conversion
    # The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
    # (you may want to display this pattern in a fixed font for better legibility)
    #
    # P   A   H   N
    # A P L S I I G
    # Y   I   R
    #
    # And then read line by line: "PAHNAPLSIIGYIR"
    # Write the code that will take a string and make this conversion given a number of rows:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        # calculate pivot points.
        # Note the additional "ghost" pivot point to account for portions of the string without a real pivot point.
        pivot_point_distance = (2 * numRows) - 2
        pivot_points = [i for i in range(0, len(s) + pivot_point_distance, pivot_point_distance)]

        ret = ""
        for radius in range(numRows):
            for pivot_point in pivot_points:
                # Add left of pivot point
                if 0 <= pivot_point - radius < len(s):
                    ret += s[pivot_point - radius]
                # Handle double count scenarios
                if radius == 0 or radius == pivot_point_distance / 2:
                    continue
                # Add right of pivot point
                if pivot_point + radius < len(s):
                    ret += s[pivot_point + radius]
        return ret


def test(test_function, expected_result, *function_arguments):
    print("Testing function: {}".format(test_function.__name__))
    print("Using arguments: {}".format(function_arguments))
    print("Expected Result: {}".format(expected_result))
    print("Actual Result: {}".format(test_function(*function_arguments)))
    assert expected_result == test_function(*function_arguments)
    print("Passed ✓\n")


def main():
    test(Solution().convert, "PAHNAPLSIIGYIR", "PAYPALISHIRING", 3)
    test(Solution().convert, "PINALSIGYAHRPI", "PAYPALISHIRING", 4)
    test(Solution().convert, "PAYPALISHIRING", "PAYPALISHIRING", 1)
    test(Solution().convert, "", "", 10)
    test(Solution().convert, "TEST", "TEST", 10)
    test(Solution().convert, "AB", "AB", 2)
    test(Solution().convert, "ABDC", "ABCD", 3)


if __name__ == "__main__":
    main()
