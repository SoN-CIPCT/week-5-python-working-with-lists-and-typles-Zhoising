# Homework 5 - List and Tuple Exercises


my_list = ["dog", "bat", "rat", "bird", "cat", "lizard"]

print("The items in the list are:", my_list)

print(f"The first two items in the list are: {my_list[0]}, {my_list[1]}")

middle_index = len(my_list) // 2
print(f"The middle two items in the list are: {my_list[middle_index-1]}, {my_list[middle_index]}")

print(f"The first and last items in the list are: {my_list[0]}, {my_list[-1]}")

# --- Tuple Exercise ---

menu = ("French Fries", "Cheese board", "Pizza", "Foie Gras", "Chili")

print("Menu:")
for item in menu:
    print(item)

new_menu = ("BLT-NEW", "Muffuletta-NEW", "Pizza", "Foie Gras", "Chili")

print("Updated menu:")
for item in new_menu:
    print(item)