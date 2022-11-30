import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

# `+` matches ONE or More times of repetitions of the proceeding expression. Also GREEDY.


result = re.findall(r"\d\d\d+", string)
print(result)
# Find all the numbers with at least THREE digits

result_1 = re.findall(r"E.+ ", string)
print(result_1)

result_2 = re.findall(r"E\w+", string)
print(result_2)