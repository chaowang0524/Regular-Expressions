import re

# The fullmatch() method returns a result
# only if the pattern matches the ENTIRE target string

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

print(len(string))

result = re.fullmatch(r".{285}", string)
# the '.' matches any character except the new line character (\n)

print(result)
