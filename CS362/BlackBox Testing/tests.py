import unittest
from credit_card_validator import credit_card_validator

#class test case for my 6 bug reveals
class TestCase(unittest.TestCase):

    #validates error case if there is no input given
    def testBugOne(self):
        self.assertEqual(credit_card_validator(''), True)

    #validates Visa cards checks if given a prefix 4 and only 15 num in length for valid length
    def testBugTwo(self):
        self.assertEqual(credit_card_validator('452100934314023'), True)

    #validates Visa cards checks if given prefix 4 and checks length for 16
    def testBugThree(self):
        self.assertEqual(credit_card_validator('4521009704314023'), True)

    #validates Amex cards checks the prefix 34 or 37 and correct input length of 16
    def testBugFour(self):
        self.assertEqual(credit_card_validator('370600982683046'), True)

    #validates Amex cards checks the prefix 34 or 37 and checks for incorrect input length of 15
    def testBugFive(self):
        self.assertEqual(credit_card_validator('3496626767003111'), True)

    #checks for Mastercard prefix 55 and checks the length correct of 16
    def testBugSix(self):
        self.assertEqual(credit_card_validator('5559973959023989'), True)


if __name__ == '__main__':
    unittest.main()
