################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.

# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 

# You will need to change the `make_oven()` function to return a new instance
# of your oven.

# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!

class Oven:

  ingredients = []
  
  boil_recipes = [
    #one-ingredient recipes
    [],
    #two-ingredients recipes
    [
      {
        "ingredients" : ["lead", "mercury"],
        "result": "gold"
      }
    ],
    #three-ingredients recipes
    [
      {
        "ingredients" : ["cheese", "dough", "tomato"],
        "result": "pizza"
      }
    ]
  ]
  freeze_recipes = [
    #one-ingredient recipes
    [],
    #two-ingredients recipes
    [
      {
        "ingredients" : ["water", "air"],
        "result": "snow"
      }
    ]
  ]
  wait_recipes = []

  result = ""

  def __init__(self):
    pass

  def add(self, item):
    self.ingredients.append(item)

  def freeze(self):
    number_of_ingredients = len(self.ingredients)
    recipes_guide = self.freeze_recipes[number_of_ingredients-1]     #Due to 0 as starting index ponint
    for recipe in recipes_guide:
      if recipe["ingredients"] == self.ingredients:
        self.result = recipe["result"]
        break

  def boil(self):
    number_of_ingredients = len(self.ingredients)
    recipes_guide = self.boil_recipes[number_of_ingredients-1]
    for recipe in recipes_guide:
      if recipe["ingredients"] == self.ingredients:
        self.result = recipe["result"]
        break

  def wait(self):
    number_of_ingredients = len(self.ingredients)
    recipes_guide = self.wait_recipes[number_of_ingredients-1]
    for recipe in recipes_guide:
      if recipe["ingredients"] == self.ingredients:
        self.result = recipe["result"]
        break

  def get_output(self):
    self.ingredients.clear()
    return self.result


def make_oven():
  return Oven()

def alchemy_combine(oven, ingredients, temperature):
  
  for item in ingredients:
    oven.add(item)

  if temperature < 0:
    oven.freeze()
  elif temperature >= 100:
    oven.boil()
  else:
    oven.wait()

  return oven.get_output()