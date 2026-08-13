menu_price = 4.50 #global variable 
count = 0

def serve_customer(name):
    # We can read the global variable naturally
    print(f"Charging {name} ₦{menu_price:.2f} for their latte.")

serve_customer("Alice")

# use and changing the global variable 
# modifing global keyword variable 

def dish_food(new_price):
    global menu_price
    menu_price = new_price
    print(f"The final price is ₦{menu_price:2f}")

dish_food(500)

def add_value():
    global count
    count = count +1
    print(count)
add_value()

# when a function is inside a function you can call the variable for the function inside the other function using nonlocal EXAMPLE

def outer_variable():
    x ="myname"
    def inner_variable():
        nonlocal x
        x = "modified"
    inner_variable()
    print(x)
outer_variable()