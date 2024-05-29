# Write your solution here
#import string_helper
def change_case(orig_string: str):
    return_string = ""
    for char in orig_string:
        if char.isupper():
            return_string += char.lower()
        else:
            return_string += char.upper()
    return return_string

def split_in_half(orig_string: str):
    half = len(orig_string) // 2
    return orig_string[:half], orig_string[half:]

def remove_special_characters(orig_string: str):
    special_characters = '!"§$%&/()=?`´,.;:<>|+-*/#_¤^°'

    return_string = ""
    for char in orig_string:
        if char in special_characters:
            continue
        return_string += char
    return return_string
    
if __name__ == "__main__":
    import string_helper
    my_string = "Well hello there!"

    print(string_helper.change_case(my_string))

    p1, p2 = string_helper.split_in_half(my_string)

    print(p1)
    print(p2)

    m2 = string_helper.remove_special_characters("This is a test, lets see how it goes!!!11!")
    print(m2)