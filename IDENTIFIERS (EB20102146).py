
import re

# pattern = '(int)\s(_|[a-z]*)[0-9]*'


integerRegex = 'int\s+([a-z|A-Z|_][a-z|A-Z|0-9|_]*)\s*=\s*[-|+]([0-9]+)'

test_string = 'int my_variable012 = -15478645.155'
result = re.fullmatch(integerRegex, test_string)



print("///////////////////////////////////////////////////////")
print(result)
if result:
  print("Valid Identifiers.")
  print("///////////////////////////////////////////////////////")
else:
  print("Invalid Identifiers")	
  print("///////////////////////////////////////////////////////")
