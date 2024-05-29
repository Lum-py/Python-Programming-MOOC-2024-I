# Write your solution here
l_1 = input("1st letter: ")
l_2 = input("2nd letter: ")
l_3 = input("3rd letter: ")

if l_1 <= l_2 <= l_3 or l_3 <= l_2 <= l_1:
    middle = l_2
elif l_2 <= l_1 <= l_3 or l_3 <= l_1 <= l_2:
    middle = l_1
else:
    middle =  l_3
   

print(f"The letter in the middle is {middle}")           