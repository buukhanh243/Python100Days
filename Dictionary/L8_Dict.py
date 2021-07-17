import unittest


def unique(str):

    char_set = {}
    for char in str:
        print(char)
        if char in char_set:
            return False
        char_set[char] = 2
        print(char_set)
    return True

class Test(unittest.TestCase):
    dataT = [('abcd'),('s432fad'),('')]
    dataF = [('232ds2'), ('hbfashb jav ()=')]

    def test_unique(self):
        #true
        for test_case in self.dataT:
            actualResult = unique(test_case)
            self.assertTrue(actualResult)

if __name__ == '__main__':
    unittest.main()