'''
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

# print(number_grid[0][0])    # the output will be 1
# print(number_grid[2][1])    # the output will be 8



for row in number_grid:
    for col in row:
        print(col , end=(" ,"))

'''
# people =\
# [
# ["Rafi",22],
# ["Alif",20],
# ["Mahabub",27],
# ["Lamia",18],
# ["Neha",16]
# ]

# people.append(list())
# print(people)

# #version 01 
# for p in  people:
#     print(p[0], "is", p[1], "years old.\n\n")

# #version 02
# for name ,age in people:
#     print(name, "is", "years old")

a_2d_list = [[1, 2],[3, 4],                     #there have 0,1,2,3 index
             [5, 6],[7, 8]
]

a_nested_list = a_2d_list[2]
a_nested_list.append(5)
# append 5 to second nested list
print(a_2d_list)


b_2d_list = [[1, 2], [3, 4]]

b_2d_list.append([5, 6])
# new list can have any length
print(b_2d_list)

if 2 in a_2d_list[1]:
    print("yes")
else:
    print("No")
