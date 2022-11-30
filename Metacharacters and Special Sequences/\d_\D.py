import re

string = "ThE Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February ."

# `\d` equivalents to [0-9]

result = re.findall(r"(\d)[a-z]", string)

print(result)

# `\D` matches any non-digit character, equivalent to [^0-9]

result_non_digit = re.findall(r"\W\D\W", string)
print(result_non_digit)
