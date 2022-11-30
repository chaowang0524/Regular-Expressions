import re

filename = "logs.txt"
with open(filename, "r", encoding="utf8") as logfile:
    string = logfile.read()

# print(string)

# match all the source that cause 'Critical' failure between 2020 Jan 11-16
result = re.findall(r"Critical 1/1[1-6]/2020.* (.*) \d\d .*", string)
# print(result)

# match the Source substring of all the log entries that were generated after 12PM and before 4PM
result_1 = re.findall(r".* .* [12|1|2|3]:\d\d:\d\d \w\w (.*) \d{1,} .*\.", string)
# print(result_1)

# match the Date of all the log entries that have TPM as the Source of the log entries
result_2 = re.findall(r".* (.*) .* [AP]M TPM .*", string)
# print(result_2)

# match the Date and Time of all the log entries that have been generated between 24 and 27 of January 2020 and between 8:00:00 and 8:59:59
result_3 = re.findall(r"\w* (1/2[4-7]/2020 8:[0-5][0-9]:[0-5][0-9]) AM .*",string)
print(result_3)
