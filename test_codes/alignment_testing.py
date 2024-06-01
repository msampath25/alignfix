from alignfix.alignment import Alignment
import numpy as np

#Some basic testing of just the alignment functions
def test_alignment():

    db1 = 'GCGCGTAGAC'
    q1 = 'CGCAG'
    s1 = 1
    l = 3
    r = len(db1)
    a1 = Alignment(db1, q1, s1, l, r)
    #testing position()
    assert a1.__position__() == (0, 3)
    #testing bottomAlignment()
    print(a1.__bottomAlignment__())
    assert a1.__bottomAlignment__() == (-3, '--AG', 'GTAG')

    #testing topAlignment -> There should be no top alignmnet since the seed starts at the 0th position in the query
    assert a1.__topAlignment__() == (0, '', '')

    #testing Align
    print(a1.Align())
    assert a1.Align() == (-3, 'CGC--AG', 'CGCGTAG')

    db2 = 'AGCTGCGCGTAGAC'
    q2 = 'ACTCGCAG'
    s2 = 5
    l = 3
    r = len(db2)
    a2 = Alignment(db2, q2, s2, l, r)

    print(a2.Align())
    assert a2.Align() == (-7, 'A-CT-CGC--AG', 'AGCTGCGCGTAG')
    print('All tests pass')

test_alignment()

#Some more basic tests for the alignment

def additional_alignment_tests():
    # Edge case: Empty database or query
    db_empty = ''
    q_empty = ''
    s_empty = 0
    l = 3
    r = 0
    a_empty = Alignment(db_empty, q_empty, s_empty, l, r)
    assert a_empty.__position__() == (0, 0)
    assert a_empty.__bottomAlignment__() == (0, '', '')
    assert a_empty.__topAlignment__() == (0, '', '')
    assert a_empty.Align() == (0, '', '')

    # Identical sequences
    db_identical = 'GATTACA'
    q_identical = 'GATTACA'
    s_identical = 0
    l = 3
    r = len(db_identical)
    a_identical = Alignment(db_identical, q_identical, s_identical, l, r)
    assert a_identical.Align() == (0, 'GATTACA', 'GATTACA')

    # Completely different sequences
    db_diff = 'GGGGGGG'
    q_diff = 'TTTTTTT'
    s_diff = 0
    l = 3
    r = len(db_diff)
    a_diff = Alignment(db_diff, q_diff, s_diff, l, r)
    assert a_diff.Align() == (-7, '-------', 'GGGGGGG')

    # Complex sequences with partial overlaps
    db_complex = 'ACTGACCTGACC'
    q_complex = 'TGACCT'
    s_complex = 1
    l = 3
    r = len(db_complex)
    a_complex = Alignment(db_complex, q_complex, s_complex, l, r)
    assert a_complex.Align() == (-2, 'TGACCT', 'TGACCT')

additional_alignment_tests()

