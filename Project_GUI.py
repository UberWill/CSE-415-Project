import tkinter
import Project_Classes

#global variables used to make the ingredient objects
i_name = ""
i_class = ""
i_cals = 0
i_pro = 0
i_carbs = 0
i_fat = 0

#just a simple variable to make sure a meal plan has been created, 0 = not created, 1 = created
plan_made = 0

#a list of all already suggested meal plans (gets filled and checked in bfs)
suggested_meal_plans = []

#A list of all added ingredients (they have their own attributes - see IngredientNode class)
added_ingredients = []
carb_ingredients = []
protein_ingredients = []
fat_ingredients = []
full_days = []
meals = []

#counters for how many of each classification of ingredient has been added
fc = 3
cc = 3
pc = 4

##TEST ADDITON OF INGREDIENTS
chicken = Project_Classes.IngredientNode("Chicken",220,48,0,2,'protein','meat')
ground_beef = Project_Classes.IngredientNode("Ground Beef",231,23,0,15,'protein','meat')
tuna  = Project_Classes.IngredientNode("Tuna",80,16,0,0,'protein','meat')
tofu = Project_Classes.IngredientNode("Tofu",180,20,2,12,'protein','none')
rice = Project_Classes.IngredientNode("rice",200,4,45,0,'carb','none')
noodle = Project_Classes.IngredientNode("Spagetti Noodle",220,8,43,1,'carb','none')
bread = Project_Classes.IngredientNode("Texas Toast",150,3,15,8,'carb','none')
oil = Project_Classes.IngredientNode("Olive oil",120,0,0,14,'fat','none')
cheese = Project_Classes.IngredientNode("Cheddar Cheese",114,7,0,10,'fat','lactose')
pb = Project_Classes.IngredientNode("Peanut Butter",188,8,6,16,'fat','peanut')
added_ingredients.append(chicken)
added_ingredients.append(ground_beef)
added_ingredients.append(tuna)
added_ingredients.append(tofu)
added_ingredients.append(rice)
added_ingredients.append(noodle)
added_ingredients.append(bread)
added_ingredients.append(oil)
added_ingredients.append(cheese)
added_ingredients.append(pb)
protein_ingredients.append(chicken)
protein_ingredients.append(ground_beef)
protein_ingredients.append(tuna)
protein_ingredients.append(tofu)
carb_ingredients.append(rice)
carb_ingredients.append(noodle)
carb_ingredients.append(bread)
fat_ingredients.append(oil)
fat_ingredients.append(cheese)
fat_ingredients.append(pb)



#setting up the window
window = tkinter.Tk()
window.title("Diet Plan")
window.wm_iconbitmap('icon.ico')

#the frame for the ingredient section
ing = tkinter.Frame(window,bd=5,relief='ridge')
ing.grid(row=0,column=0,sticky='w')

#the frame for the goal section
goals = tkinter.Frame(window,bd=5,relief='ridge')
goals.grid(row=1,column=0,sticky='e')

#the frame for the restrictions section
rest = tkinter.Frame(window,bd=5,relief='ridge')
rest.grid(row=1,column=1,sticky='w')

#the frame to house the meals and goal differences, basically the results
results = tkinter.Frame(window,bd=5,relief = 'ridge')
results.grid(row=0,column=1,sticky='w')

#the ingredient hazard, 'peanuts' is peanut allergy, 'meat' means not vegetarian safe, 'lactose'
#means not lactose intolerant safe, 'none' is obvious
i_hazard = tkinter.StringVar()
i_hazard.set("none")

#the goal for weight loss or weight gain, "lose" is for weight loss, "gain" is for weight gain
#this gets changed via the radio buttons in the goal section automatically as different
#radio buttons are chosen
weight_goal = tkinter.StringVar()
weight_goal.set("lose")
#global variables for goals
g_cals = 0
g_fat = 0
g_pro = 0
g_carbs = 0

#the restrictions, 0 means they dont have that restriction, 1 means they do
#these get updated by the checkboxes in the restrictions section by the user
vegetarian = tkinter.IntVar()
peanut_allergy = tkinter.IntVar()
lactose_intolerant = tkinter.IntVar()
#the variable to show that the restrictions have been set by user (0=not set, 1 = set)
set_r = 0


