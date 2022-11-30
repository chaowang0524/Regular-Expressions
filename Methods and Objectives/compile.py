import re

# help(re)
# dir(re)

# path = 'C:\\Users\\tasks\\new'
# path = r'C:\Users\tasks\new' # raw string
# print(path)

s = r"\d{4}"
"""
 '\d':any digit from 0 - 9; 
{4}: the proceeding digit occurs 4 times
so it will match "1234", "3416", "8350" etc any four consecutive digits in the target string.

"""

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

# print(type(s))
t = re.compile(s)  # easy to use the same pattern over and over again
# print(type(t))
result = re.findall(t, string)
print(result)
