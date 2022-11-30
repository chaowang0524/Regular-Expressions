import re

# the match() method matches ONLY AT THE BEGINNING of the target string!
# if no match is found, it returns None
string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

result = re.match(r"\w{3}", string)
# "\w" represents any alphanumeric character, uppercase or lowercase and the underscore character
# but not the white spaces
# "\w{3}" looks for 3 consecutive alphanumeric characters
print(result)

result1 = re.match(r"\w{4}", string)
print(result1)
print(result.group(0))
