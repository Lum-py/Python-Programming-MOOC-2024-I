# Write your solution here
x = input("Please type in a string: ")
i_1 = x[1]
i_2 = x[-2]

if i_1 != i_2:
    print("The second and the second to last characters are different")
else:
    print(f"The second and the second to last characters are {i_1}")