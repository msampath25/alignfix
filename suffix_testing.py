from suffix_arr import SA


def test_suffix_array():
    sa = SA("")
    assert list(sa.suffix_arr) == [0]

    sa = SA("a")
    assert list(sa.suffix_arr) == [1, 0]

    sa = SA("aaaaa")
    assert list(sa.suffix_arr) == [5, 4, 3, 2, 1, 0]

    sa = SA("abcde")
    assert list(sa.suffix_arr) == [5, 0, 1, 2, 3, 4]

    sa = SA("banana")
    assert list(sa.suffix_arr) == [6, 5, 3, 1, 0, 4, 2]

    sa = SA("abracadabra")
    assert list(sa.suffix_arr) == [11, 10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]

    sa = SA("mississippi")
    assert list(sa.suffix_arr) == [11, 10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2]

    sa = SA("hello, world!")
    assert list(sa.suffix_arr) == [6, 12, 13, 5, 11, 1, 0, 10, 2, 3, 4, 8, 9, 7]

    sa = SA("abc123def")
    assert list(sa.suffix_arr) == [9, 3, 4, 5, 0, 1, 2, 6, 7, 8]

    sa = SA("thequickbrownfoxjumpsoverthelazydog")
    assert list(sa.suffix_arr) == [
        35, 29, 8, 6, 32, 27, 2, 23, 13, 34, 26, 1, 5, 16, 7, 28, 18, 12, 33, 21,
        10, 14, 19, 3, 9, 24, 20, 25, 0, 4, 17, 22, 11, 15, 31, 30
    ]

    sa = SA("hello\nworld")
    assert list(sa.suffix_arr) == [10, 9, 1, 0, 8, 2, 3, 6, 4, 7, 5]

    sa = SA("hello\tworld")
    assert list(sa.suffix_arr) == [10, 9, 1, 0, 8, 2, 3, 6, 4, 7, 5]

    print("All test cases passed!")


test_suffix_array()
