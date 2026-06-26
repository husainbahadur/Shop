MainMeal = ("Chicken Burger", "Beef Burger", "Cheese Burger")
Snack = ("Crisps", "Chocolate", "Gum")
Drink = ("Coke", "Sprite", "Water")
MainMealCos = 3
SnackCos = 2
DrinkCos = 1
# MainMeal for £3, Snack for £2, Drink for £1

print("HELLO, Welcome to Macds")
print("Do you want a Main Meal?")
if input() == "yes": #1st Yes
    print("Our Main Meal options are", ', '.join(MainMeal))
    print("Please pick what you would like")
    MainMealch = input()
    if MainMealch in MainMeal:
        print(MainMealch, "That will be £", MainMealCos)

print("Do you also want a Snack?")
if input() == "yes":
    print("Our Snack options are", ', '.join(Snack))
    print("Please pick what you would like")
    Snackch = input()
    if Snackch in Snack:
        print(MainMealch,"and a", Snackch, "Now your total is £", MainMealCos + SnackCos)

print("Do you also want a Drink?")
if input() == "yes":
    print("Our Drink options are", ', '.join(Drink))
    print("Please pick what you would like")
    Drinkch = input()
    if Drinkch in Drink:
        print(MainMealch, Snackch, "and ", Drink, "Thats all, Your Total is £", MainMealCos + SnackCos + DrinkCos)