#function to get ingredient input and store it
def get_ingredient():
    global i_name
    i_name = name.get()
    global i_cals
    i_cals = total_calories.get()
    global i_pro
    i_pro = protein.get()
    global i_carbs
    i_carbs = carbs.get()
    global i_fat
    i_fat = fat.get()
    global i_class
    i_class = classif.get()
    global i_hazard

    #convert the string input to integers, if not possible display error to user
    try:
        i_cals = int(i_cals)
    except ValueError:
        top = tkinter.Toplevel()
        top.title("Error")
        top.geometry('{}x{}'.format(180,100))
        top.wm_iconbitmap('error.ico')
        msg = tkinter.Message(top, text = "Please enter an integer amount for calories.")
        msg.pack()
        errbutton = tkinter.Button(top, text = "Dismiss", command = top.destroy)
        errbutton.pack()
        i_name = ''
        i_cals = 0
        i_pro = 0
        i_carbs = 0
        i_fat = 0
        return 0
    try:
        i_pro = int(i_pro)
    except ValueError:
        top = tkinter.Toplevel()
        top.title("Error")
        top.geometry('{}x{}'.format(180,100))
        top.wm_iconbitmap('error.ico')
        msg = tkinter.Message(top, text = "Please enter an integer amount for protein.")
        msg.pack()
        errbutton = tkinter.Button(top, text = "Dismiss", command = top.destroy)
        errbutton.pack()
        i_name = ''
        i_cals = 0
        i_pro = 0
        i_carbs = 0
        i_fat = 0
        return 0
    try:
        i_carbs = int(i_carbs)
    except ValueError:
        top = tkinter.Toplevel()
        top.title("Error")
        top.geometry('{}x{}'.format(180,100))
        top.wm_iconbitmap('error.ico')
        msg = tkinter.Message(top, text = "Please enter an integer amount for carbs.")
        msg.pack()
        errbutton = tkinter.Button(top, text = "Dismiss", command = top.destroy)
        errbutton.pack()
        i_name = ''
        i_cals = 0
        i_pro = 0
        i_carbs = 0
        i_fat = 0
        return 0
    try:
        i_fat = int(i_fat)
    except ValueError:
        top = tkinter.Toplevel()
        top.title("Error")
        top.geometry('{}x{}'.format(180,100))
        top.wm_iconbitmap('error.ico')
        msg = tkinter.Message(top, text = "Please enter an integer amount for fat.")
        msg.pack()
        errbutton = tkinter.Button(top, text = "Dismiss", command = top.destroy)
        errbutton.pack()
        i_name = ''
        i_cals = 0
        i_pro = 0
        i_carbs = 0
        i_fat = 0
        return 0

    #display error if not all fields filled
    if i_name == '' or i_cals == '' or i_pro == '' or i_carbs == '' or i_fat == '' or i_class == '':
        top = tkinter.Toplevel()
        top.title("Error")
        top.geometry('{}x{}'.format(180,100))
        top.wm_iconbitmap('error.ico')
        msg = tkinter.Message(top, text = "Please do not leave an ingredient entry blank.")
        msg.pack()
        errbutton = tkinter.Button(top, text = "Dismiss", command = top.destroy)
        errbutton.pack()
        i_name = ''
        i_cals = 0
        i_pro = 0
        i_carbs = 0
        i_fat = 0
    elif not i_class.lower() in ['fat', 'carb', 'protein']:
        top = tkinter.Toplevel()
        top.title("Error")
        top.geometry('{}x{}'.format(180,100))
        top.wm_iconbitmap('error.ico')
        msg = tkinter.Message(top, text = "Please make sure Ingredient is either fat, carb, or protein.")
        msg.pack()
        errbutton = tkinter.Button(top, text = "Dismiss", command = top.destroy)
        errbutton.pack()
        i_name = ''
        i_cals = 0
        i_pro = 0
        i_carbs = 0
        i_fat = 0
    else:
        ##This is where the ingredient is actually added
        global added_ingredients
        new_ing = Project_Classes.IngredientNode(i_name,i_cals,i_pro,i_carbs,i_fat,i_class,i_hazard.get())
        added_ingredients.append(new_ing)
        if(new_ing.classification == 'carb'):
            carb_ingredients.append(new_ing)
        if(new_ing.classification == 'protein'):
            protein_ingredients.append(new_ing)
        if(new_ing.classification == 'fat'):
            fat_ingredients.append(new_ing)
        name.delete(0,'end')
        total_calories.delete(0,'end')
        protein.delete(0,'end')
        carbs.delete(0,'end')
        fat.delete(0,'end')
        classif.delete(0,'end')
        i_hazard.set('none')

        counter.configure(state='normal')
        counter.delete(1.0,'end')
        counter.insert('end',len(added_ingredients))
        counter.configure(state='disabled')

        if new_ing.classification == 'fat':
            global fc
            fc += 1
            fat_counter.configure(state='normal')
            fat_counter.delete(1.0,'end')
            fat_counter.insert('end',fc)
            fat_counter.configure(state='disabled')
        elif new_ing.classification == 'carb':
            global cc
            cc += 1
            carb_counter.configure(state='normal')
            carb_counter.delete(1.0,'end')
            carb_counter.insert('end',cc)
            carb_counter.configure(state='disabled')
        elif new_ing.classification == 'protein':
            global pc
            pc += 1
            pro_counter.configure(state='normal')
            pro_counter.delete(1.0,'end')
            pro_counter.insert('end',pc)
            pro_counter.configure(state='disabled')

