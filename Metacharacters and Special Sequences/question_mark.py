import re

string = "The Euro STOXX 600 indEx, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

# `?` matches 0 OR 1 only repetitions of the preceding expression.

result = re.findall(r"\d\d\d?", string)
# matches all the numbers with TWO or THREE digits

print(result)

result_1 = re.findall(r"E.? ", string)
print(result_1)
# matches all the words with ONE or TWO letters/symbols have "E" before the white space

result_2 = re.findall(r"E\w?", string)
print(result_2)
# matches all the words/expressions with ONE or TWO alphanumeric letters after "E"
