x = input("Enter Values Seperated By Spaces: ")

x_list = x.split()

x_distinct = len(set(x_list))

print("Number Of Distinct Elements: ", x_distinct)
