MainMeal = ("Chicken Burger", "Beef Burger", "Cheese Burger") 
Snack = ("Crisps", "Chocolate", "Gum")
Drink = ("Coke", "Sprite", "Water")
MainMealCos = 3
SnackCos = 2
DrinkCos = 1
TotalCos = 0

def MainMealPlug():
    global TotalCos
    if input("Do you want a Main Meal? ") == "yes":
        print("Our Main Meal options are", ', '.join(MainMeal))
        print("Please pick what you would like:")
        MainMealch = input()
        if MainMealch in MainMeal:
            TotalCos += MainMealCos
            print(MainMealch, "That will be £", MainMealCos)

def SnackPlug():
    global TotalCos
    if input("Do you want a Snack? ") == "yes":
        print("Our Snack options are", ', '.join(Snack))
        print("Please pick what you would like:")
        Snackch = input()
        if Snackch in Snack:
            TotalCos += SnackCos
            print(Snackch, "That will be £", SnackCos)

def DrinkPlug():
    global TotalCos
    if input("Do you want a Drink? ") == "yes":
        print("Our Drink options are", ', '.join(Drink))
        print("Please pick what you would like:")
        Drinkch = input()
        if Drinkch in Drink:
            TotalCos += DrinkCos
            print(Drinkch, "That will be £", DrinkCos)
            print("Your Total cost is: £", TotalCos)
    elif input() == "no":
        print("BYYY, HAVE A GREAT DAY :)")

print("HELLO, Welcome to Macds")
MainMealPlug()
SnackPlug()
DrinkPlug()