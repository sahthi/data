import re
str1 = "21ac63/91ft25"
op = [] 
op2 = []
str3 = re.findall(r"(\d.)",str1)
str4 = re.findall(r"\w.(\w.)\w.",str1)
op.append(str3)
op2.append(str4)
print op
print op2
