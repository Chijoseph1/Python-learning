# lambda function a nameless, single line helper function
# price and tax parameter 
cal_total = lambda price, tax : price * (1 + tax)

print(cal_total(4.50,0.08))

# map the value x + 50 loop inside everything in the list and added 50 to it that how it work 
# And iterate a list applies the tool to every item, return a lazy map 

menu = [9.0, 93, 56]
new_menu = list(map(lambda x : x + 50, menu))
print(new_menu)

# filter It pass through every time in the list through a boolean list, if the text return true the test pass if it return false that means it false.

menu = [
    {"name":"malta", "price":50},
    {"name":"fanta", "price":50},
    {"name":"coke", "price":30}
]

check_price = list(map(lambda menu:menu["price"]< 50,menu))
print(check_price)

# sorted() to sort

menu = [
    {"name":"malta", "price":50},
    {"name":"fanta", "price":50},
    {"name":"coke", "price":30}
]
alpha = ["a","b","f","c"]
sort_price=sorted(menu,key=lambda value:value["price"])
print(sort_price)

alpha_text = sorted(alpha, key=lambda v : v)
print(alpha_text)