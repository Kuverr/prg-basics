###
# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file,'r') as file:
    content = file.read
    email = content

# regular expression pattern
# for amounts
pattern = '€\d+'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)

# calculate the total purchases
sum = 0
for amount in amounts:
   sum += amount

# print result
print(sum)