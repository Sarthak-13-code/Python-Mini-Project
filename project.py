# tracker.py
# Name: Sarthak Gupta (2501350021)
# Date: October 8, 2025
# Project Title: Daily Calorie Tracker

print("Welcome to the Daily Calorie Tracker!")

meal_names = []
calorie_amounts = []

try:
    num_meals = int(input("No. Of meals : "))
except ValueError:
    print("Invalid number. Please enter a whole number like 2, 3 etc.")
    exit() 

print("\n Meals")
for i in range(num_meals):
    meal_name = input(f"Meal #{i+1} Name: ")
    calorie_amount = int(input(f"Calorie Count in '{meal_name}' "))
    meal_names.append(meal_name)
    calorie_amounts.append(calorie_amount)

print("\nThank you ! All meals are added\n")

total_calories = sum(calorie_amounts)
if num_meals > 0:
    average_calories = total_calories / num_meals
else:
    average_calories = 0
daily_limit = int(input("Whats your daily calorie limit:  "))

print("\n--Your Calorie Analysis--")
if total_calories > daily_limit:
    print(f"Warning! daily limit ({daily_limit} calories) exceeded.")
    print(f"{total_calories - daily_limit} calories over the limit!")
else:
    print(f"Great job! ({daily_limit} calories) not exceeded.")
    calories_left = daily_limit - total_calories
    print(f"you can take {calories_left} calories more.")

print("\n--- Meal Summary ---")
print(f"{'Meal Name':<20} {'Calories'}") 
print("-----------------------------")

for i in range(num_meals):
    print(f"{meal_names[i]:<20} {calorie_amounts[i]}")

print("-----------------------------")
print(f"{'Total:':<20} {total_calories}")
print(f"{'Average:':<20} {average_calories:.2f}")
print("-----------------------------")