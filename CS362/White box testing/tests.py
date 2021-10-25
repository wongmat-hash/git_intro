import unittest
from contrived_func import contrived_func


# class test case for my tests
class TestCase(unittest.TestCase):

    # asserts equal to the contrived function with true passing in
    # x is declaration variable we can set to anything
    def test1(self):
        x = 5
        self.assertEqual(contrived_func(x), 1)

    def test2(self):
        x = 145
        self.assertEqual(contrived_func(x), 1)

    def test3(self):
        x = 555
        self.assertEqual(contrived_func(x), 1)

    def test4(self):
        x = 6
        self.assertEqual(contrived_func(x), 0)

    def test5(self):
        x = 161
        self.assertEqual(contrived_func(x), 0)

    def test6(self):
        x = 75
        self.assertEqual(contrived_func(x), 1)

    def test7(self):
        x = 49
        self.assertEqual(contrived_func(x), 0)


if __name__ == '__main__':
    unittest.main()
