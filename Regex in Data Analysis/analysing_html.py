import pandas, lxml, re

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

d = pandas.read_html(url)[1]

# show the dataframe
# d

# convert the element in the dataframe to string: `to_string()`
data = d.to_string()

# data

# find all the object type that are mutable
scenario_1 = re.findall(r"\n\d{1,}\s{1,}(.+?)\s{1,}mutable.+", data)
# print(scenario_1)

# find all the types whose syntax examples contains `{}`
scenario_2 = re.findall(r"\n\d{1,}\s*(\w{1,}).*\{.*\}", data)
# `\{.*\}` stands for the `{}` can be either connected or not connected
# print(scenario_2)

# find all the description of the data type whose name are not longer than 4 characters
scenario_3 = re.findall(r"\n\d{1,}\s+\w{1,4}\s+\w{2,}\s+(.+?)\s{2,}.+", data)
# print(len(scenario_3))

# find the first ten characters of the description of the data type
# whose ID is odd number
scenario_4 = re.findall(
    r"[13579]{1,2}\s+.{3,}\s+?\w+?\s+?([A-Z].{9}).+\s{2,}.+",
    data,
)
# print(scenario_4)
# odd number class: `\d*[13579]`

# find all the data types with their syntax examples contain at least one float number
scenario_5 = re.findall(r"\n\d{1,}\s{1,}(\w+?)\s{1,}.*\d{1,}\.\d{1,}", data)
# scenario_5 = re.findall(r"\n\d{1,}\s{1,}(\w+?)\s{1,}.*\d{1,}\.\d{1,}",data)
# print(scenario_5)

# find all the the immutable data types whose names are at least 7 characters.
scenario_6 = re.findall(r"\d{1,}\s{1,}(\w{7,})\s*immutable", data)
# print(scenario_6)
# print()
# result = re.findall(r"\d{1,}\s{1,}(\w{7,})\s{1,}immutable", data)
# print(result)

# find all the descriptions for all immutable data types whose names are no more than 3 characters.
scenario_7 = re.findall(r"\d{1,}\s{1,}\w{1,3}\s+?immutable\s{1,}(.+?)\s{2,}", data)
# print(scenario_7)
# result = re.findall(r"\d{1,}\s{1,}\w{1,3}\s{1,}immutable\s{1,}(.+?)\s{2,}", data)
# print(result)

# find all the data types whose ID is an even number(including 0)
scenario_8 = re.findall(r"\n\d*[02468]\s{1,}(.+?)\s{1,}\w{2,}.*", data)
# print(scenario_8)

# findall the data types whose IDs are made of only 1 digit
# and contain at least 3 consecutive digits somewhere on their repective lines
scenario_9 = re.findall(r"\n[0-9]\s{1,}(\w+)\s{1,}.*(?=[\d]{3,}).*", data)
# print(scenario_9)

# find all the immutable data types that do not contain a digit in the Description and Syntax Example columns
scenario_10 = re.findall(r"\d{1,}\s{1,}(\w+)\s{1,}immutable\s{1,}(?!.*\d{1,}).*", data)
print(scenario_10)

# `Do not contain a digit`  class (?!.*\d{1,})
