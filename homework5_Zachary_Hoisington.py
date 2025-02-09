# Homework 5 - List and Tuple Exercises

# --- List Exercise ---
# Create a list with 6 items
my_list = ["dog", "bat", "rat", "bird", "cat", "lizard"]

# Print all items in the list
print("The items in the list are:", my_list)

# Print the first two items using slicing
print(f"The first two items in the list are: {my_list[0]}, {my_list[1]}")

# Print the middle two items using slicing
middle_index = len(my_list) // 2
print(f"The middle two items in the list are: {my_list[middle_index-1]}, {my_list[middle_index]}")

# Print the first and last items using indexing
print(f"The first and last items in the list are: {my_list[0]}, {my_list[-1]}")

# --- Tuple Exercise ---
# Define a tuple with five basic foods on a menu
menu = ("French Fries", "Cheese board", "Pizza", "Foie Gras", "Chili")

# Print each item using a for loop
print("Menu:")
for item in menu:
    print(item)

# Updating the menu by replacing two items
new_menu = ("BLT-NEW", "Muffuletta-NEW", "Pizza", "Foie Gras", "Chili")

# Print each item on the revised menu using a loop
print("Updated menu:")
for item in new_menu:
    print(item)