#the method that takes the user input for goals and stores it
def set_goals():
    global g_cals
    global g_fat
    global g_pro
    global g_carbs
    global weight_goal
    g_cals = calories_goal.get()
    g_fat = fat_goal.get()
    g_pro = protein_goal.get()
    g_carbs = carb_goal.get()

    #convert the string input to integers, if not possible display error to user
    try:
        g_cals = int(g_cals)
    except ValueError:
        top = tkinter.Toplevel()
        top.title("Error")
        top.geometry('{}x{}'.format(180,100))
        top.wm_iconbitmap('error.ico')
        msg = tkinter.Message(top, text = "Please enter an integer amount for calories.")
        msg.pack()
        errbutton = tkinter.Button(top, text = "Dismiss", command = top.destroy)
        errbutton.pack()
        g_cals = 0
        g_fat = 0
        g_pro = 0
        g_carbs = 0
        return 0
    try:
        g_fat = int(g_fat)
    except ValueError:
        top = tkinter.Toplevel()
        top.title("Error")
        top.geometry('{}x{}'.format(180,100))
        top.wm_iconbitmap('error.ico')
        msg = tkinter.Message(top, text = "Please enter an integer amount for fat.")
        msg.pack()
        errbutton = tkinter.Button(top, text = "Dismiss", command = top.destroy)
        errbutton.pack()
        g_cals = 0
        g_fat = 0
        g_pro = 0
        g_carbs = 0
        return 0
    try:
        g_pro = int(g_pro)
    except ValueError:
        top = tkinter.Toplevel()
        top.title("Error")
        top.geometry('{}x{}'.format(180,100))
        top.wm_iconbitmap('error.ico')
        msg = tkinter.Message(top, text = "Please enter an integer amount for protein.")
        msg.pack()
        errbutton = tkinter.Button(top, text = "Dismiss", command = top.destroy)
        errbutton.pack()
        g_cals = 0
        g_fat = 0
        g_pro = 0
        g_carbs = 0
        return 0
    try:
        g_carbs = int(g_carbs)
    except ValueError:
        top = tkinter.Toplevel()
        top.title("Error")
        top.geometry('{}x{}'.format(180,100))
        top.wm_iconbitmap('error.ico')
        msg = tkinter.Message(top, text = "Please enter an integer amount for carbs.")
        msg.pack()
        errbutton = tkinter.Button(top, text = "Dismiss", command = top.destroy)
        errbutton.pack()
        g_cals = 0
        g_fat = 0
        g_pro = 0
        g_carbs = 0
        return 0

    #display error if not all fields filled out
    if g_cals == '' or g_fat == '' or g_pro == '' or g_carbs == '':
        top = tkinter.Toplevel()
        top.title("Error")
        top.geometry('{}x{}'.format(180,90))
        top.wm_iconbitmap('error.ico')
        msg = tkinter.Message(top, text = "Please do not leave a goal entry blank.")
        msg.pack()
        errbutton = tkinter.Button(top, text = "Dismiss", command = top.destroy)
        errbutton.pack()
        g_cals = 0
        g_fat = 0
        g_pro = 0
        g_carbs = 0
    elif ((g_fat / 100) + (g_pro / 100) + (g_carbs / 100)) != 1:
        top = tkinter.Toplevel()
        top.title("Error")
        top.geometry('{}x{}'.format(180,90))
        top.wm_iconbitmap('error.ico')
        msg = tkinter.Message(top, text = "Please make sure %'s add to 100%")
        msg.pack()
        errbutton = tkinter.Button(top, text = "Dismiss", command = top.destroy)
        errbutton.pack()
        g_cals = 0
        g_fat = 0
        g_pro = 0
        g_carbs = 0
    else:
        g_fat = ((g_fat / 100) * g_cals) / 9
        g_fat = round(g_fat,1)
        g_pro = ((g_pro / 100) * g_cals) / 4
        g_pro = round(g_pro,1)
        g_carbs = ((g_carbs / 100) * g_cals) / 4
        g_carbs = round(g_carbs)

        fat_goal.delete(0,'end')
        fat_goal.insert('end',str(g_fat)+' Grams of Fat')
        protein_goal.delete(0,'end')
        protein_goal.insert('end',str(g_pro)+' Grams of Protein')
        carb_goal.delete(0,'end')
        carb_goal.insert('end',str(g_carbs)+' Grams of carbs')

        calories_goal.configure(state='disabled')
        fat_goal.configure(state='disabled')
        protein_goal.configure(state='disabled')
        carb_goal.configure(state='disabled')
        #r1.configure(state='disabled')
        #r2.configure(state='disabled')

        goal_set.configure(state='normal')
        goal_set.insert('end',"GOAL SET!")
        goal_set.configure(state='disabled')

