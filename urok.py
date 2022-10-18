a = ["a","b", "dkfj", 3, 4, 34]
str_list = []
len_
int_list = []

for i in a:
    if type(i) == str:
        str_list.append(i)
    elif type(i) == int:
        int_list.append(i)

print(sorted(int_list))

# with open("d.txt", "w") as f:
#     for i in a:
