import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

# re.sub(pattern, replacement, string, count, flags)

result = re.sub(r"[A-Z]{2,}", "INDEX", string)
# [A-Z]: character class - any character from A-Z in uppercase exclusively
# [a-z]: character class - any character from A-Z in lowercase exclusively
# {2, }: the preceeding character to be repeated at least two times (above 2)
print(result)

result_1 = re.sub(
    r"[A-Z]{2,}", "INDEX", string, 2
)  # only replace the first two matches
print(result_1)
