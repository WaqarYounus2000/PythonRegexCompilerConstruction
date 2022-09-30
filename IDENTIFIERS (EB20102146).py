
import re


def IntegerFunction(test_string=""):
    integerRegex = 'int\s+([a-z|A-Z|_][a-z|A-Z|0-9|_]*)\s*=\s*([^|-|+]([0-9]+))'
    result = re.fullmatch(integerRegex, test_string)
    
    if result:
      print("Valid Identifiers.")
      print(result)
    else:
      print("Invalid Identifiers")

def FloatFunction(test_string=""):
    floatRegex = 'float\s+([a-z|A-Z|_][a-z|A-Z|0-9|_]*)\s*=\s*([-|+|^]*)([0-9]*)\.([0-9]+)'  
    result = re.fullmatch(floatRegex, test_string)
    
    if result:
      print(result)
      print("Valid Identifiers.")
    else:
      print("Invalid Identifiers")


# IntegerFunction("int my_variableIntg = 2154")
FloatFunction("float _0my1_variable1float = 2.547")