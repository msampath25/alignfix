from alignfix.alignment import Alignment
import numpy as np

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
