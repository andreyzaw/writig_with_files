def read_cook_book(file_name):
# Creating cook book with a file
    cook_book = {}
    with open(file_name, encoding="utf-8") as f:
# Reading cook and count ingradient
        for line_file in f:
            cook = line_file.strip()
            count_ingr_str = f.readline().strip()
            count_ingr = int(count_ingr_str)
            recipe = []
# Forming a list of ingredients
            for i in range(count_ingr):
                ingradiet = {}
                str_ingradient = f.readline().strip().split(" | ")
                ingradiet["ingredient_name"] = str_ingradient[0]
                ingradiet["quantity"] = str_ingradient[1]
                ingradiet["measure"] = str_ingradient[2]
                recipe.append(ingradiet)
            cook_book.setdefault(cook, recipe)
            null_str = f.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
# Forming a list of ingredients for dishes
    cook_book = read_cook_book("recipes.txt")
    dict_ingradients = {}
    for dishe in dishes:
        for ingradient in cook_book[dishe]:
            count_ingradient = {}
            count_ingradient["measure"] = ingradient["measure"]
# Calculating count ingredients
            if ingradient["ingredient_name"] not in dict_ingradients.keys():
                count_ingradient["quantity"] = int(ingradient["quantity"]) * person_count
            else:
                count_ingradient["quantity"] += int(ingradient["quantity"]) * person_count
            dict_ingradients[ingradient["ingredient_name"]] = count_ingradient
    return dict_ingradients

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


