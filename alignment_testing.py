from alignment import Alignment
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

    #testing topAlignment
    assert a1.__topAlignment__() == (0, '', '')

    #testing Align
    print(a1.Align())
    assert a1.Align() == ('CGC--AG', 'CGCGTAG')
    print('All tests pass')

test_alignment()