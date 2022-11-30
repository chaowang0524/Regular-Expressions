import re

f = open(r"bookshelf.txt")
string = f.read()
# print(string)

# get the booktitle less than 25 characters
result = re.findall(r".+?;(.{1,25});.+?", string)
# print(result)

# get the author names if the author published the book after 2000
result_1 = re.findall(r"(.+?);.+?;20[0-9][0-9]", string)
# print(result_1)

# match all the book titles that end with the letter p
result_2 = re.findall(r".+?;(.*p);.+?", string)
# print(result_2)

# match all the author names whose last name starts with letter B
result_3 = re.findall(r"(.{2,} B.*);.+?;.+?", string)
# print(result_3)

# match all the books that have been published between 1980 and 1999
result_4 = re.findall(r".+?;(.+?);19[8-9][0-9]", string)
print(result_4)
