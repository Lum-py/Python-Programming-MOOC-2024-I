# Write your solution here
string = input("Please type in a sentence: ")

i = 0

print(string[i])

while i < len(string) - 1:
    i += 1
    if string[i] != " ":
        continue
    print(string[i + 1])
