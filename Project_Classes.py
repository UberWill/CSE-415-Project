#the class to store ingredients
class IngredientNode:

    def __init__(self, name, calories, protein, carbs, fat, classification):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
        self.classification = classification.lower()

#the class to store meals
class MealNode:

    def __init__(self, name, ingredient1, ingredient2, ingredient3):
        ingredients = [ingredient1, ingredient2, ingredient3]
        for i in ingredients:
            if i.classification == 'fat':
                self.fat_ingredient = i
            elif i.classification == 'carb':
                self.carb_ingredient = i
            elif i.classification == 'protein':
                self.protein_ingredient = i
        self.mealName = name
        self.total_calories = self.fat_ingredient.calories +\
                              self.carb_ingredient.calories + self.protein_ingredient.calories
        self.total_protein = self.fat_ingredient.protein +\
                              self.carb_ingredient.protein + self.protein_ingredient.protein
        self.total_carbs = self.fat_ingredient.carbs +\
                              self.carb_ingredient.carbs + self.protein_ingredient.carbs
        self.total_fat = self.fat_ingredient.fat +\
                              self.carb_ingredient.fat + self.protein_ingredient.fat

#the class to store meals for the day
class DayNode:

    def __init__(self, meal1, meal2, meal3):
        self.meal1 = meal1
        self.meal2 = meal2
        self.meal3 = meal3
        self.total_calories = meal1.total_calories + meal2.total_calories + meal3.total_calories
        self.total_protein = meal1.total_protein + meal2.total_protein + meal3.total_protein
        self.total_carbs = meal1.total_carbs + meal2.total_carbs + meal3.total_carbs
        self.total_fat = meal1.total_fat + meal2.total_fat + meal3.total_fat
