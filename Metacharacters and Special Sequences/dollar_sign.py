import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998.\nThe panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

# `$` matches the end of the line or end the string (befor each new line character)

result = re.findall(r"\s(\w{2,})\W$", string, re.M)

# `\s` the proceeding white space
# `(\w{2,})` the word
# `\W$` the last punctuation
# `\W` matches any non-alphanumeric character, the oppsite of \w (dedicate for punctuations)

result_1 = re.findall(r"\s(\w{2,})\W$", string, re.M)
print(result_1)
