#SWEET POTATO SOUP

ingredients = {"olive oil",
               "onion",
               "sweet potato",
               "apple",
               "garlic",
               "ginger",
               "coriander",
               "paprika",
               "apple cider vinegar",
               "milk",
               "broth"}

ingredient = input("Search for an ingredient: ")

if ingredient in ingredients:
    print(f"{ingredient} is an ingredient in sweet potato soup.")
else:
    print(f"{ingredient} is not an ingredient in sweet potato soup.")
