from unittest import TestCase
import luhn_check

class TestLuhnCheck(TestCase):

    def setUp(self):
        pass
    def test_known_sum(self):
        self.assertEquals(67, luhn_check.check_sum("7992739871"))

    def test_check_digit(self):
        self.assertEquals(3, luhn_check.find_check_digit("7992739871"))

    def test_check_valid(self):
        self.assertFalse(luhn_check.is_luhn_valid("abcdefg"))
        self.assertTrue(luhn_check.is_luhn_valid("79927398713"))

    def test_check_invalid(self):
        self.assertFalse(luhn_check.is_luhn_valid("79927398714"))

    def test_regex(self):
        self.assertTrue(luhn_check.check_regex("346340033233241"))
        self.assertFalse(luhn_check.check_regex("996340033233241"))

    def test_check_cc(self):
        #amex
        self.assertTrue(luhn_check.is_valid_cc("346340033233241"))
        #discover
        self.assertTrue(luhn_check.is_valid_cc("6011066253550425"))
        #visa
        self.assertTrue(luhn_check.is_valid_cc("4485332611430235"))
        #mc
        self.assertTrue(luhn_check.is_valid_cc("5463393720504875"))
        #bad:
        self.assertFalse(luhn_check.is_valid_cc("abcdefg"))
        self.assertFalse(luhn_check.is_valid_cc("11abcdefg"))
        self.assertFalse(luhn_check.is_valid_cc("946340033233241"))
        self.assertFalse(luhn_check.is_valid_cc("546339372050487500"))
