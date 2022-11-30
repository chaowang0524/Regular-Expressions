import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

# tries to match the first pattern from left to rigth till it finds match (`A | B | C`), not greedy

result = re.search(r"\d{3}|\d{4}|\b[A-Z]{4}\b", string)
# first, it will try to find the first three-digit number in the string
# if not, it will try to find the first four-digit number in the string
# if not, it will try to find the first four-uppercase-letter word in the string
print(result)  # find the first three-digit number in the string: 600
