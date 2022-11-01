# this needs to contain the password checking function
# this will contain the tests you wrote during the TDD process with main function
# notes
# Sample Workflow

# Read specification
# Write first test and run it to ensure it fails
# Commit changes, "Wrote test1 to see if an empty string is rejected correctly"
# Write the bare minimum implementation to get the test to pass
# Run test to see if it passes
# Commit changes, "Made check_pwd return False when the length is 0, it passed"
# Write second test...

def check_pwd(string):
    if len(string) == 0:
        return False
    else:
        return True
# requirements for True
# Must be between 8 and 20 characters (inclusive)
# Must contain at least one lowercase letter
# Must contain at least one uppercase letter
# Must contain at least one digit
# Must contain at least one symbol from: ~`!@#$%^&*()_+-= (copy and paste to avoid missing characters) These are the only permitted symbols
