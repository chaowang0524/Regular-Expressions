import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

# match the pattern if and only if it does not follow the condition


result = re.findall(r"\d(?![5-9]|\D)", string) 
# will only match if it is not followed by a digit nor a non-digit character
print(result)

result_words = re.findall(r'\b\w+\b(?!\s)', string)
print(result_words)
