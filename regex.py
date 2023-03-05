import re
L = ["python practice", "workearly training"]
#the expression w+ and \W will match the words starting
#with letter 'p' and thereafter anything which is not
#started with 'p' will not be identified
for elem in L:
    z = re.match("(p\w+)\W(p\w+)", elem)
    if z:print(z.groups())

# re.search():takes a PATTERN and a TEXT to scan from
# and returns a match object when the pattern is found
patterns = ['Learning Python', 'workearly']
text = 'Learning Python now'
for pattern in patterns:
      print('Looking for "%s" in "%s" --> '%(pattern,text))
      if re.search(pattern, text):
          print("match found")
      else:
          print("No match")

#===re.findall() : a list of email addresses ...the findall to get all emails
#from the list
em = 'john@gmail.com,angie123@outlook.com'
emails = re.findall(r'[\w -]+@[\w -]+', em)
for email in emails:
    print(email)

#re.sub() : turns a string eg (210)-3450987 into 2103450987
#using the pattern \D --> matches any char which is not digit
#re.sub (pattern, repl, string, count = 0, flags = 0)

phone_num = '(210)-345-0987'
pattern = '\D'
outcome = re.sub(pattern,'',phone_num)
print(outcome)

#re.compile() string_pattern finds two consecutive digits in birthdate
#compiled to re.Pattern object
#find all matches in birthdate and print the numbers
birthdate = "John's birthdate is on 18/02/93"
string_pattern = r"\d{2}"
regex_pattern = re.compile(string_pattern)
outcome = regex_pattern.findall(birthdate)
print(outcome)

#re.split(): split each word using \s, parse each word in the string
#seperately
print(re.split(r'\s', 'the process of splitting is explained here in detail'))