#the method that resets the goals so the user can input new ones
def reset_goals():
    global g_cals, g_fat, g_pro, g_carbs, weight_goal
    weight_goal.set("lose")
    g_cals = 0
    g_fat = 0
    g_pro = 0
    g_carbs = 0
    calories_goal.configure(state='normal')
    fat_goal.configure(state='normal')
    protein_goal.configure(state='normal')
    carb_goal.configure(state='normal')
    #r1.configure(state='normal')
    #r2.configure(state='normal')

    calories_goal.delete(0,'end')
    fat_goal.delete(0,'end')
    protein_goal.delete(0,'end')
    carb_goal.delete(0,'end')

    goal_set.configure(state='normal')
    goal_set.delete(1.0,'end')
    goal_set.configure(state='disabled')

    whipe_meal_data()

#the method that sets the restrictions to prevent accidental changes
def set_restrictions():
    c1.configure(state='disabled')
    c2.configure(state='disabled')
    c3.configure(state='disabled')
    restrictions_set.configure(state='normal')
    restrictions_set.insert('end',"RESTRICTIONS SET!")
    restrictions_set.configure(state='disabled')
    global set_r
    set_r = 1

#the method that resets the restrictions to allow changes to them
def reset_restrictions():
    c1.configure(state='normal')
    c2.configure(state='normal')
    c3.configure(state='normal')
    restrictions_set.configure(state='normal')
    restrictions_set.delete(1.0,'end')
    restrictions_set.configure(state='disabled')
    global vegetarian
    global peanut_allergy
    global lactose_intolerant
    vegetarian.set(0)
    peanut_allergy.set(0)
    lactose_intolerant.set(0)
    global set_r
    set_r = 0
    whipe_meal_data()


def getIngredient(name,list):
    for x in list:
        if x.name == name:
            return x


##Trying to figure out if we need the "name" field
def makeAMeal(ingredients,number):
    return Project_Classes.MealNode((number+1),getIngredient(ingredients[0],protein_ingredients),getIngredient(ingredients[1],carb_ingredients),getIngredient(ingredients[2],fat_ingredients))


##BFS
def IterativeBFS(s):
    OPEN = [s]
    CLOSED = []

    ##Gets all permutations of ingredients
    ingredient_combos = Project_Classes.getPossibleMeals(protein_ingredients,carb_ingredients,fat_ingredients)

    ##Creates a list of meal objects based on permutations
    meals = []
    for c in ingredient_combos:
        meal = makeAMeal(c,0)
        meals.append(meal)

    ##Does BFS stops when we get a viable meal (May need to have another check for the day in total)
    while OPEN != []:
        S = OPEN[0]
        del OPEN[0]
        CLOSED.append(S)
        L = []
        if Project_Classes.goal_state(S) and not(meal_match(S)):
            print("Got em")
            suggested_meal_plans.append(S)
            return S
        for m in meals:
            if Project_Classes.isMealPossible(g_cals,g_pro,g_carbs,g_fat,m,weight_goal.get(),vegetarian.get(),peanut_allergy.get(),lactose_intolerant.get()):
                new_state = Project_Classes.change_state(S,m)
                if new_state not in CLOSED and m not in S:
                    L.append(new_state)
        OPEN = OPEN + L

#given a day's meal plan, returns true if that meal has already been suggested
def meal_match(meal_plan):
    global suggested_meal_plans
    for s in suggested_meal_plans:
        same_meals_found = 0
        for i in range(3):
            if meal_plan[i].fat_ingredient == s[i].fat_ingredient and \
                    meal_plan[i].carb_ingredient == s[i].carb_ingredient and \
                    meal_plan[i].protein_ingredient == s[i].protein_ingredient:
                same_meals_found += 1
        if same_meals_found == 3:
            return True
    return False

