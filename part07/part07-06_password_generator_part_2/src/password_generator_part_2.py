# Write your solution here
from string import ascii_lowercase, digits
from random import choice

def generate_strong_password(length: int, dig: bool, special: bool):
    special_chars = "!?=-+()#"
    password = [choice(ascii_lowercase)]
    
    if dig:
        password.append(choice(digits))
    if special:
        password.append(choice(special_chars))
        
    for _ in range(length - len(password)):
        password.append(choice(ascii_lowercase))
    
    return ''.join(password)

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(5, False, False))