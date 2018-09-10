import re
string="lksadhfklsjdahgfkjsdh98q345irfh893yi ue45798403t7 3874yr "
s=re.findall(r'\D',string)
print "".join(s)
st1="hash askjhshs asjdhaskhfa skfjahkfjha kjhakjsfhakj kajshfkajhf kjhdat lakjfhat kjdat lkdhf lkhfat"
h=re.findall(r'\b(\w+at)\b',st1)
print h
print "count",len(h)
