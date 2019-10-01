#the class to store ingredients
#ADDED COMMENT LINE CHECK OF GIT IS WORKING
class IngredientNode:

    def __init__(self, name, calories, protein, carbs, fat, classification, hazard):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
        self.classification = classification.lower()
        self.hazard = hazard



#the class to store meals
class MealNode:

    def __init__(self, name, ingredient1, ingredient2, ingredient3):
        ingredients = [ingredient1, ingredient2, ingredient3]

        ##Changed this to allow for a None Meal Node to be used for testing and BFS
        for i in ingredients:
            if i == None:
                self.fat_ingredient = None
                self.carb_ingredient = None
                self.protein_ingredient = None
            elif i.classification == 'fat':
                self.fat_ingredient = i
            elif i.classification == 'carb':
                self.carb_ingredient = i
            elif i.classification == 'protein':
                self.protein_ingredient = i

        self.mealName = name
        if self.protein_ingredient == None:
            self.total_calories = 0
            self.total_protein = 0
            self.total_carbs = 0
            self.total_fat = 0
        else:
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


##This returns a list of all combinations of ingredients possible
def getPossibleMeals(protiens,carbs,fats):
    meals = [(p.name,c.name,f.name) for p in protiens for c in carbs for f in fats]
    return meals

##this will check to see if there is a restriction on the meal that is proposed. If so let the user no it cannot use this meal
def check_restrictions(ingredient,vegR,peanutR,lactoseR):
    if ingredient.hazard.lower() == 'none':
        return False
    if vegR == 1:
        if ingredient.hazard.lower() == 'meat':
            return True
        else:
            return False
    if peanutR == 1:
        if ingredient.hazard.lower() == 'peanut':
            return True
        else:
            return False
    if lactoseR == 1:
        if ingredient.hazard.lower() == 'lactose':
            return True
        else:
            return False


##Prints the goals
def print_goals(tcal,tp,tc,tf):
    print("Total Calories:" + str(tcal) + "\n")
    print("Total Protein:" + str(tp) + "\n")
    print("Total Carbs:" + str(tc) + "\n")
    print("Total Fat:" + str(tf) + "\n")


##This gets the calories left for the day based on a day list of meals
def get_calories_left(day,tcal):
    calories = tcal
    for i in day:
        calories -= i.total_calories
    return calories

##Copy function to transition states
def copy_state(s):
    new = []
    for i in s:
        new.append(i)
    return new

##Goal state function we just want three meals.
def goal_state(s):
    if len(s) == 3:
        return True
    else:
        return False

##Adds a meal to the state
def change_state(s,meal):
    new = copy_state(s)
    new.append(meal)
    return new


##Checks if a meal is possible based on restrictions and calories
def isMealPossible(tcal,tp,tc,tf,meal,weight_goal,vegR,peanutR,lactoseR):
    if check_restrictions(meal.protein_ingredient,vegR,peanutR,lactoseR):
        return False
    if check_restrictions(meal.carb_ingredient,vegR,peanutR,lactoseR):
        return False
    if check_restrictions(meal.fat_ingredient,vegR,peanutR,lactoseR):
        return False
    if weight_goal == 'lose':
        if meal.total_calories > tcal:
            return False
        else:
            return True
    if weight_goal == 'gain':
        if meal.total_calories < tcal:
            return False
        else:
            return True

##checks to see if the day given is possible
def isDayPossible(tcal,day,weight_goal):
    calories = tcal
    for i in day:
       calories -= i.total_calories
    if weight_goal == 'lose':
        if calories <= 0:
            return True
        else:
            False
    else:
        if calories >= 0:
            return True
        else:
            False











