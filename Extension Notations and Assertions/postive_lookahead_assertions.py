import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

# Positive lookahead assertions
# Negative lookahead assertions
# Positive lookbehind assertions
# Negative lookbehind assertions

# syntax (?=...)
# provides a condition where the match should be performed

# for match a certain pattern
# if and only if the pattern is followed by the pattern after the equal sign
result = re.findall(r"[A-Z]{5}\s(?=[0-9]{3})", string)
print(result)

result_1 = re.findall(r"([A-Z]{5})\s(?=[0-9]{3})", string)
print(result_1)

result_euro = re.findall(r"Euro(?=[a-z]+)", string)
print(result_euro)
