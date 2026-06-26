Shop, Python Ordering System
A command-line ordering system built in Python, simulating a fast food shop where a customer can order a Main Meal, Snack, and Drink and get a running total. This was a personal project I built and improved across 4 versions to practice core Python concepts.
Language: Python
Latest version: Shop3.py
What the project does
The program runs in the terminal and walks the user through ordering items from a menu. It asks if they want a Main Meal, a Snack, and a Drink, shows the available options, takes their choice, and keeps a running total of what they've ordered. At the end it prints their total cost and says goodbye.
How it evolved, version by version
Shop.py, The starting point
This was the first version. It worked, but it was all written in one block from top to bottom, no functions, no structure, just sequential if statements and input() calls. The logic for each menu item (Main Meal, Snack, Drink) was just repeated three times in a row.
The biggest problem was that the total wasn't actually tracked properly, each section just printed the cost of that individual item rather than adding everything up. So by the end you didn't actually get a proper total, you just got three separate prices printed out.
It did the job for a first attempt but it was messy and hard to follow.
Shop1.py, Learning about functions
The first thing I changed was breaking the code into functions, MainMealPlug(), SnackPlug(), and DrinkPlug(). Each one handled its own menu category separately instead of everything being piled into one block.
This was me getting to grips with how functions work in Python, the idea that you can wrap a chunk of logic into something reusable and call it whenever you need it. The code was cleaner and easier to read as a result.
The total tracking still wasn't fixed at this point though, each function just printed the price of that item individually, so you still couldn't see a combined total at the end.
shop2.py, Tracking the total with a global variable
This version introduced a TotalCos variable and used global to let each function update it. So every time the user ordered something, the cost got added to TotalCos, and at the end the program printed the combined total.
This was the first version where the program actually behaved like a proper ordering system, you could order multiple things and see what you owe in total, which was the whole point.
I also added a goodbye message when the user said "no" to an item, which made it feel a bit more finished.
Using global worked, but it's not considered the cleanest approach in Python, the next version deals with that.
Shop3.py, The final version, cleaner and more reusable
This is the version I'm most happy with. The biggest change was replacing the three separate functions (MainMealPlug, SnackPlug, DrinkPlug) with a single reusable function called order_item(). Instead of repeating the same logic three times, I just pass in the prompt, the list of items, and the cost, and the function handles the rest.
Python
So instead of three separate functions doing the same thing with different variable names, I have one function that works for any menu category. That's the concept of writing DRY code, Don't Repeat Yourself.
I also wrapped everything in a main() function and called it at the bottom, which is standard practice in Python and makes it clear where the program starts.
Python
The code went from 45 lines in shop2.py down to 27 lines in Shop3.py, shorter, cleaner, and easier to extend if I wanted to add more menu categories later.
What I learned from this project
The main thing I took away from building this was how much structure matters in code. The first version worked, but it was already becoming hard to follow and it would have been a nightmare to extend. Each version taught me something new, functions, global variables, and then how to make functions actually reusable by passing arguments in rather than hardcoding everything.
The jump from shop2.py to Shop3.py was the most satisfying, going from three functions doing the same thing to one function that handles all three cases just by being passed different data. That's the kind of thinking I want to keep building on.
What I'd improve next
Replace global total_cost with returning values from the function instead, using global variables works but it's not the cleanest approach
Add input validation so the program handles unexpected inputs (like typing something that isn't on the menu) rather than just silently moving on
Store the menu items and prices in a dictionary rather than separate tuples and variables, which would make it easier to manage
Let the user see a full receipt at the end showing everything they ordered and the individual prices, not just the total