#The method that will make the meals once all input from user received
def make_meals():
    global g_cals, g_fat, g_protein, g_carbs, added_ingredients, set_r, fc, cc, pc
    #displays error if no goals set
    if g_cals == 0 and g_fat == 0 and g_pro == 0 and g_carbs == 0:
        top = tkinter.Toplevel()
        top.title("Error")
        top.geometry('{}x{}'.format(180,70))
        top.wm_iconbitmap('error.ico')
        msg = tkinter.Message(top, text = "Please set goals first.")
        msg.pack()
        errbutton = tkinter.Button(top, text = "Dismiss", command = top.destroy)
        errbutton.pack()
    #displays error is no ingredients added
    elif len(added_ingredients) < 3:
        top = tkinter.Toplevel()
        top.title("Error")
        top.geometry('{}x{}'.format(180,90))
        top.wm_iconbitmap('error.ico')
        msg = tkinter.Message(top, text = "Please add more ingredients first.")
        msg.pack()
        errbutton = tkinter.Button(top, text = "Dismiss", command = top.destroy)
        errbutton.pack()
    elif fc == 0 or cc == 0 or pc == 0:
        top = tkinter.Toplevel()
        top.title("Error")
        top.geometry('{}x{}'.format(180,90))
        top.wm_iconbitmap('error.ico')
        msg = tkinter.Message(top, text = "Please add at least one ingredient of each type.")
        msg.pack()
        errbutton = tkinter.Button(top, text = "Dismiss", command = top.destroy)
        errbutton.pack()
    elif set_r == 0:
        top = tkinter.Toplevel()
        top.title("Error")
        top.geometry('{}x{}'.format(180,90))
        top.wm_iconbitmap('error.ico')
        msg = tkinter.Message(top, text = "Please set restrictions first.")
        msg.pack()
        errbutton = tkinter.Button(top, text = "Dismiss", command = top.destroy)
        errbutton.pack()
    else:
        ##This is just a tester to make sure things are working according to plan
        Project_Classes.print_goals(g_cals,g_pro,g_carbs,g_fat)

        ##Here we just create a empty list that will get filled by IterativeBFS
        day = []

        ##Gets a day's worth of meals! Seems to be working just fine! Does not allow for the same meal all day
        day  = IterativeBFS(day)

        #if no meals could be found, tell user
        if day == None:
            #meal1
            meal1.configure(state='normal')
            meal1.insert('end','NO MEAL COULD BE\n FOUND')
            meal1.configure(state='disabled')
            #meal 2
            meal2.configure(state='normal')
            meal2.insert('end','NO MEAL COULD BE\n FOUND')
            meal2.configure(state='disabled')
            #meal 3
            meal3.configure(state='normal')
            meal3.insert('end','NO MEAL COULD BE\n FOUND')
            meal3.configure(state='disabled')
            return 0

        #display the results for each day's meals in the results part of the GUI

        #meal1
        meal1.configure(state='normal')
        meal1.insert('end',day[0].fat_ingredient.name +'\n'+ day[0].carb_ingredient.name +\
                     '\n'+ day[0].protein_ingredient.name)
        meal1.configure(state='disabled')
        #meal 2
        meal2.configure(state='normal')
        meal2.insert('end',day[1].fat_ingredient.name +'\n'+ day[1].carb_ingredient.name +\
                     '\n'+ day[1].protein_ingredient.name)
        meal2.configure(state='disabled')
        #meal 3
        meal3.configure(state='normal')
        meal3.insert('end',day[2].fat_ingredient.name +'\n'+ day[2].carb_ingredient.name +\
                     '\n'+ day[2].protein_ingredient.name)
        meal3.configure(state='disabled')

        #display the goal differences
        day_meals = Project_Classes.DayNode(day[0],day[1],day[2])

        #calorie differences
        total_meal_cals.configure(state='normal')
        total_meal_cals.insert('end',day_meals.total_calories)
        total_meal_cals.configure(state='disabled')
        diff_cals.configure(state='normal')
        if day_meals.total_calories-g_cals > 0:
            diff_cals.insert('end','+')
        diff_cals.insert('end',day_meals.total_calories-g_cals)
        diff_cals.configure(state='disabled')

        #fat differences
        total_meal_fat.configure(state='normal')
        total_meal_fat.insert('end',day_meals.total_fat)
        total_meal_fat.configure(state='disabled')
        diff_fat.configure(state='normal')
        if day_meals.total_fat-g_fat > 0:
            diff_fat.insert('end','+')
        diff_fat.insert('end',day_meals.total_fat-g_fat)
        diff_fat.configure(state='disabled')

        #protein differences
        total_meal_pro.configure(state='normal')
        total_meal_pro.insert('end',day_meals.total_protein)
        total_meal_pro.configure(state='disabled')
        diff_pro.configure(state='normal')
        if day_meals.total_protein-g_pro > 0:
            diff_pro.insert('end','+')
        diff_pro.insert('end',day_meals.total_protein-g_pro)
        diff_pro.configure(state='disabled')

        #carbs differences
        total_meal_carbs.configure(state='normal')
        total_meal_carbs.insert('end',day_meals.total_carbs)
        total_meal_carbs.configure(state='disabled')
        diff_carbs.configure(state='normal')
        if day_meals.total_carbs-g_carbs > 0:
            diff_carbs.insert('end','+')
        diff_carbs.insert('end',day_meals.total_carbs-g_carbs)
        diff_carbs.configure(state='disabled')

        #make sure to mark that a meal plan has been made (used in new_meals())
        global plan_made
        plan_made = 1


