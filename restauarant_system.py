#  define menu 
menu = { "Pizza" : 50,
        "Pasta" : 40,
        "Burger" : 60,
        "Salad" : 70,
        "Coffee": 80,
}
# Greet 
print("Welcome to Python Restaurant")
print("Pizza : Rs 50\nPasta : Rs 40\nBurger: Rs 60\nSalad : Rs 70\nCofee : Rs 80 ")
order_total = 0
item_1 = input("Enter the name of item you want of order: ").title()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item{item_1} has been added to your order")
else:
    print(f"ordered item {item_1} is not avaiable yet!")

another_order = input("Do you want to add another item?(yes/no)\n")
if another_order == "yes":
    item_2  = input("Enter the name of second item: ").title()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"ordered{item_2} is not avaiable!") 

print(f"The Total amount of items to pay is {order_total}")   