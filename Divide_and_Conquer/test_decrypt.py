import pytest
from skeleton_decrypt import reverse_karatsuba 
from skeleton_decrypt import main 

DubaDuba_testcases = [
    ([(2, 3), (6, 5), (4, 2)],(42,23)),
    ([(1, 3), [(3, 6), (7, 8), (4, 2)], [(2, 3), (6, 5), (4, 2)]],(421,233)),
    ([[(2, 1), (6, 10), (4, 9)], [(2, 8), (6, 20), (4, 12)], (0, 37)],(42, 3791)),
    ([[(3, 3), (6, 6), (3, 3)], [(4, 5), [(9, 0), (13, 2), (4, 2)], [(5, 5), (9, 6), (4, 1)]], [(1, 2), [(3, 4), (7, 5), (4, 1)], [(2, 2), (6, 3), (4, 1)]]],(42133, 12233))
]
@pytest.mark.parametrize("filename, output",DubaDuba_testcases)
def test_reverse_karatsuba(filename, output):
    assert reverse_karatsuba(filename) == output 
     
def test_input_handling():
    assert(main("input_decrypt.txt") == [(42,23),(421,233), (42133, 12233), (42,3791)])
