import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998.\nThe panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

# `\A` matches the beginning of the string

# using `^` to match the beginning of the every new line
result = re.findall(r"^([A-Z].*?)\s", string, re.M)
print(result)

# using `\A` to match the beginning of the string regardless of the newline
result_a = re.findall(r"\A([A-Z].*?)\s", string, re.M)
print(result_a)

# `\Z` matches the end of the string regardless of the multiline
result_z = re.findall(
    r"\W\Z", string, re.M
)  # `\W` matches the non-alphanumeric characters
print(result_z)

# using `$` to match the end of the string before the newline

result_end = re.findall(r"\W$", string, re.M)
print(result_end)
