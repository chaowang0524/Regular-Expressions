l = []
a = "apple", 5
b, c = a

# print(b)

l.append(
    f"{b}, {c}"
)  # `append` will convert the tuple into a string and append to the list

# this is a list including string
print(l)

d = l[0]
