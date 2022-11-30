import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

result = re.subn(r"[A-Z]{2,}", "INEDX", string)
# return the result as a tuple
# in the tuple, the first element is the replaced string,
# and the second is the amount of replacements have been made
print(result)

# use 'count' argument to fix the number of replacements
result_1 = re.subn(r"[A-Z]{2,}", "INEDX", string, 2)
print(result_1)
# the result will change accordingly
