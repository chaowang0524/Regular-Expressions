import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

# Adding an `?` after `*`, `+` or `?` will turn off the greedy behaviour,
# i.e to match as few as possible

# using the `*` pattern to match 0 or more
result = re.findall(r"\d\d\d*", string)
print(result)  # `*` will match numbers with at least TWO digits to infinite digits

# Adding the question mark to cancel the greedy behaviour
result_1 = re.findall(r"\d\d\d*?", string)
print(result_1)  # greedy behaviour cancelled, i.e 0 repetition
# Now only matches all the numbers with TWO digits
# or the first and second digits of the numbers with more digits

# using the `+` pattern to match 1 or more
result_2 = re.findall(r"\d\d\d+", string)
print(result_2)  # matches all the numbers with at least THREE digits

# Adding the question mark to cancel the greedy behaviour
result_2_cancel = re.findall(r"\d\d\d+?", string)
print(result_2_cancel)  # greedy behaviour cancelled

# using the `?` pattern to match 0 or 1
result_3 = re.findall(r"\d\d\d?", string)  # trying to match 1 repetititon
print(result_3)

# Adding the question mark to cancel the greedy behaviour
result_3_cancel = re.findall(r"\d\d\d??", string)
print(
    result_3_cancel
)  # greedy behaviour cancelled, only matches 0 repetition, i.e, two digits
