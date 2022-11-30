import re

filename = "web.txt"
with open(filename, "r", encoding="utf-8") as webfile:
    string = webfile.read()

# print(string)

# match the websites that have online shopping services:
result = re.findall(r".*(https:.*\.\w+).*\s+\d.* .*Online shopping.*", string)
# print(result)

# match the Site name of all the sites that are based in China and have a 3-letter URL extension.
result_1 = re.findall(r"(.*)\t\s*https:.*\.\w{3}.* China", string)
# print(result_1)

# match the URL and the country of all the Social networking sites whose domain name (exclude the extension) is less than 5 characters long
result_2 = re.findall(
    r".*(https://\w{1,5}\.\w*)\s*.*\s*Social networking\s*(\w*)", string
)
# print(result_2)

# match the Site name and the web protocal of ll the sites whose URLs contain subdomains:
result_3 = re.findall(r"(.*)\s(https)://\w\w*\.\w\w*\.\w\w*\s.*", string,re.M)
# result_3 = re.findall(r"(.+)\s+(http.*)://.+\..+\.\w{2,}\s.+", string)

# website class:
# http.*://.+\..+\.\w{2,}

print(result_3)

