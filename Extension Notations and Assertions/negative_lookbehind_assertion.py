import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

# (?<!...)


# looking for a number that is not preceded by a space
result = re.findall(r"(?<!\s)\d{1,}", string)
print(result)

# looking for an "x" or "X" that is not preceded nor followed by another "X" or "x"

result_x = re.findall(r"(?<!x)x(?!x)", string, re.I)  # `re.I` for case insensitive
print(result_x)
