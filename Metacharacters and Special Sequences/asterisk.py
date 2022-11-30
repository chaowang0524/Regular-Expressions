import re

string = "ThE Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February ."

# `*` matches 0 or more repetitions of the preceding expression in a greedy way

result = re.findall(
    r"\d\d\d*", string
)  # `*` is looking for the preceding `\d` rather than `\d\d\d`
# `\d\d\d*` is matching 2 digits or three or more digits as `*` can match 0 repetition.
# With `findall`, the pattern should match ALL the numbers with two or more digits in the string.

print(result)

result_1 = re.findall(r"E.* ", string)
# the pattern is trying to match EVERYTHING starts from the capital letter E till there's no white space
# Thus the `*` is greedy
print(result_1)


result_2 = re.findall(r"E\w*", string)
print(result_2)
