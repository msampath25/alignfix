from suffix_array import SA

def test_suffix_array():
    sa = SA("")
    assert list(sa.suffix_arr) == [0]

    sa = SA("a")
    assert list(sa.suffix_arr) == [0]

    sa = SA("aaaaa")
    assert list(sa.suffix_arr) == [0, 1, 2, 3, 4]

    sa = SA("abcde")
    assert list(sa.suffix_arr) == [0, 1, 2, 3, 4]

    sa = SA("banana")
    assert list(sa.suffix_arr) == [5, 3, 1, 0, 4, 2]

    sa = SA("abracadabra")
    assert list(sa.suffix_arr) == [10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]

    sa = SA("mississippi")
    assert list(sa.suffix_arr) == [10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2]

    sa = SA("hello, world!")
    assert list(sa.suffix_arr) == [12, 11, 10, 0, 6, 8, 3, 5, 1, 7, 9, 4, 2]

    sa = SA("abc123def")
    assert list(sa.suffix_arr) == [0, 1, 2, 6, 7, 8, 3, 4, 5]

    sa = SA("thequickbrownfoxjumpsoverthelazydog")
    assert list(sa.suffix_arr) == [
        32, 20, 12, 24, 34, 10, 28, 22, 14, 26, 18, 30, 8, 16, 4, 6, 2, 0,
        31, 19, 11, 23, 33, 9, 27, 21, 13, 25, 17, 29, 7, 15, 3, 5, 1
    ]

    sa = SA("hello\nworld")
    assert list(sa.suffix_arr) == [10, 5, 0, 7, 9, 6, 1, 8, 2, 3, 4]

    sa = SA("hello\tworld")
    assert list(sa.suffix_arr) == [10, 5, 0, 7, 9, 6, 1, 8, 2, 3, 4]

    print("All test cases passed!")

test_suffix_array()
