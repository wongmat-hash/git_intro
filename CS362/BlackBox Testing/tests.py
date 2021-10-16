import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):

    def testBugOne(self):
        self.assertEqual(credit_card_validator(''), True)

    def testBugTwo(self):
        self.assertEqual(credit_card_validator('452100934314023'), True)

    def testBugThree(self):
        self.assertEqual(credit_card_validator('4521009704314023'), True)

    def testBugFour(self):
        self.assertEqual(credit_card_validator('370600982683046'), True)

    def testBugFive(self):
        self.assertEqual(credit_card_validator('3496626767003111'), True)

    def testBugSix(self):
        self.assertEqual(credit_card_validator('2720995085393011'), True)


if __name__ == '__main__':
    unittest.main()
