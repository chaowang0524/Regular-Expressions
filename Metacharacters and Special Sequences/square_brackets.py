import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

# `[]` represents sets of characters and character classes


# try to match "w", "x", "k" or "q"
result = re.findall(r"[wxkq]", string)
print(result)

# try to match letter from a to d (a, b, c, or d)
result_1 = re.findall(r"[a-d]", string)
print(result_1)

# try to match letter in uppercase from S to W
result_2 = re.findall(r"[S-W]", string)
print(result_2)

# try to match digits from 1 to 5
result_3 = re.findall(r"[1-5]", string)
print(result_3)

# try to match two consecutive letters, the first letter from a to f, the second from c to w
result_two_letters = re.findall(r"[a-f][c-w]", string)
print(result_two_letters)

# try to match two consecutive digits, the first digits from 0 to 5, the second digits from 7 to 9
result_two_digits = re.findall(r"[0-5][7-9]", string)
print(result_two_digits)

# find a letter follow a digit in the string
result_letter_after_digit = re.findall(r"[0-9][a-z]", string)
print(result_letter_after_digit)

# try to match any character except "x"
result_no_x = re.findall(r"[^x]", string)  # `^` is negation
print(result_no_x)
print("x" in result_no_x)


# special characters will lose their power inside the square brackets such as `*`, `.`, `+` and `?`
result_power = re.findall(r"(.+?)", string)
print(result_power)

result_no_power = re.findall(
    r"[(.+?)]", string
)  # searching for the actual symbols (`.+?`)
print(result_no_power)
