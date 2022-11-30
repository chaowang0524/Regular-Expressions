import re

# f = open(r"phone.txt")
# string = f.read()
# print(string)

# open the file in python
filename = "phone.txt"
with open(filename, encoding="utf-8") as file:
    string = file.read()
    # print(string)

# get the person's last name and phone number whose area code ends with 0
result = re.findall(r".+ (.+)\t\(\d\d[0]\) (.+)", string)
# print(result)

# get the area code of the person whose phone number ends with 7
result_1 = re.findall(r".+\t(.{5}) .{7}[7]", string)
# print(result_1)

# get all the persons (first and last name) whose phone number starts with an odd digit
result_2 = re.findall(r"(.+)\t.{5}\s[13579].{7}", string)
# print(result_2)

# get all the persons (first name) whose area code is a number less than 300
result_3 = re.findall(r"(.+) .+\t\([0-2]\d\d\).+", string)
# print(result_3)

# get all the persons (first name) whose last name ends in a vowel and phone number ends in either 0,7 or 9
result_4 = re.findall(r"(.+) .+[aeiou]\t.{5}\s.{7}[079]",string, re.I)
print(result_4)
