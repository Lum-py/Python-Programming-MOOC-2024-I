# Write your solution here
def anagrams(string_1, string_2):
    list_1 = []
    list_2 = []
    for char in string_1:
        list_1.append(char)
    for char in string_2:
        list_2.append(char)
    if sorted(list_1) == sorted(list_2):
        return True
    else:
        return False

if __name__ == "__main__":
    anagrams("tame", "meta") 