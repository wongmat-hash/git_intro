def check_pwd(string):
    symbollib = '~`!@#$%^&*()_+-='                                                #possible combination of characters
    numSym = 0                                                                  #counter for symbols
    numlowercase = 0                                                            #counter for lower case
    numuppercase = 0                                                            #counter for upper
    numNumbers = 0                                                              #counter for numbers

    if len(string) < 8 or len(string) > 20:                                     #first criteria between 8 - 20 inclusive
        return False                                                            #if its not inclusive 8 - 20 breaks out
    for x in string:                                                            #loops through checks for upper
        if x.isupper():
            numuppercase += 1                                                   #adds to counter
    if numuppercase == 0:                                                       #if none found
        return False                                                            #breaks out
    for x in string:
        if x.islower():                                                         #checks for lowers
            numlowercase += 1                                                   #adds to counter
    if numlowercase == 0:                                                       #otherwise break out again
        return False
    for x in string:                                                            #checks for digit
        if x.isdigit():
            numNumbers += 1                                                     #adds to counter
    if numNumbers == 0:                                                         #otherwise breaks out again
        return False
    for x in string:                                                            #loops through string
        for y in symbollib:                                                       #loops through valid symbollib
            if x == y:
                numSym += 1                                                     #checks and adds
    if numSym == 0:                                                             #otherwise breaks out
        return False
    return True
