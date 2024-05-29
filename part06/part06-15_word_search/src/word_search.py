# Write your solution here
def find_words(search_term: str):
    found_words = []
    
    with open("words.txt") as file:
        for word in file:
            word = word.strip()
            if search_term.startswith("*"):
                if word.endswith(search_term[1:]):
                    found_words.append(word)
            elif search_term.endswith("*"):
                if word.startswith(search_term[:-1]):
                    found_words.append(word)
            elif "." in search_term:
                if len(word) == len(search_term):
                    match = True
                    for i in range(len(word)):
                        if search_term[i] != "." and word[i] != search_term[i]:
                            match = False
                            break
                    if match:
                        found_words.append(word)
            elif word == search_term:
                found_words.append(word)

    return found_words

if __name__ == "__main__":
    print(find_words("ca."))