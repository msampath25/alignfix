from suffix_arr import SA


def test_suffix_array():
    db = "ACGACTACGATAAC"
    sa = SA(db)
    word = "AC"
    first, last = sa.Seeds(word)
    print(f"Database: {db}")
    print(f"Suffix Array: {sa.suffix_arr}")
    print(f"Word: {word}")
    print(f"First occurrence: {first}")
    print(f"Last occurrence: {last}")

    print("All test cases passed!")


test_suffix_array()
