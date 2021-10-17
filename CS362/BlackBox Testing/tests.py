import unittest
from credit_card_validator import credit_card_validator


# class test case for my 6 bug reveals
class TestCase(unittest.TestCase):

    # validates error case if there is no input given invalid check returns F
    # picked using category partition testing
    def testBugOne(self):
        self.assertEqual(credit_card_validator(''), True)

    # validates Visa cards checks for corect prefix and length invalid = F
    # picked using category partition testing
    def testBugTwo(self):
        self.assertEqual(credit_card_validator('452100934314023'), True)

    # checks against Mastercards checks for outside prefixs and length of 16
    # picked using category partition testing
    def testBugThree(self):
        self.assertEqual(credit_card_validator('2720995085393011'), True)

    # validates Amex cards checks the prefix 34 or 37 and correct length of 16
    # picked using category partition testing 
    def testBugFour(self):
        self.assertEqual(credit_card_validator('370600982683046'), True)

    # validates Amex cards checks the prefix and for incorrect length of 15
    # picked using category partition testing
    def testBugFive(self):
        self.assertEqual(credit_card_validator('3496626767003111'), True)

    # validates Visa cards checks if given prefix 4 and checks length for 16
    # picked using category partition testing
    def testBugSix(self):
        self.assertEqual(credit_card_validator('4521009704314023'), True)


if __name__ == '__main__':
    unittest.main()
