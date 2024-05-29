# Write your solution here
def read_recipes(filename: str):
    with open(filename) as file:
        return file.read().lower().split("\n\n")
    
def search_by_name(filename: str, word: str):
    found_recipes = []
    recipelist = read_recipes(filename)

    for recipe in recipelist:
        lines = recipe.strip().split("\n")
        recipe_name = lines[0].lower()
        if word.lower() in recipe_name:
            found_recipes.append(recipe_name.capitalize())
    
    return found_recipes

def search_by_time(filename: str, time: int):
    found_recipes = []
    recipelist = read_recipes(filename)

    for recipe in recipelist:
        lines = recipe.strip().split("\n")
        recipe_name = lines[0]
        recipe_time = int(lines[1])
        if recipe_time <= time:
            found_recipes.append(f"{recipe_name.capitalize()}, preparation time {recipe_time} min")       
    return found_recipes

def search_by_ingredient(filename: str, ingredient: str):
    found_recipes = []
    recipelist = read_recipes(filename)
    for recipe in recipelist:
        lines = recipe.strip().split("\n")
        recipe_name = lines[0]
        recipe_time = int(lines[1])
        ingredients = lines[2:]
        
        for search in ingredients:
            if search == ingredient:
                found_recipes.append(f"{recipe_name.capitalize()}, preparation time {recipe_time} min")
    return found_recipes




if __name__ == "__main__":
    # found_recipes = search_by_name("recipes2.txt", "oat")
    # for recipe in found_recipes:
    #     print(recipe)
    # found_recipes = search_by_time("recipes1.txt", 20)

    # for recipe in found_recipes:
    #     print(recipe)
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)