#the method to display new meals if shown ones were not to the user's liking
def new_meals():
    global plan_made
    if plan_made == 0:
        top = tkinter.Toplevel()
        top.title("Error")
        top.geometry('{}x{}'.format(180,100))
        top.wm_iconbitmap('error.ico')
        msg = tkinter.Message(top, text = "Please click Make Meals first before making new meals.")
        msg.pack()
        errbutton = tkinter.Button(top, text = "Dismiss", command = top.destroy)
        errbutton.pack()
    else:
        #whipe all data from GUI
        whipe_meal_data()
        make_meals()

def whipe_meal_data():
    #whipe all data from GUI
        meal1.configure(state='normal')
        meal1.delete(1.0,'end')
        meal1.configure(state='disabled')

        meal2.configure(state='normal')
        meal2.delete(1.0,'end')
        meal2.configure(state='disabled')

        meal3.configure(state='normal')
        meal3.delete(1.0,'end')
        meal3.configure(state='disabled')

        total_meal_cals.configure(state='normal')
        total_meal_cals.delete(1.0,'end')
        total_meal_cals.configure(state='disabled')

        total_meal_fat.configure(state='normal')
        total_meal_fat.delete(1.0,'end')
        total_meal_fat.configure(state='disabled')

        total_meal_pro.configure(state='normal')
        total_meal_pro.delete(1.0,'end')
        total_meal_pro.configure(state='disabled')

        total_meal_carbs.configure(state='normal')
        total_meal_carbs.delete(1.0,'end')
        total_meal_carbs.configure(state='disabled')

        diff_cals.configure(state='normal')
        diff_cals.delete(1.0,'end')
        diff_cals.configure(state='disabled')

        diff_fat.configure(state='normal')
        diff_fat.delete(1.0,'end')
        diff_fat.configure(state='disabled')

        diff_pro.configure(state='normal')
        diff_pro.delete(1.0,'end')
        diff_pro.configure(state='disabled')

        diff_carbs.configure(state='normal')
        diff_carbs.delete(1.0,'end')
        diff_carbs.configure(state='disabled')

#initialize the Add Intgredients section
tkinter.Label(ing, text = "Add Ingredients", font= ("Helvetica",16)).grid(row=0,columnspan=2)
#the name input area
tkinter.Label(ing, text = "Name",).grid(row=1,sticky='e')
name = tkinter.Entry(ing)
name.grid(row=1,column=1)
#total calories input area
tkinter.Label(ing, text = "Total Calories").grid(row=2,sticky='e')
total_calories = tkinter.Entry(ing)
total_calories.grid(row=2,column=1)
#protien input area
tkinter.Label(ing, text = "Protein (g)").grid(row=3,sticky='e')
protein = tkinter.Entry(ing)
protein.grid(row=3,column=1)
#carbs input area
tkinter.Label(ing, text= "Carbs (g)").grid(row=4,sticky='e')
carbs = tkinter.Entry(ing)
carbs.grid(row=4,column=1)
#fat input area
tkinter.Label(ing, text="Fat (g)").grid(row=5,sticky='e')
fat = tkinter.Entry(ing)
fat.grid(row=5,column=1)
#the ingredient classification area (fat, carb, or protein)
tkinter.Label(ing, text="Classification\n(Fat, Carb, or Protein)").grid(row=6,sticky='e')
classif = tkinter.Entry(ing)
classif.grid(row=6,column=1)

#area for user to specify food hazard for ingredient
h1 = tkinter.Radiobutton(ing, text = "Contains Peanuts", variable = i_hazard, value = 'peanut')
h1.grid(row = 7, column = 1,sticky='w')
h2 = tkinter.Radiobutton(ing, text = "Meat Product", variable = i_hazard, value = 'meat')
h2.grid(row = 8, column = 1,sticky='w')
h3 = tkinter.Radiobutton(ing, text = "Contains Lactose", variable = i_hazard, value = 'lactose')
h3.grid(row = 9, column = 1,sticky='w')
h4 = tkinter.Radiobutton(ing, text = "No Hazard", variable = i_hazard, value = 'none')
h4.grid(row=10,column=1,sticky = 'w')

#button to finish the adding of ingredient
tkinter.Button(ing, text="Add Ingredient",
               command = get_ingredient).grid(row=11,column=1,sticky='w',pady=4)

#number of ingredients added, counter
tkinter.Label(ing,text="Ingredients\nAdded:").grid(row=12,column=0,sticky='e')
counter = tkinter.Text(ing,height=1,width=3)
counter.grid(row=12,column=1,sticky='w')
counter.insert('end',len(added_ingredients))
counter.configure(state='disabled')

