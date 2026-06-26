MainMeal = ("Chicken Burger", "Beef Burger", "Cheese Burger")
Snack = ("Crisps", "Chocolate", "Gum")
Drink = ("Coke", "Sprite", "Water")
MainMealCos = 3
SnackCos = 2
DrinkCos = 1
total_cost = 0

def order_item(prompt, items, cost):
    global total_cost
    if input(prompt) == "yes":
        print("Our options are", ', '.join(items))
        choice = input("Please pick what you would like: ")
        if choice in items:
            print(choice, "That will be £", cost)
            total_cost += cost

def main():
    print("HELLO, Welcome to Macds")
    order_item("Do you want a Main Meal? ", MainMeal, MainMealCos)
    order_item("Do you want a Snack? ", Snack, SnackCos)
    order_item("Do you want a Drink? ", Drink, DrinkCos)
    print("Your total is £", total_cost)
    print("BYYY, HAVE A GREAT DAY :)")
    quit()

main()