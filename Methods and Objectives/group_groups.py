import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

result = re.search(r".+\s(.+ex).+(\d\d\s.+).", string)

# '.' stands for any character except the new line character
# '+' stands for the proceeding character will repeat one or more times
# '\s' stands for the white space
#'(.+ex)' one or more characters ends with 'ex'


# so the above actually is looking for a word we don't care about
# plus a word ends with ex

# '.+' in between stands for the words between 'index' and the date

# RE for date "\d\d\s.+"
# '\d\d' for the two digits of the day
# '\s' for the white space in between
# '.+' to match the month

# the last '.' stands for the period mark,
# or can be any punctuations to offer the context for RE

result.groups()
# return a tuple 
# print(result.groups)
