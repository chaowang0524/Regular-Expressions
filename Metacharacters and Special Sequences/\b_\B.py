import re

string = "The Euro STOXX 600 index, which tracks all stock markets across ,Euro! pe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

# `\b` matches the non-alphanumeric characters that border the word

result = re.findall(
    r"\b\w{10,}\b", string
)  # try to match all the standalone words with at least 10 letters

print(result)

result_euro = re.findall(r"\bEuro\b", string)
print(result_euro)

# `\B` matches the alphanumeric characters that border the word

result_B = re.findall(r"\Brack\B", string)
print(result_B)
