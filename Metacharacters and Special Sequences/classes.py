import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."


result_digits = re.findall(r"[0-9]", string)  # overall character class for digit
print(result_digits)

result_letters = re.findall(
    r"[a-zA-Z]", string
)  # overall character class for letters, case insensitive
print(result_letters)

result_non_letters = re.findall(r"[^0-9]", string)  # non digit character in the string
print(result_non_letters)

result_white_space = re.findall(
    r"[ \n\t\r\f\v]", string
)  # all white space character in the string
print(result_white_space)
# print(len(result_white_space))
# print(string.count(" "))

result_non_white_space = re.findall(
    r"[^ \n\t\r\f\v]", string
)  # any non white space character in the string
print(result_non_white_space)

result_alphanumeric = re.findall(
    r"[a-zA-Z0-9_]", string
)  # all alphabetic characters in the string
print(result_alphanumeric)

result_non_alphanumeric = re.findall(
    r"[^a-zA-Z0-9_]", string
)  # all non alphabetic characters in the string
print(result_non_alphanumeric)