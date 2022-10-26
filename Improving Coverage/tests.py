import unittest
from contrived_func import contrived_func


# note for grader, truth tables are all written out below.
class TestCase(unittest.TestCase):
    # if we pass in the 101-149 it should evaluate true for our first if statement
    # THIS IS OUR c2, c6, c9
    def test_bug1(self):
        x = 100
        self.assertEqual(contrived_func(x), True)

    # THIS IS OUR c1
    def test_bug2(self):
        x = 110
        self.assertEqual(contrived_func(x), True)

    # THIS IS OUR C10 condition
    def test_bug3(self):
        x = 151
        self.assertEqual(contrived_func(x), False)

    # THIS IS THE C4 CONDITION
    # this tests against val == 6
    def test_bug4(self):
        x = -6
        self.assertEqual(contrived_func(x), True)

    # THIS QUALIFIES C11
    def test_bug5(self):
        x = 75
        self.assertEqual(contrived_func(x), True)

    # this qualifies our c5 condition
    def test_bug6(self):
        x = 48
        self.assertEqual(contrived_func(x), False)

    # this is our c7
    def test_bug7(self):
        x = 6
        self.assertEqual(contrived_func(x), False)


if __name__ == "__main__":
    unittest.main()


# truth tables (x) means not possible no point to even run this branch
# val < 150 | val > 100 | outcome | conditional label | test value
# True      | True      | True    | C1                | 101-150 ANY VALUE BETWEEN 101-149 should work to test the first if statment
# True      | False     | False   | C2                |
# False     | True (X)  | False   | C3
# False     | False (X) | False(X)| C3 (X)

###############################################
# val * 5 < 361 | val /2 < 24 | & outcome |val == 6: | outcome | Conditional label | Notes                                                                                          | test notes
# True          | True        | True      | True (6) | False   | C1                | if 0 or 6                                                                                      | value to test for should be 6
# True          | True        | True      | True     | True    | C2                | if its not 6 so it evaluates to true
# True          | False       | False (x) | False(x) | False(x)| C3 (X)            | if 50 but all conditionals don't run since it needs both & values to eval true
# False         | True (x)    | false (x) | False (x)| False(X)| C3 (X)            | needs both & cases to run so this evaluates to c3 again none of the conditionals are run
# False         | False (X)   | False (X) | False (X)| false(x)| C3 (x)            | needs both conditionals to run so nothing else is run

###############################################
# val > 75 |  or val /8 < 10 | && val** val % 5 == 0 | outcome | conditional label | notes
# True     | True            | True                  | true    | C1                | is this even possible?
# true     | false           | True                  | true    | C2                |
# true     | false           | false                 | false   | c3                | since && is false rest is not run
# False    | true            | true                  | true    | c1                |
# false    | false           | True                  | true    | C2                | double false for the first value before && so second part not run
# false    | false           | false (x)             | false(x)| c4                | double false for first values before && so second part not run
