"""Provide an overview of the nutritional values of a recipe"""

__author__ = "Christian de Vries"

import os


Strings = list[str]


def get_recipe_ingredients() -> Strings:
    """
    Asks the user for a list of ingredients that will be included in a recipe
    """
    ingredient_list = []
    while True:
        ingredient_input = input("Give the name of an ingredient included in the recipe (empty to end)")
        if ingredient_input == "":
            break
        ingredient_list.append(ingredient_input)

    return ingredient_list


def get_nutritional_values(ingredient_list: Strings, file_name="nutritional_values.csv") -> dict:
    """
    Tries to get nutritional values for each of the ingredients in the list from a file
    Asks the user for the nutritional values if not yet available in the file and writes them to the file for future use
    """
    nutritional_value_dict = {}
    # Checks if we have the file and otherwise makes one
    if not os.path.isfile(file_name):
        with open(file_name, "w") as nutritional_value_file:
            nutritional_value_file.write("name,unit,kcal,fat,carbohydrate,protein\n")
    # Open file and obtain nutritional values of each ingredient
    with open(file_name) as nutritional_file:
        next(nutritional_file)  # Skip the header line
        for line in nutritional_file:
            name, unit, kcalories, fat, carbohydrate, protein = line.split(",")
            nutritional_value_dict[name] = {"unit": unit, "kcalories": float(kcalories), "fat": float(fat),
                                            "carbohydrate": float(carbohydrate), "protein": float(protein)}

    new_nutritional_value_dict = {}

    for ingredient in ingredient_list:
        if ingredient not in nutritional_value_dict:
            unit = input("Please provide the amount of units (f.e. 100gr) for which you have "
                         "the nutritional information of " + ingredient)
            kcalories = float(input("Please provide the value for kcalories of " + ingredient))
            carbohydrate = float(input("Please provide the value for carbohydrate of " + ingredient))
            fat = float(input("Please provide the value for fat of " + ingredient))
            protein = float(input("Please provide the value for protein of " + ingredient))
            nutritional_value_dict[name] = {"unit": unit, "kcalories": float(kcalories), "fat": float(fat),
                                            "carbohydrate": float(carbohydrate), "protein": float(protein)}
            new_nutritional_value_dict[ingredient] = {"unit": unit, "kcalories": float(kcalories), "fat": float(fat),
                                                      "carbohydrate": float(carbohydrate), "protein": float(protein)}

            with open(file_name, "a") as nutritional_file:
                for name in new_nutritional_value_dict:
                    unit, kcalories, fat, carbohydrate, protein = new_nutritional_value_dict[ingredient].values()
                    nutritional_file.write("\n" + name + "," + str(unit) + "," + str(kcalories) + "," + str(fat) + "," +
                                           str(carbohydrate) + "," + str(protein) + "")

    # Make dictionary of all nutritional values
    total_nutritional_values_dict = nutritional_value_dict | new_nutritional_value_dict

    # Obtain only the nutritional values of the ingredients in the recipe
    nutritional_value_of_ingredients_dict = {name: total_nutritional_values_dict[name] for name in ingredients}

    return nutritional_value_of_ingredients_dict


def get_amounts(ingredient_list: Strings, nutritional_value_dict: dict) -> dict:
    """
    Given a list of ingredients and a dictionary of nutritional values
    ask the user to provide how much of each ingredient should be used in the recipe
    """

    for ingredient in ingredient_list:
        unit = nutritional_value_dict[ingredient]["unit"]
        amount = float(input("How much " + unit + " of " + ingredient + " is in your recipe?"))
        nutritional_value_dict[ingredient]["amount"] = amount

    return nutritional_value_dict


def generate_table(nutritional_value_dict: dict):
    """
    ask the user for a quantity per ingredient
    generate a table with nutrient information per ingredient and a total for the recipe
    also generate a line of the total per portion (ask the user for the number of portions)
    """
    totals = {}

    # for every ingredient, get the name + values dictionary
    for ingredient, ingredient_values in nutritional_value_dict.items():
        # then for every nutritient type (kCal, fat, etc..), and the matching value for this ingredient
        for nutritient_type, nutritient_value in ingredient_values.items():
            # See if current nutritient_type is "unit"
            if nutritient_type == "unit":
                # then continue the loop, since we dont want to sum units
                continue

            # If this nutritient_type is not being counted yet, add to totals with value 0
            if nutritient_type not in totals:
                totals[nutritient_type] = 0
            # add the amount*value to the total of the matching nutritient_type
            totals[nutritient_type] += ingredient_values["amount"] * nutritient_value

    with open('output.txt', 'w') as f:
        print("{:<15} {:<10} {:<10} {:<12} {:<10} {:<15} {:<10}".format('Ingredient', 'Amount', 'Unit', 'Kcalories',
                                                                        'fat', 'carbohydrat', 'protein'), file=f)
        for name, values in nutritional_value_dict.items():
            unit = values["unit"]
            amount = values["amount"]
            kcalories = values["kcalories"]
            fat = values["fat"]
            carbohydrate = values["carbohydrate"]
            protein = values["protein"]
            print("{:<15} {:<10} {:<10} {:<12.2f} {:<10.2f} {:<15.2f} {:<10.2f}".format(name, amount, unit, kcalories,
                                                                                        fat, carbohydrate, protein),
                  file=f)
        total_kcalories = totals["kcalories"]
        total_fat = totals["fat"]
        total_carbohydrat = totals["carbohydrate"]
        total_protein = totals["protein"]
        print("\n{:<15} {:<10} {:<10} {:<12.2f} {:<10.2f} {:<15.2f} {:<10.2f}".format('Total', " ", " ",
                                                                                      total_kcalories, total_fat,
                                                                                      total_carbohydrat, total_protein),
              file=f)


if __name__ == '__main__':

    # 1.  Ask for a list of ingredients.
    ingredients = get_recipe_ingredients()

    # 2. Get nutrient information for each of these ingredients.
    nutritional_values = get_nutritional_values(ingredients)

    # 3. Ask for a list of amounts for each of the ingredients.
    amounts_list = get_amounts(ingredients, nutritional_values)

    # 4. Based on the information retrieved generate a meaningful output.
    generate_table(nutritional_values)
