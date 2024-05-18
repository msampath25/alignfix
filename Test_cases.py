from suffix_array import SA

def test_suffix_array():
    # Empty string
    sa = SA("")
    assert list(sa.suffix_arr) == [0]

    # Single character string
    sa = SA("a")
    assert list(sa.suffix_arr) == [0]

    # String with all same characters
    sa = SA("aaaaa")
    assert list(sa.suffix_arr) == [0, 1, 2, 3, 4]

    # String with unique characters
    sa = SA("abcde")
    assert list(sa.suffix_arr) == [0, 1, 2, 3, 4]

    # String with repeated characters
    sa = SA("banana")
    assert list(sa.suffix_arr) == [5, 3, 1, 0, 4, 2]

    # String with repeated substrings
    sa = SA("abracadabra")
    assert list(sa.suffix_arr) == [10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]

    # String with multiple repeated characters
    sa = SA("mississippi")
    assert list(sa.suffix_arr) == [10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2]

    # String with special characters
    sa = SA("hello, world!")
    assert list(sa.suffix_arr) == [12, 11, 10, 0, 6, 8, 3, 5, 1, 7, 9, 4, 2]

    # String with numbers
    sa = SA("abc123def")
    assert list(sa.suffix_arr) == [0, 1, 2, 6, 7, 8, 3, 4, 5]

    # Long string
    sa = SA("thequickbrownfoxjumpsoverthelazydog")
    assert list(sa.suffix_arr) == [
        32, 20, 12, 24, 34, 10, 28, 22, 14, 26, 18, 30, 8, 16, 4, 6, 2, 0,
        31, 19, 11, 23, 33, 9, 27, 21, 13, 25, 17, 29, 7, 15, 3, 5, 1
    ]

    # String with newline character
    sa = SA("hello\nworld")
    assert list(sa.suffix_arr) == [10, 5, 0, 7, 9, 6, 1, 8, 2, 3, 4]

    # String with tab character
    sa = SA("hello\tworld")
    assert list(sa.suffix_arr) == [10, 5, 0, 7, 9, 6, 1, 8, 2, 3, 4]

    print("All test cases passed!")

# Run the test function
test_suffix_array()
