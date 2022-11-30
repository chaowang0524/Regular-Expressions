import openpyxl
import re

workbook = openpyxl.load_workbook(
    r"/Users/chaowang/Library/Mobile Documents/com~apple~CloudDocs/NLP/Python Tutorial/Regular Expressions/Filtering Employee Data/Employees.xlsx"
)

# print(workbook.sheetnames)

employee_sheet = workbook["EmployeeData"]
# print(employee_sheet.dimensions)


data = []

for row in employee_sheet.values:
    # unpack the row:
    a, b, c, d, e, f, g = row
    # fstring converts int to string and merge it into a new string
    data.append(f"{a},{b},{c},{d},{e},{f},{g}")
# print(data)
employees = "\n".join(data)
# print(type(employees))
print(employees)

# find all the names with salary over 24000 but less than 30000
result = re.findall(r"\d{1,},(.+?,.+?),.*,2[4-9]\d{3}", employees)
# print(result)

# find the names who are working in IT or Marketing with last name no more than 5 characters
result_1 = re.findall(r"\d+?,(.+?,\w{1,5}),(IT|Marketing),.*", employees)
# print(result_1)

# to split the names and their department:

# use list comprehension to get the first element (the name) in the list
names = [i[0] for i in result_1]
# print(names)

# Non-capturing group:
result_nocapture = result_1 = re.findall(
    r"\d+?,(.+?,\w{1,5}),(?:IT|Marketing),.*", employees
)
# print(result_nocapture)

# find all the names's first name's character starts from P to Z
# with their phone number starts with even numbers and ends with odd numbers
result_2 = re.findall(
    r"\d+?,([P-Z]\w+?,\w+?),.*,[2468]\d{8}[13579],.*,\d{5}", employees
)
# print(result_2)

# find the people and their phone number who are working in NY and in Sales.
result_3 = re.findall(r"\d+?,(\w+?,\w+?),Sales,(\d{1,}).+New York,.+", employees)
# print(f"This is a list of tuples: {result_3}")

# convert the tuple inside the list to string:
str_in_list = [" ".join(i) for i in result_3]  # put each tuple together by using `join`
# print(f"This is a list of strings: {str_in_list}")

# find all the people who are not based in Miami
result_4 = re.findall(r"\d{1,},(\w+,\w+),.+(?!Miami),.+", employees)
# print(result_4)

# find all the people work in HR or IT who make more than 30k but less than 60k
result_5 = re.findall(r"\d{1,},\w+,(\w+),\w{2},.+,[3-5]\d{4}", employees)
# print(result_5)


# find all the people whose phone number ends with two consecutive odd digits
result_6 = re.findall(r"\d{1,},(\w+,\w+),.+,\d{8}[13579][13579],.+", employees)
# print(result_6)

# find all the first names of the people who work in IT and last name starts with D
result_7 = re.findall(r"\d{1,},(\w+),D\w+,IT,.+", employees)
# print(result_7)

# find all the salaries of the people based in Chicago or LA and working in logistics
result_8 = re.findall(r"\d{1,},\w+,\w+,Logistics.+(?:Chicago|LA),(\d{5})", employees)
# print(result_8)

# find the people's last name and phone number who are located outside Las Vegas
result_9 = re.findall(r"\d{1,},(\w+,\w+),.+,(\d{10}),.+, (?!Las Vegas).+", employees)
# result_10 = re.findall(r"\d{1,},(\w+,\w+),.+,(\d{10}),.+(?!Las Vegas).+", employees)
print(result_9)
print()
# print(result_10)
