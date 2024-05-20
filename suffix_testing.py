from suffix_arr import SA


def test_suffix_array():
    # Test case 1: Simple string
    db1 = "banana"
    sa1 = SA(db1)
    assert sa1.Seeds("ana") == (1, 3)
    assert sa1.Seeds("na") == (2, 4)
    assert sa1.Seeds("a") == (1, 5)

    # Test case 2: String with repeated characters
    db2 = "mississippi"
    sa2 = SA(db2)
    assert sa2.Seeds("iss") == (1, 4)
    assert sa2.Seeds("si") == (3, 6)
    assert sa2.Seeds("i") == (1, 10)
    
    # Test case 3: String with no matches
    db3 = "abcdefg"
    sa3 = SA(db3)
    assert sa3.Seeds("hij") == (-42, -69)
    assert sa3.Seeds("efh") == (-42, -69)
    
    # Test case 4: Empty string
    db4 = ""
    sa4 = SA(db4)
    assert sa4.Seeds("a") == (-42, -69)
    
    print("All test cases passed!")

test_suffix_array()
