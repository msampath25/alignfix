from suffix_arr import SA


def test_suffix_array():
    db1 = "banana"
    sa1 = SA(db1)
    assert sa1.Seeds("ana") == (1, 3)
    assert sa1.Seeds("na") == (2, 4)
    assert sa1.Seeds("a") == (1, 5)

    print("All test cases passed!")

test_suffix_array()