#number of fat-based ingredients added
tkinter.Label(ing,text="Fat-Based\nIngredients\nAdded:").grid(row=13,column=0,sticky='e')
fat_counter = tkinter.Text(ing,height=1,width=3)
fat_counter.grid(row=13,column=1,sticky='w')
fat_counter.insert('end',fc)
fat_counter.configure(state='disabled')

#number of carb-based ingredients added
tkinter.Label(ing,text="Carb-Based\nIngredients\nAdded:").grid(row=14,column=0,sticky='e')
carb_counter = tkinter.Text(ing,height=1,width=3)
carb_counter.grid(row=14,column=1,sticky='w')
carb_counter.insert('end',cc)
carb_counter.configure(state='disabled')

#number of protein-based ingredients added
tkinter.Label(ing,text="Protein-Based\nIngredients\nAdded:").grid(row=15,column=0,sticky='e')
pro_counter = tkinter.Text(ing,height=1,width=3)
pro_counter.grid(row=15,column=1,sticky='w')
pro_counter.insert('end',pc)
pro_counter.configure(state='disabled')


#initialize the goals section
tkinter.Label(goals, text = "Goals", font= ("Helvetica",16)).grid(row=8,column=1,sticky='w')
#the calorie goal input area
tkinter.Label(goals, text = "Calories",).grid(row=9,sticky='e')
calories_goal = tkinter.Entry(goals)
calories_goal.grid(row=9,column=1)
#the fat goal input area
tkinter.Label(goals, text = "Fat (%)",).grid(row=10,sticky='e')
fat_goal = tkinter.Entry(goals)
fat_goal.grid(row=10,column=1)
#the protein goal input area
tkinter.Label(goals, text = "Protein (%)",).grid(row=11,sticky='e')
protein_goal = tkinter.Entry(goals)
protein_goal.grid(row=11,column=1)
#the carb goal input area
tkinter.Label(goals, text = "Carb (%)",).grid(row=12,sticky='e')
carb_goal = tkinter.Entry(goals)
carb_goal.grid(row=12,column=1)
#the lose weight or gain weight options
#r1 = tkinter.Radiobutton(goals, text='Lose Weight', variable = weight_goal, value = 'lose')
#r1.grid(row=13,column=1)
#r2 =tkinter.Radiobutton(goals, text='Gain Weight', variable = weight_goal, value = 'gain')
#r2.grid(row=14,column=1)
#button to set goals
tkinter.Button(goals, text="Set Goals",
               command = set_goals).grid(row=15,column=0,sticky='e',pady=4)
#space to let the user know their goals have been accepted by the program
goal_set = tkinter.Text(goals,height=1,width=9)
goal_set.grid(row=15,column=1)
goal_set.configure(state='disabled')
#button to reset goals
tkinter.Button(goals, text="Reset Goals",
               command = reset_goals).grid(row=16,column=0,sticky='e',pady=4)


#the area the user will select certain restrictions from
tkinter.Label(rest, text = "Restrictions", font= ("Helvetica",16)).grid(row=0,columnspan=2)
#all the restrictions
c1 = tkinter.Checkbutton(rest, text = "Vegetarian", variable = vegetarian)
c1.grid(row = 1, column = 0,sticky='w')
c2 = tkinter.Checkbutton(rest, text = "Peanut Allergy", variable = peanut_allergy)
c2.grid(row = 2, column = 0,sticky='w')
c3 = tkinter.Checkbutton(rest, text = "Lactose Intolerant", variable = lactose_intolerant)
c3.grid(row = 3, column = 0,sticky='w')
#button to set restrictions
tkinter.Button(rest, text="Set Restrictions",
               command = set_restrictions).grid(row=4,column=0,sticky='w',pady=4)
#space to let the user know their restrictions have been accepted by the program
restrictions_set = tkinter.Text(rest,height=1,width=17)
restrictions_set.grid(row=4,column=1)
restrictions_set.configure(state='disabled')
#button to reset restrictions
tkinter.Button(rest, text="Reset Restrictions",
               command = reset_restrictions).grid(row=5,column=0,sticky='w',pady=4)


