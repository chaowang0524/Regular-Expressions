import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

# re.search(pattern,string,flags)

result = re.search(r"\d{3}", string)  # search 3 consecutive digits in the 'string'
# the search() method only returns the FIRST occurrence of the pattern in the target string
# if no match is found, the search() method returns None
result1 = re.search(r"\d{10}", string)
print(result1)
