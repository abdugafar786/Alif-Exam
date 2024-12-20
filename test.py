from main import ShopingList

# 1. Create shopping list instances
list1 = ShopingList("apple", 20)
list2 = ShopingList("lemon", 10)

# 2. Add new products to the list
list1.create()
list2.create()

# 3. Display the shopping list
print("Shopping list:")
list1.show_shopping_list()

# 4. Update a product
print("\nUpdating a product:")
list1.update("apple", 20, "banana", 25)
list1.show_shopping_list()

# 5. Delete a product
print("\nDeleting a product:")
list1.delete("lemon", 10)
list1.show_shopping_list()

# 6. Calculate the total price
print("\nTotal price:")
total_price = list1.get_total_price()
print(f"Total: {total_price} $")
