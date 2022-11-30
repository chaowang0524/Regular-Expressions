import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

result = re.findall(r"the", string, re.I)
# 'I' for case insensitive
# print(result)


string2 = "Hello\nPython"
result_2 = re.search(r".+", string2)
print(result_2)


result_3 = re.search(r".+", string2, re.S)
# 'S' enables '.' to include the newline character
print(result_3)

result_3 = re.search(r".+\s(.+ex).+(\d\d\s.+).", string)

result_4 = re.search(
    r""".+\s #Beginning of the string
                    (.+ex) # Searching for index
                    .+ #Middle of the string
                    (\d\d\s.+). #Date at the end""",
    string,
    re.X,
)
print(result_4)
print(result_4.groups())
