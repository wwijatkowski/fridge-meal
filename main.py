import json


def main():
    # choice_to_eat = input('what you want to eat? ')
    choice_to_eat = 'scrambled eggs'
    # Load actual ingredients file list and meals.
    data_ingredients = json.load(open('ingredients.json'))
    data_meals = json.load(open('meals.json'))
    dict_of_ingredients_needed = dict()

    # Checking if we have enough quantity of each ingredient, if not create list of missing ingredients with quantity
    dict_ingredients_of_chosen_meal = data_meals.get(choice_to_eat)

    for ingredient, count in dict_ingredients_of_chosen_meal.items():
        result_of_check_ingredients = data_ingredients.get(ingredient) - count

        if result_of_check_ingredients < 0:
            dict_of_ingredients_needed[ingredient] = abs(result_of_check_ingredients)

    # "Making meal" -  changing quantity of this ingredients what we use for this meal
    if dict_of_ingredients_needed:
        print(f'We have no enough quantity of this ingredients {dict_of_ingredients_needed}. '
              f'Go to shop and add to your ingredients')
    else:
        for ingredient, count in dict_ingredients_of_chosen_meal.items():
            data_ingredients[ingredient] -= count

    # Saving new quantity of ingredients into file json.
    data_ingredients_file = open('ingredients.json', "w")
    json.dump(data_ingredients, data_ingredients_file)
    data_ingredients_file.close()


if __name__ == "__main__":
    main()