#the section where we display the results
#meal 1 info
tkinter.Label(results,text="Meal 1",font= ("Helvetica",12)).grid(row=0,column=0)
meal1 = tkinter.Text(results,height = 5, width = 20)
meal1.grid(row=1,column=0)
meal1.configure(state='disabled')
#meal 2 info
tkinter.Label(results,text="Meal 2",font= ("Helvetica",12)).grid(row=2,column=0)
meal2 = tkinter.Text(results,height = 5, width = 20)
meal2.grid(row=3,column=0)
meal2.configure(state='disabled')
#meal 3 info
tkinter.Label(results,text="Meal 3",font= ("Helvetica",12)).grid(row=4,column=0)
meal3 = tkinter.Text(results,height = 5, width = 20)
meal3.grid(row=5,column=0)
meal3.configure(state='disabled')
#button to make the meals once all input recieved
tkinter.Button(results, text="Make Meals", command = make_meals).grid(row=0,column=1,pady=4)
#button to request new meals if shown ones aren't to user's liking
tkinter.Button(results, text="New Meals", command = new_meals).grid(row=4,column=1,pady=4)
#the difference between goal and meal nutritional values data
#set up the labels
goal_diff = tkinter.Frame(results,bd=5,relief = 'ridge')
goal_diff.grid(row=1,rowspan=3,column=1)
tkinter.Label(goal_diff,text='Goals Difference',font= ("Helvetica",12)).grid(row=0,columnspan=3)
tkinter.Label(goal_diff,text='Total').grid(row=1,column=1)
tkinter.Label(goal_diff,text='Difference').grid(row=1,column=2)
tkinter.Label(goal_diff,text='Calories').grid(row=2,column=0)
tkinter.Label(goal_diff,text='Fat').grid(row=3,column=0)
tkinter.Label(goal_diff,text='Protein').grid(row=4,column=0)
tkinter.Label(goal_diff,text='Carbs').grid(row=5,column=0)
#now put in data fields (these will get populated during the actual meal selection)
total_meal_cals = tkinter.Text(goal_diff,height=1,width=6)
total_meal_cals.grid(row=2,column=1)
total_meal_cals.configure(state='disabled')

diff_cals = tkinter.Text(goal_diff,height=1,width=6)
diff_cals.grid(row=2,column=2)
diff_cals.configure(state='disabled')

total_meal_fat = tkinter.Text(goal_diff,height=1,width=6)
total_meal_fat.grid(row=3,column=1)
total_meal_fat.configure(state='disabled')

diff_fat = tkinter.Text(goal_diff,height=1,width=6)
diff_fat.grid(row=3,column=2)
diff_fat.configure(state='disabled')

total_meal_pro = tkinter.Text(goal_diff,height=1,width=6)
total_meal_pro.grid(row=4,column=1)
total_meal_pro.configure(state='disabled')

diff_pro = tkinter.Text(goal_diff,height=1,width=6)
diff_pro.grid(row=4,column=2)
diff_pro.configure(state='disabled')

total_meal_carbs = tkinter.Text(goal_diff,height=1,width=6)
total_meal_carbs.grid(row=5,column=1)
total_meal_carbs.configure(state='disabled')

diff_carbs = tkinter.Text(goal_diff,height=1,width=6)
diff_carbs.grid(row=5,column=2)
diff_carbs.configure(state='disabled')

#Default Ingredient List for testing purposes#
#######################################################################################################################
# chicken = Project_Classes.IngredientNode("Chicken",220,48,0,2,'protein','meat')
# ground_beef = Project_Classes.IngredientNode("Ground Beef",231,23,0,15,'protein','meat')
# tuna  = Project_Classes.IngredientNode("Tuna",80,16,0,0,'protein','meat')
# rice = Project_Classes.IngredientNode("rice",200,4,45,0,'carb','none')
# noodle = Project_Classes.IngredientNode("Spagetti Noodle",220,8,43,1,'carb','none')
# bread = Project_Classes.IngredientNode("Texas Toast",150,3,15,8,'carb','none')
# oil = Project_Classes.IngredientNode("Olive oil",120,0,0,14,'fat','none')
# cheese = Project_Classes.IngredientNode("Cheddar Cheese",114,7,0,10,'fat','lactose')
# pb = Project_Classes.IngredientNode("Peanut Butter",188,8,6,16,'fat','peanut')
# added_ingredients.append(chicken)
# added_ingredients.append(rice)
# added_ingredients.append(oil)
# protein_ingredients.append(chicken)
# protein_ingredients.append(ground_beef)
# protein_ingredients.append(tuna)
# carb_ingredients.append(rice)
# carb_ingredients.append(noodle)
# carb_ingredients.append(bread)
# fat_ingredients.append(oil)
# fat_ingredients.append(cheese)
# fat_ingredients.append(pb)

###had to add this so I could test the make meal button with the methods. We can delete this whenever we want if
##we add ingredients by hand
#fc = 3
#pc = 3
#cc = 3
########################################################################################################################


#vanity, yo
us = tkinter.Label(window,text="Program by: William Brugato and Josh Mendoza, Version: 0.9001", font = ('Arial',7,'italic'),fg='orange')
us.grid(row=3,column = 1)
#button to quit the program
tkinter.Button(window, text="Quit", background = 'red',command = window.quit).grid(row=3,column=2,pady=4)

window.mainloop()

