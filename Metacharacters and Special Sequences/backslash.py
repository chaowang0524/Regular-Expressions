import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

# `\`signals a special sequence
# escaping and matching a symbol with special meaning in regex syntax

# `\`signals a special sequence
result = re.findall(r"\d", string)

print(result)


# escaping and matching a symbol with special meaning in regex syntax
result_1 = re.findall(
    r"\.", string
)  # escapes the regex syntax to match the actual symbol '.'
print(result_1)
