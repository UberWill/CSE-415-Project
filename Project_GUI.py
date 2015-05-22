import tkinter
import Project_Classes

#global variables used to make the ingredient objects
i_name = ""
i_cals = 0
i_pro = 0
i_carbs = 0
i_fat = 0

#A list of all added ingredients (they have their own attributes - see IngredientNode class)
added_ingredients = []

#setting up the window
window = tkinter.Tk()
window.title("Diet Plan")
window.wm_iconbitmap('icon.ico')

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

#initialize the Add Intgredients section
tkinter.Label(window, text = "Add Ingredients", font= ("Helvetica",16)).grid(row=0,column=1,sticky='w')
#the name input area
tkinter.Label(window, text = "Name",).grid(row=1,sticky='e')
name = tkinter.Entry(window)
name.grid(row=1,column=1)
#total calories input area
tkinter.Label(window, text = "Total Calories").grid(row=2,sticky='e')
total_calories = tkinter.Entry(window)
total_calories.grid(row=2,column=1)
#protien input area
tkinter.Label(window, text = "Protien (g)").grid(row=3,sticky='e')
protein = tkinter.Entry(window)
protein.grid(row=3,column=1)
#carbs input area
tkinter.Label(window, text= "Carbs (g)").grid(row=4,sticky='e')
carbs = tkinter.Entry(window)
carbs.grid(row=4,column=1)
#fat input area
tkinter.Label(window, text="Fat (g)").grid(row=5,sticky='e')
fat = tkinter.Entry(window)
fat.grid(row=5,column=1)


#function to get input and store it
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
    if i_name == '' or i_cals == '' or i_pro == '' or i_carbs == '' or i_fat == '':
        top = tkinter.Toplevel()
        top.title("Error")
        top.geometry('{}x{}'.format(180,100))
        top.wm_iconbitmap('error.ico')
        msg = tkinter.Message(top, text = "Please do not leave an ingredient entry blank.")
        msg.pack()
        errbutton = tkinter.Button(top, text = "Dismiss", command = top.destroy)
        errbutton.pack()
    else:
        global added_ingredients
        added_ingredients.append(Project_Classes.IngredientNode(i_name,i_cals,i_pro,i_carbs,i_fat))
        name.delete(0,'end')
        total_calories.delete(0,'end')
        protein.delete(0,'end')
        carbs.delete(0,'end')
        fat.delete(0,'end')

        counter.configure(state='normal')
        counter.delete(1.0,'end')
        counter.insert('end',len(added_ingredients))
        counter.configure(state='disabled')

#the method that takes the user input for goals and stores it
def set_goals():
    global g_cals
    global g_fat
    global g_pro
    global g_carbs
    g_cals = calories_goal.get()
    g_fat = fat_goal.get()
    g_pro = protein_goal.get()
    g_carbs = carb_goal.get()
    if g_cals == '' or g_fat == '' or g_pro == '' or g_carbs == '':
        top = tkinter.Toplevel()
        top.title("Error")
        top.geometry('{}x{}'.format(180,100))
        top.wm_iconbitmap('error.ico')
        msg = tkinter.Message(top, text = "Please do not leave a goal entry blank.")
        msg.pack()
        errbutton = tkinter.Button(top, text = "Dismiss", command = top.destroy)
        errbutton.pack()
    else:
        calories_goal.configure(state='disabled')
        fat_goal.configure(state='disabled')
        protein_goal.configure(state='disabled')
        carb_goal.configure(state='disabled')
        r1.configure(state='disabled')
        r2.configure(state='disabled')

        goal_set.configure(state='normal')
        goal_set.insert('end',"GOAL SET!")
        goal_set.configure(state='disabled')

#the method that resets the goals so the user can input new ones
def reset_goals():
    calories_goal.configure(state='normal')
    fat_goal.configure(state='normal')
    protein_goal.configure(state='normal')
    carb_goal.configure(state='normal')
    r1.configure(state='normal')
    r2.configure(state='normal')

    calories_goal.delete(0,'end')
    fat_goal.delete(0,'end')
    protein_goal.delete(0,'end')
    carb_goal.delete(0,'end')

    goal_set.configure(state='normal')
    goal_set.delete(1.0,'end')
    goal_set.configure(state='disabled')

