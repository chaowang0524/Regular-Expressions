import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

# result = string.split()
# print(result)

result = re.split(r"\s", string)
# '\s' matches the regular space, as well as \n,\t and \r
print(result)
# can also use `\W+` to split with nonalphanumeric characters





result_1 = re.split(r"\s{3}", string)
# print(result_1)
