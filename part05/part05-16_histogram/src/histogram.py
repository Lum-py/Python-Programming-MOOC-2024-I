# Write your solution here
def histogram(string: str):
    stars = {}
    for char in string:
        if char not in stars:
            stars[char] = ""
        stars[char] += "*" 
    for key in stars:
        print(key, stars[key])   

if __name__ == "__main__":
    histogram("abba")