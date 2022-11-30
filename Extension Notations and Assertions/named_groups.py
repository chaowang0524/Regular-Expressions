import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."


result = re.search(r".+(\b.+ex\b).+(\b[A-Z]{4}\b).+(\d\d\s.+)\.", string)

# name the group: ?P<...>

result_named = re.search(
    r".+(?P<wordex>\b.+ex\b).+(?P<uppercase>\b[A-Z]{4}\b).+(?P<date>\d\d\s.+)\.", string
)
result_named.group("wordex")
result_named.group("uppercase")

result_named.group(1)  # numbers still work

result_dict = result_named.groupdict()  # make the groups into a dictionary
print(type(result_dict)) # it's a dictionary 

for key, values in result_dict.items():
    print(key, values, sep=":")
