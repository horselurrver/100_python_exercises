import re
"""
Assuming that we have some email addresses in the "username@companyname.com" format,
please write program to print the company name of a given email address.
Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:

john@google.com
Then, the output of the program should be:

google
"""
def getCompany(email):
    pattern = '\w+@(\w+).com'
    prog = re.match(pattern, email)
    print(prog.group(1))

getCompany('john@google.com')