#the method that sets the restrictions to prevent accidental changes
def set_restrictions():
    c1.configure(state='disabled')
    c2.configure(state='disabled')
    c3.configure(state='disabled')
    restrictions_set.configure(state='normal')
    restrictions_set.insert('end',"RESTRICTIONS SET!")
    restrictions_set.configure(state='disabled')

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


#button to finish the adding of ingredient
tkinter.Button(window, text="Add Ingredient",
               command = get_ingredient).grid(row=6,column=1,sticky='w',pady=4)

#number of ingredients added, counter
tkinter.Label(window,text="Ingredients\nAdded:").grid(row=7,column=0,sticky='e')
counter = tkinter.Text(window,height=1,width=3)
counter.grid(row=7,column=1,sticky='w')
counter.insert('end',"0")
counter.configure(state='disabled')

#initialize the goals section
tkinter.Label(window, text = "Goals", font= ("Helvetica",16)).grid(row=8,column=1,sticky='w')
#the calorie goal input area
tkinter.Label(window, text = "Calories",).grid(row=9,sticky='e')
calories_goal = tkinter.Entry(window)
calories_goal.grid(row=9,column=1)
#the fat goal input area
tkinter.Label(window, text = "Fat (%)",).grid(row=10,sticky='e')
fat_goal = tkinter.Entry(window)
fat_goal.grid(row=10,column=1)
#the protein goal input area
tkinter.Label(window, text = "Protein (%)",).grid(row=11,sticky='e')
protein_goal = tkinter.Entry(window)
protein_goal.grid(row=11,column=1)
#the carb goal input area
tkinter.Label(window, text = "Carb (%)",).grid(row=12,sticky='e')
carb_goal = tkinter.Entry(window)
carb_goal.grid(row=12,column=1)
#the lose weight or gain weight options
r1 = tkinter.Radiobutton(window, text='Lose Weight', variable = weight_goal, value = 'lose')
r1.grid(row=13,column=1)
r2 =tkinter.Radiobutton(window, text='Gain Weight', variable = weight_goal, value = 'gain')
r2.grid(row=14,column=1)
#button to set goals
tkinter.Button(window, text="Set Goals",
               command = set_goals).grid(row=15,column=0,sticky='e',pady=4)
#space to let the user know their goals have been accepted by the program
goal_set = tkinter.Text(window,height=1,width=9)
goal_set.grid(row=15,column=1)
goal_set.configure(state='disabled')
#button to reset goals
tkinter.Button(window, text="Reset Goals",
               command = reset_goals).grid(row=16,column=0,sticky='e',pady=4)


#the area the user will select certain restrictions from
tkinter.Label(window, text = "Restrictions", font= ("Helvetica",16)).grid(row=8,column=5,sticky='w')
#all the restrictions
c1 = tkinter.Checkbutton(window, text = "Vegetarian", variable = vegetarian)
c1.grid(row = 9, column = 5,sticky='w')
c2 = tkinter.Checkbutton(window, text = "Peanut Allergy", variable = peanut_allergy)
c2.grid(row = 10, column = 5,sticky='w')
c3 = tkinter.Checkbutton(window, text = "Lactose Intolerant", variable = lactose_intolerant)
c3.grid(row = 11, column = 5,sticky='w')
#button to set restrictions
tkinter.Button(window, text="Set Restrictions",
               command = set_restrictions).grid(row=12,column=5,sticky='w',pady=4)
#space to let the user know their restrictions have been accepted by the program
restrictions_set = tkinter.Text(window,height=1,width=17)
restrictions_set.grid(row=12,column=6)
restrictions_set.configure(state='disabled')
#button to reset restrictions
tkinter.Button(window, text="Reset Restrictions",
               command = reset_restrictions).grid(row=13,column=5,sticky='w',pady=4)


#button to quit the program
tkinter.Button(window, text="Quit", background = 'red',command = window.quit).grid(row=99,column=99,pady=4)

window.mainloop()

