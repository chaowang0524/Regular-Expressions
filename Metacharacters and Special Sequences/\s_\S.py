import re

string = "ThE Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. \nThe panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February ."

# `\s` matches white space characters: \t,\n,\r,\f,\v and the space

# equivalent to [ \n\t\f\r\v]

result = re.findall(r"\s", string)
print(result)

# `\S` matches any non-white space characters

result_eight = re.findall(r"\S{8,}", string)
print(result_eight)
