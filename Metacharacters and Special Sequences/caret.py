import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

string_1 = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. \nThe panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."
result = re.search(r"^\w{3}", string)

# '^' matches the beginning of the string, \w for three times.

# `search` only returns the first result 

print(result)

print(string_1)

result_1 = re.findall(r"^\w{3}", string_1, re.M) # `findall` returns all the results
print(result_1)

