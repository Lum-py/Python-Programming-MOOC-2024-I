# Write your solution here
s_1 = input("Please type in string 1: ")
s_2 = input("Please type in string 2: ")
x = "The strings are equally long"
if len(s_1) < len(s_2):
    x = s_2
elif len(s_1) > len(s_2):
    x = s_1

if len(s_1) == len(s_2):
    print(x)
else:
    print(f"{x} is longer")