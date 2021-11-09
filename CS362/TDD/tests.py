import random
import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    def testOne(self):
        string = '246810'
        self.assertFalse(check_pwd(string))

    def testTwo(self):
        string = 'abcdefghi'
        self.assertFalse(check_pwd(string))

    def testThree(self):
        string = 'ABCDEFGHI'
        self.assertFalse(check_pwd(string))

    def testFour(self):
        string = 'abcdEFGHI'
        self.assertFalse(check_pwd(string))

    def testFive(self):
        string = 'abcdEFGH1234~'
        self.assertFalse(check_pwd(string))

if __name__ == '__main__':
    unittest.main()
