from credit_card_validator import credit_card_validator
import random
import string
import unittest


# visa prefix 4 length 16 and luhn validated yes
class TestCase(unittest.TestCase):

    # visa prefix 4 length 16 and luhn validated yes THIS WORKS VALIDATING IN GRADASCOPE AS TEST_BUG1
    def test1(self):
        tests_to_generate = 158333
        for i in range(tests_to_generate):
            expected = True
            # DEFINE THE EDGE CASES FOR LENGTHS
            edge_cases = [15, 16, 17, 18]
            odds = random.randint(0, 1)
            if odds == 1:
                length = random.choice(edge_cases)
            else:
                # Random length of string 16 length
                length = random.randint(0, 16)
            # Prefix length
            prefix_length = random.randint(0, length)
            # rest of the card numbers
            rest_numbers = random.randint(0, length - prefix_length)
            # Determine final length of length
            length = prefix_length + rest_numbers
            # set the expected result based on specification
            # THIS CRITERIA IS FOR LENGTH
            if length != 16:
                expected = False
            # THIS CRITERIA IS FOR PREFIX
            if prefix_length != 1:
                expected = False
            # pass this all into the self gen_pass with 3 values
            c_number = self.gen_pass(length, prefix_length, rest_numbers)
            # luhn validation store it as a % 10 value
            if luhn_checksum(c_number) != 0:
                expected = False
            # generate error if it does not meet criteria
            if credit_card_validator(c_number) != expected:
                print("Error: {} should be {}".format(c_number, expected))

    # mastercard prefix 51-55 and 2221-2720 length 16 luhn validated yes  THIS ENTIRE THING ONLY JUST VALIDATES BUG1
    def test2(self):
        tests_to_generate = 158333
        for i in range(tests_to_generate):
            expected = True
            # define the edge cases here for lengths
            edge_cases = [15, 16, 17, 18]
            odds = random.randint(0, 1)
            if odds == 1:
                length = random.choice(edge_cases)
            else:
                # Random Length of string 16 is chosen
                length = random.randint(0, 16)
            # prefix length
            prefix_length = random.randint(0, length)
            # rest of the card numbers
            rest_numbers = random.randint(0, length - prefix_length)
            # determine the final length
            length = prefix_length + rest_numbers
            # set the expected results based on sepcs
            # This is criteria for length
            if length != 16:
                expected = False
            # this is the spec for prefix for 2 and 4 values
            if (prefix_length != 2) or (prefix_length != 4):
                expected = False
            # pass all this into gen_pass with 3 values
            c_numbers = self.gen_pass(length, prefix_length, rest_numbers)
            # luhn_checksum validator
            if luhn_checksum(c_numbers) != 0:
                expected = False
            # generate error message if it doesnt meet
            if credit_card_validator(c_numbers) != expected:
                print("Error: {} should be {}".format(c_numbers, expected))

    # AMEX prefix prefixes 34-37 length 15 luhn validated yes   THIS ENTIRE THING ONLY JUST VALIDATES BUG1
    def test3(self):
        tests_to_generate = 158333
        for i in range(tests_to_generate):
            expected = True
            # define the edge cases here for lengths
            edge_cases = [14, 15, 16]
            odds = random.randint(0, 1)
            if odds == 1:
                length = random.choice(edge_cases)
            else:
                # Random Length of string 16 is chosen
                length = random.randint(0, 15)
            # prefix length
            prefix_length = random.randint(0, length)
            # rest of the card numbers
            rest_numbers = random.randint(0, length - prefix_length)
            # determine the final length
            length = prefix_length + rest_numbers
            # set the expected results based on sepcs
            # This is criteria for length
            if length != 15:
                expected = False
            # this is the spec for prefix for 2 and 4 values
            if prefix_length != 2:
                expected = False
            # pass all this into gen_pass with 3 values
            c_numbers = self.gen_pass(length, prefix_length, rest_numbers)
            # luhn_checksum validator
            if luhn_checksum(c_numbers) != 0:
                expected = False
            # generate error message if it doesnt meet
            if credit_card_validator(c_numbers) != expected:
                print("Error: {} should be {}".format(c_numbers, expected))

    def gen_pass(self, length, prefix_length, rest_numbers):
        # prefix length
        p_length = string.digits
        # rest numbers
        r_numbers = string.digits
        all_pos = p_length + r_numbers

        pwd = ""
        pwd = pwd + "".join(random.choice(p_length) for i in range(prefix_length))
        pwd = pwd + "".join(random.choice(r_numbers) for i in range(rest_numbers))
        pwd = pwd + "".join(random.choice(all_pos) for i in range(length - len(pwd)))

        return "".join(random.sample(pwd, len(pwd)))


# WORK CITED FOR Luhns: https://stackoverflow.com/questions/21079439/implementation-of-luhn-formula
def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10


if __name__ == "__main__":
    unittest.main()
