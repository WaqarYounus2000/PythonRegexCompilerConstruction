
import re

pattern = 'int=(_|[a-z]*)[0-9]*'
test_string = 'int=waqar'
result = re.match(pattern, test_string)

if result:
  print("Valid Identifiers.")
else:
  print("Invalid Identifiers")	
