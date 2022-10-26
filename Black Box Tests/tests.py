import unittest
from credit_card_validator import credit_card_validator


# notes for grader. Cases 1-13 are me trying out annd learning the syntax. I am also learning how Luhn's number works.
# cases 14-45 are written with category partition I am breaking up the categories by: Prefix, Length, Bit (Luhns law correct or not)
# cases 48-76 are all written as boundary testing with cases derived from category partition
class TestCase(unittest.TestCase):
    # this test should be valid for VISA since it starts with 4 and has 16 chars
    def test_bug1(self):
        self.assertEqual(credit_card_validator("412345678901234"), False)

    # this test should be valid for MasterCard starts with 51 and has 16 chars
    def test_bug2(self):
        self.assertEqual(credit_card_validator("5151525252535353"), False)

    # this test should be valid for Amex starts with 34 has 16 chars and satisifies luhns VALID WORKS ON GRADASCOPE bug4
    def test_bug3(self):
        self.assertEqual(credit_card_validator("341234567890123"), False)

    # this tests that there is a valid input and is not empty which would error VALID WORKS ON GRADASCOPE
    def test_bug4(self):
        self.assertEqual(credit_card_validator(""), False)

    # this test makes sure that we only have strings with numeric values
    def test_bug5(self):
        self.assertEqual(credit_card_validator("A123456789012345"), False)

    # this test makes sure that we are under 17 or more characters
    def test_bug6(self):
        self.assertEqual(credit_card_validator("4123456789012345678"), False)

    # this tests make sure that we don't have invalid prefix like 0
    def test_bug7(self):
        self.assertEqual(credit_card_validator("01234567890123456"), False)

    # this checks to make sure that we aren't looking at strings with characters
    def test_bug8(self):
        self.assertEqual(credit_card_validator("ABCDEFGHIJKLMNOP"), False)

    # this test will test for MasterCard with the prefix and length count
    def test_bug9(self):
        self.assertEqual(credit_card_validator("4485432427872033859"), True)

    # this test will test for VISA with prefix and legnth count and satisfies luhns VALID GRADASCOPE
    def test_bug11(self):
        self.assertEqual(credit_card_validator("4485862702116970"), True)

    # this tests for a valid amex with valid length and valid bit THIS SATISFIES BUG 4 in gradascope
    def test_bug12(self):
        self.assertEqual(credit_card_validator("371381253951375"), True)

    # this safisfies bug 4 again in gradascope
    def test_bug13(self):
        self.assertEqual(credit_card_validator("349559681295098"), True)

    # This tests for mastercard with length and prefix but bit count is off OUNTS FOR TEST 6 GRADASCOPE if 2720995085393011
    def test_bug14(self):
        self.assertEqual(credit_card_validator("2720995085393012"), False)

    # CASES 14-45 are all selected via category partition testing
    # this is a mastercard that satisfies luhns and prefix and length THIS SATISIFIES Bug 6
    def test_bug15(self):
        self.assertEqual(credit_card_validator("2720128412342234"), True)

    # CASES 14-45 are all selected via category partition testing
    # same mastercard test but test out of range prefix with valid luhns
    def test_bug16(self):
        self.assertEqual(credit_card_validator("2721123412341224"), False)

    # CASES 14-45 are all selected via category partition testing
    # same mastercard test with prefix in range and valid luhns
    def test_bug17(self):
        self.assertEqual(credit_card_validator("2719123412341230"), True)

    # CASES 14-45 are all selected via category partition testing
    # visa prefix correct, length correct, bit correct
    def test_bug18(self):
        self.assertEqual(credit_card_validator("4123123422444244"), True)

    # CASES 14-45 are all selected via category partition testing
    # visa prefix incorrect, length correct, bit correct
    def test_bug19(self):
        self.assertEqual(credit_card_validator("5123123412841284"), False)

    # CASES 14-45 are all selected via category partition testing
    # visa prefix incorrect, length incorrect, bit correct
    def test_bug20(self):
        self.assertEqual(credit_card_validator("75123123412441244"), False)

    # CASES 14-45 are all selected via category partition testing
    # visa prefix incorrect, length incorrect, bit incorrect
    def test_bug21(self):
        self.assertEqual(credit_card_validator("512341234123412"), False)

    # CASES 14-45 are all selected via category partition testing
    # visa prefix incorrect, length correct, bit incorrect
    def test_bug22(self):
        self.assertEqual(credit_card_validator("5123412341234123"), False)

    # CASES 14-45 are all selected via category partition testing
    # visa prefix correct, length correct, bit incorrect
    def test_bug23(self):
        self.assertEqual(credit_card_validator("4123412341234123"), False)

    # CASES 14-45 are all selected via category partition testing
    # 34AMEX prefix correct, length correct, bit correct this satisfies bug 4 again in gradascope
    def test_bug24(self):
        self.assertEqual(credit_card_validator("341234123412341"), True)

    # CASES 14-45 are all selected via category partition testing
    # 34AMEX prefix incorrect, length correct, bit correct
    def test_bug25(self):
        self.assertEqual(credit_card_validator("721234123412341"), False)

    # CASES 14-45 are all selected via category partition testing
    # 34AMEX prefix incorrect, length incorrect, bit correct
    def test_bug26(self):
        self.assertEqual(credit_card_validator("80223412341084"), False)

    # CASES 14-45 are all selected via category partition testing
    # 34AMEX prefix incorrect, length incorrect, bit incorrect
    def test_bug27(self):
        self.assertEqual(credit_card_validator("90123412341234"), False)

    # CASES 14-45 are all selected via category partition testing
    # 34AMEX prefix incorrect, length correct, bit incorrect
    def test_bug28(self):
        self.assertEqual(credit_card_validator("901234123412341"), False)

    # CASES 14-45 are all selected via category partition testing
    # 34AMEX prefix correct, length correct, bit incorrect
    def test_bug29(self):
        self.assertEqual(credit_card_validator("341234123412340"), False)

    # CASES 14-45 are all selected via category partition testing
    # 37AMEX prefix correct, length correct, bit correct this satisifes bug 4 in gradascope
    def test_bug30(self):
        self.assertEqual(credit_card_validator("331234123412384"), True)

    # CASES 14-45 are all selected via category partition testing
    # 37AMEX prefix incorrect, length correct, bit correct
    def test_bug31(self):
        self.assertEqual(credit_card_validator("681234123412331"), True)

    # CASES 14-45 are all selected via category partition testing
    # 37AMEX prefix incorrect, length incorrect, bit correct
    def test_bug32(self):
        self.assertEqual(credit_card_validator("80623412341234"), False)

    # CASES 14-45 are all selected via category partition testing
    # 37AMEX prefix incorrect, length incorrect, bit incorrect
    def test_bug33(self):
        self.assertEqual(credit_card_validator("80123517210102"), False)

    # CASES 14-45 are all selected via category partition testing
    # 37AMEX prefix incorrect, length correct, bit incorrect
    def test_bug34(self):
        self.assertEqual(credit_card_validator("721234567891234"), False)

    # CASES 14-45 are all selected via category partition testing
    # 37AMEX prefix correct, length correct, bit incorrect this satisifes bug4 in gradascope
    def test_bug35(self):
        self.assertEqual(credit_card_validator("371234123412341"), False)

    # CASES 14-45 are all selected via category partition testing
    # case 1 of mastercard 51-55 prefix correct, length correct, bit correct
    def test_bug36(self):
        self.assertEqual(credit_card_validator("532341234223472"), True)

    # CASES 14-45 are all selected via category partition testing
    # case 2 of mastercard 51-55 prefix INCORRECT, length CORRECT, bit CORRECT
    def test_bug37(self):
        self.assertEqual(credit_card_validator("3232341234123422"), False)

    # CASES 14-45 are all selected via category partition testing
    # case 3 of mastercard 51-55 prefix INCORRECT, length INCORRECT, bit, CORRECT
    def test_bug38(self):
        self.assertEqual(credit_card_validator("123412341234135"), False)

    # CASES 14-45 are all selected via category partition testing
    # case 4 of mastercard 51-55 prefix INCORRECT, length INCORRECT, bit INCORRECT
    def test_bug39(self):
        self.assertEqual(credit_card_validator("123412341234136"), False)

    # CASES 14-45 are all selected via category partition testing
    # case 5 of mastercard 51-55 prefix INCORRECT, length CORRECT, bit INCORRECT
    def test_bug40(self):
        self.assertEqual(credit_card_validator("1234123412341234"), False)

    # CASES 14-45 are all selected via category partition testing
    # case 6 of mastercard 51-55 prefix CORRECT, length CORRECT, bit INCORRECT
    def test_bug41(self):
        self.assertEqual(credit_card_validator("5312341234123413"), False)

    # CASES 14-45 are all selected via category partition testing
    # case 1 of mastercard 2221-2720 prefix correct, length correct, bit correct
    def test_bug42(self):
        self.assertEqual(credit_card_validator("2221123412341223"), True)

    # CASES 14-45 are all selected via category partition testing
    # case 2 of mastercard 2221-2720  prefix INCORRECT, length CORRECT, bit CORRECT
    def test_bug43(self):
        self.assertEqual(credit_card_validator("2220123412341224"), False)

    # CASES 14-45 are all selected via category partition testing
    # case 3 of mastercard 2221-2720  prefix INCORRECT, length INCORRECT, bit, CORRECT
    def test_bug44(self):
        self.assertEqual(credit_card_validator("22191234123417345"), False)

    # CASES 14-45 are all selected via category partition testing
    # case 4 of mastercard 2221-2720  prefix INCORRECT, length INCORRECT, bit INCORRECT
    def test_bug45(self):
        self.assertEqual(credit_card_validator("111122223333"), False)

    # CASES 14-45 are all selected via category partition testing
    # case 5 of mastercard 2221-2720  prefix INCORRECT, length CORRECT, bit INCORRECT
    def test_bug46(self):
        self.assertEqual(credit_card_validator("9721291187221731"), False)

    # CASES 14-45 are all selected via category partition testing
    # case 6 of mastercard 2221-2720  prefix CORRECT, length CORRECT, bit INCORRECT this satifisfies bug 6 in gradasccope
    def test_bug47(self):
        self.assertEqual(credit_card_validator("2720945384373914"), False)

    # these CASES are all selected for boundary testing 48-76
    # case to check for all prefix for Visa for 4 this is correct prefix and length and bit
    def test_bug48(self):
        self.assertEqual(credit_card_validator("4123451230512385"), True)

    # these CASES are all selected for boundary testing 48-76
    # case to check for all prefix for visa for 3 this is incorrect prefix and correct length and bit
    def test_bug49(self):
        self.assertEqual(credit_card_validator("3123412341234147"), False)

    # these CASES are all selected for boundary testing 48-76
    # case to check for prefix for Visa for 5 this is incorrect prefix and correct length and bit
    def test_bug50(self):
        self.assertEqual(credit_card_validator("5123451934512365"), False)

    # these CASES are all selected for boundary testing 48-76
    # case for mastercard prefix for 50 wrong prefix correct bit and length
    def test_bug51(self):
        self.assertEqual(credit_card_validator("5012345023451234"), False)

    # these CASES are all selected for boundary testing 48-76
    # case for mastercard prefix for 51 correct prefix and correct bit and length
    def test_bug52(self):
        self.assertEqual(credit_card_validator("5123451234512925"), True)

    # these CASES are all selected for boundary testing 48-76
    # case for mastercard prefix for 52 this is correct prefix length and bit
    def test_bug53(self):
        self.assertEqual(credit_card_validator("5934512345124451"), True)

    # these CASES are all selected for boundary testing 48-76
    # case for mastercard prefix for 53 correct prefix correct length and bit
    def test_bug54(self):
        self.assertEqual(credit_card_validator("5345123451233"), True)

    # these CASES are all selected for boundary testing 48-76
    # case for mastercard prefix for 54 correct prefix correct length and bit
    def test_bug55(self):
        self.assertEqual(credit_card_validator("5417345123451234"), True)

    # these CASES are all selected for boundary testing 48-76
    # case for mastercard prefix for 55 correct prefix correct lenght and bit
    def test_bug56(self):
        self.assertEqual(credit_card_validator("5567123451234573"), True)

    # these CASES are all selected for boundary testing 48-76
    # case for mastercard prefix for 56 correct prefix length and bit
    def test_bug57(self):
        self.assertEqual(credit_card_validator("56781274546781244"), True)

    # these CASES are all selected for boundary testing 48-76
    # case for mastercard prefix for 2220 correct prefix, length and bit
    def test_bug58(self):
        self.assertEqual(credit_card_validator("222012345123431"), True)

    # these CASES are all selected for boundary testing 48-76
    # case for mastercard prefix for 2221 correct prefix length and bit
    def test_bug59(self):
        self.assertEqual(credit_card_validator("222123450234572"), True)

    # these CASES are all selected for boundary testing 48-76
    # case for mastercard prefix for 2222 correct prefix lengt and bit
    def test_bug60(self):
        self.assertEqual(credit_card_validator("222212345123411"), True)

    # these CASES are all selected for boundary testing 48-76
    # case for mastercard prefix for 2300 correct prefix legnth and bit
    def test_bug61(self):
        self.assertEqual(credit_card_validator("230032345123421"), True)

    # these CASES are all selected for boundary testing 48-76
    # case for mastercard prefix for 2400 correct prefix legnth and bit
    def test_bug62(self):
        self.assertEqual(credit_card_validator("240012345123421"), True)

    # these CASES are all selected for boundary testing 48-76
    # case for mastercard prefix for 2500 correct prefix legnth and bit
    def test_bug63(self):
        self.assertEqual(credit_card_validator("250012345103461"), True)

    # these CASES are all selected for boundary testing 48-76
    # case for mastercard prefix for 2600 correct prefix legnth and bit
    def test_bug64(self):
        self.assertEqual(credit_card_validator("260012345612345"), True)

    # these CASES are all selected for boundary testing 48-76
    # case for mastercard prefix for 2700 correct prefix legnth and bit
    def test_bug65(self):
        self.assertEqual(credit_card_validator("270012345612335"), True)

    # these CASES are all selected for boundary testing 48-76
    # case for mastercard prefix for 2719 correct prefix legnth and bit
    def test_bug66(self):
        self.assertEqual(credit_card_validator("2719123451204562"), True)

    # these CASES are all selected for boundary testing 48-76
    # case for mastercard prefix for 2720 correct prefix legnth and bit THIS SATISISFIES BUG 6
    def test_bug67(self):
        self.assertEqual(credit_card_validator("2720123456239552"), True)

    # these CASES are all selected for boundary testing 48-76
    # case for mastercard prefix for 2721 incorrect prefix legnth and bit
    def test_bug68(self):
        self.assertEqual(credit_card_validator("2721123412341224"), False)

    # these CASES are all selected for boundary testing 48-76
    # case for mastercard prefix for 2800 incorrect prefix legnth and bit
    def test_bug69(self):
        self.assertEqual(credit_card_validator("2800123412342334"), False)

    # these CASES are all selected for boundary testing 48-76
    # case for amex for 33 incorrect prefix correct length and bit
    def test_bug70(self):
        self.assertEqual(credit_card_validator("331231234123422"), False)

    # these CASES are all selected for boundary testing 48-76
    # case for amex for 34 correct prefix correct length and bit THIS SATISFIES BUG 4
    def test_bug71(self):
        self.assertEqual(credit_card_validator("341231234112323"), True)

    # these CASES are all selected for boundary testing 48-76
    # case for amex for 35 correct prefix correct length and bit
    def test_bug72(self):
        self.assertEqual(credit_card_validator("351234510340193"), True)

    # these CASES are all selected for boundary testing 48-76
    # case for amex for 36 correct prefix correct length and bit
    def test_bug73(self):
        self.assertEqual(credit_card_validator("361231034512305"), True)

    # these CASES are all selected for boundary testing 48-76
    # case for amex for 37 correct prefix correct length and bit THIS SATIFISFIES BUG 4
    def test_bug74(self):
        self.assertEqual(credit_card_validator("371231034512345"), True)

    # these CASES are all selected for boundary testing 48-76
    # case for amex for 38 incorrect prefix correct length and bit
    def test_bug75(self):
        self.assertEqual(credit_card_validator("381231234511345"), False)

    # these CASES are all selected for boundary testing 48-76
    # This test checks for spaces in the middle of strings
    def test_bug76(self):
        self.assertEqual(credit_card_validator("2700123 5612335"), False)

    # checks to see if other bugs work as properly this is derived from cateogry partition on error handling
    # this particular test checks for spaces in the middle of strings
    def test_bug77(self):
        self.assertEqual(credit_card_validator("2700123 54612335"), False)

    # this case satisfies the out of range for length and prefix derived from category parition
    def test_bug78(self):
        self.assertEqual(credit_card_validator("2981517136451293"), False)

    # all these tests check for spaces for each individual card being correct for before and after
    def test_bug79(self):
        self.assertEqual(credit_card_validator(" 351234510340193"), False)

    # This is derived from category partition on error handling with a space before using correct prefix
    def test_bug80(self):
        self.assertEqual(credit_card_validator(" 2720123456239552"), False)

    # This is checking for a space before and with a valid string. Derived from error handling from category partition
    def test_bug81(self):
        self.assertEqual(credit_card_validator(" 240012345123421"), False)

    # This is checking for spaces after. Derived from category parition on error handling
    def test_bug82(self):
        self.assertEqual(credit_card_validator("240012345123421 "), False)

    # This checks for a valid visa with invalid length derived from category parition
    def test_bug83(self):
        self.assertEqual(credit_card_validator("41234512345123455"), False)

    # This checks for visa with valid string and invalid length derived from category parition
    def test_bug84(self):
        self.assertEqual(credit_card_validator("412345123451239"), False)

    # This checks for valid mastercard with invalid length using cateogyr parition
    def test_bug85(self):
        self.assertEqual(credit_card_validator("512345123451239"), False)

    # This checks for valid string mastercard with invalid length using cateogyr parition
    def test_bug86(self):
        self.assertEqual(credit_card_validator("51234512345123454"), False)

    # This checks for valid amex with invalid length using cateogyr partioin
    def test_bug87(self):
        self.assertEqual(credit_card_validator("34123416341236"), False)

    # 14-45 after bug this bug checks for amex with invalid length 16 THIS SATISFIES BUG 5
    def test_bug88(self):
        self.assertEqual(credit_card_validator("3412341234123416"), False)

    # This bug checks for just prefixs for Visa
    def test_bug89(self):
        self.assertEqual(credit_card_validator("4"), False)

    # This bug checks for just prefixs for Mastercards
    def test_bug90(self):
        self.assertEqual(credit_card_validator("51"), False)

    # This bug checks for just prefixs for Mastercards
    def test_bug91(self):
        self.assertEqual(credit_card_validator("52"), False)

    # This bug checks for just prefixs for Mastercards
    def test_bug92(self):
        self.assertEqual(credit_card_validator("53"), False)

    # This bug checks for just prefixs for Mastercards
    def test_bug93(self):
        self.assertEqual(credit_card_validator("54"), False)

    # This bug checks for just prefixs for Mastercards
    def test_bug94(self):
        self.assertEqual(credit_card_validator("55"), False)

    # This bug checks for just prefixs for Mastercards
    def test_bug95(self):
        self.assertEqual(credit_card_validator("2221"), False)

    # This bug checks for just prefixs for Mastercards
    def test_bug96(self):
        self.assertEqual(credit_card_validator("2720"), False)

    # This bug checks for just prefixs for Amex
    def test_bug97(self):
        self.assertEqual(credit_card_validator("34"), False)

    # This bug checks for just prefixs for Amex
    def test_bug97(self):
        self.assertEqual(credit_card_validator("37"), False)

    # This bug checks for just prefixs for Amex
    def test_bug98(self):
        self.assertEqual(credit_card_validator("42"), False)


if __name__ == "__main__":
    unittest.main()
