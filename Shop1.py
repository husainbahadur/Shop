MainMeal = ("Chicken Burger", "Beef Burger", "Cheese Burger")
Snack = ("Crisps", "Chocolate", "Gum")
Drink = ("Coke", "Sprite", "Water")
MainMealCos = 3
SnackCos = 2
DrinkCos = 1
# MainMeal for £3, Snack for £2, Drink for £1

def MainMealPlug():
    if input("Do you want a Main Meal? ") == "yes":
        print("Our Main Meal options are", ', '.join(MainMeal))
        print("Please pick what you would like:")
        MainMealch = input()
        if MainMealch in MainMeal:
            print(MainMealch, "That will be £", MainMealCos)

def SnackPlug():
    if input("Do you want a Snack?") == "yes":
        print("Our Sanck options are", ', '.join(Snack))
        print("Please pick what you would like:")
        Snackch = input()
        if Snackch in Snack:
            print(Snackch, "That will be £", SnackCos)

def DrinkPlug():
    if input("Do you want a Drink? ") == "yes":
        print("Our Drink options are", ', '.join(Drink))
        print("Please pick what you would like:")
        Drinkch = input()
        if Drinkch in Drink:
            print(Drinkch, "That will be £", DrinkCos)







print("HELLO, Welcome to Macds")
MainMealPlug()