import re

filename = "stocks.txt"

with open(filename, "r", encoding="utf-8") as stockfile:
    string = stockfile.read()

# print(string)

# find the company with its revenue that is less than 50B
result = re.findall(r"(.+?)\s+\d\d*\.\d\d*M\s+([1-4]\d\.\d\d*B).*", string)
# print(result)

# find the company names whose revenue is between 10B and 30B and P/E ratio is between 10 and 15
result_1 = re.findall(
    r"(.+?)\s+\d\d*\.\d\d*M\s+[1-3][0-9]\.\d+B\s+1[0-4]\.\d+.*", string
)
# print(result_1)  # Tesla

# find the company names whose average volume is less than 10M
result_2 = re.findall(r"(.+?)\s+\d\.\d+M.*", string)
# print(result_2)

# find the company names whose average volume starts with an even digit and their P/E ratio ends with an odd digit

result_3 = re.findall(r"(.+?)\s+[2468][0-9]*\.[0-9]+M\s+[0-9]+\.[0-9]+B\s+[0-9]+\.[0-9]+?[13579]", string)
print(result_3)

result_4 = re.findall(r"(.+?)\s+[2468][0-9]*\.[0-9]+M\s+[0-9]+\.[0-9]+B\s+[0-9]+\.[0-9][13579]", string)
print(result_4)