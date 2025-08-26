#Create a shopping cart program that will continuously ask the user for a food product and the price of that product.
# Have an exit clause if the user wishes to stop adding more products to their cart.
# The program should then display the food items and the  total cost of all products in the cart.

foods = []
prices = []
total_cost = 0

while True:
    food = input("Enter a food product (or type 'exit' to finish): ")
    if food.lower() == 'exit':
        break
    price = float(input(f"Enter the price of {food}: "))
    
    foods.append(food)
    prices.append(price)
    total_cost += price

print("----------YOUR CART:----------")

for food in foods:
    print(food, end=", ")

print("\n")
print("Total cost of products in the cart:", total_cost)