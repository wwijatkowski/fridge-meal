import json

# choice_to_eat = input('what you want to eat? ')
choice_to_eat = 'scrambled eggs'
# Load actual ingredients file list.
data_ingredients = open('ingredients.json', "r")
data_ingredients_json = json.load(data_ingredients)
dict_of_ingredients_and_values = data_ingredients_json[list(data_ingredients_json.keys())[0]]
data_ingredients.close()

# Load chosen meal.

data_meals = open('meals.json').read()
data_meals_json = json.loads(data_meals)
dict_of_meals_with_ingredients = data_meals_json[list(data_meals_json.keys())[0]]
list_of_meals = list(dict_of_meals_with_ingredients.keys())

# Checking if we have enough quantity of each ingredient, if not create list of missing ingredients with quantity

dict_ingredients_of_chosen_meal = dict_of_meals_with_ingredients[choice_to_eat]
list_of_ingredients_of_chosen_meal = list(dict_ingredients_of_chosen_meal)
dict_of_ingredients_needed = dict()
for ingredient in list_of_ingredients_of_chosen_meal:
    result_of_check_ingredients = dict_of_ingredients_and_values[ingredient] - \
                                  dict_ingredients_of_chosen_meal[ingredient]
    if result_of_check_ingredients < 0:
        dict_of_ingredients_needed[ingredient] = abs(result_of_check_ingredients)

# "Making meal" -  changing quantity of this ingredients what we use for this meal
if len(dict_of_ingredients_needed.items()) == 0:
    for ingredient in list_of_ingredients_of_chosen_meal:
        result_of_check_ingredients = dict_of_ingredients_and_values[ingredient] - \
                                      dict_ingredients_of_chosen_meal[ingredient]
        dict_of_ingredients_and_values[ingredient] = result_of_check_ingredients
else:
    print(f'We have no enough quantity of this ingredients {dict_of_ingredients_needed}. '
          f'Go to shop and add to your ingredients')

# Saving new quantity of ingredients into file json.
data_ingredients = open('ingredients.json', "w")
json.dump(data_ingredients_json, data_ingredients)
data_ingredients.close()

if __name__ == "__main__":
    pass