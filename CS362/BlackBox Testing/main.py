def digits_of(number):
  return [int(i) for i in str(number)]

def checksum_luhn(card_number):
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2] #right side
    even_digits = digits[-2::-2] #right side
    total = sum(odd_digits)
    for digit in even_digits:
      total += sum(digits_of(2 * digit))
    return total % 10

def is_valid(card_number):
    return checksum_luhn(card_number) == 0

def main():
    choice = 'y'
    while choice == 'y' or choice == 'Y':
        try:
            card_number = input("\nEnter the credit card number: ")             #line below checks for lengths 15-16 which is length of visa, master, amex
            if is_valid(card_number) and 15 <=len(card_number) and len(card_number) <= 16:
                print("\nThis is a valid credit card number.")
                if card_number[0:1] = "4":                                      #check for if its a visa card by prefix
                    print("Type: Visa card.")
                elif card_number[0:2] == "34" or card_number[0:2] == "37":      #checks prefix to see if its an AMEX
                    print("Type: American Express (AMEX) card")                 #THIS NEEDS FIXING ITS NOT CORRECT CHECK THE RANGE
                elif card_number[0:2] == "51" or card_number[0:2] == "55" or card_number[0:2] == "2221" or card_number[0:2] == "2720"]:
                    print("Type: Mastercard.")
            else:
                print("\nInvalid! Credit card number.")

            choice = input("\nWant to check again (y/n): ")
        except ValueError:
                print("\nErr! Credit card number should be numeric. Try again.")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
            
if __name__ == '__main__':
	main()
