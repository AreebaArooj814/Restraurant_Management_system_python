#  define menu 
menu = { "Pizza" : 50,
        "Pasta" : 40,
        "Burger" : 60,
        "Salad" : 70,
        "Coffee": 80,
}
print("Welcome to Python Restaurant")
print("Pizza : Rs 50\nPasta : Rs 40\nBurger: Rs 60\nSalad : Rs 70\nCofee : Rs 80 ")
order_total = 0
while True:
    item = input("Enter the name of item you want to be order: ").title()
    if item == "Done":
        break
    
    if item in menu:
        order_total += menu[item]
        print(f"Your ordered item {item} has been added to your order")
    else:
        print(f"Ordered item {item} is not avialable!")
print(f"The total ammount of item to pay is Rs{order_total}")