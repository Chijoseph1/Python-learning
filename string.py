order = " boy "
girl = "car"
strip_line=order.strip()
print(strip_line.upper())
print(strip_line[0:1])
print(f"my name is {order} i have a {girl}")
book = "my name is chibuzor"
split_line= book.split(" ")
join_line = "-".join(split_line)
print(join_line)

def book(a,v= 10, b= 57):
    return a+v+b

print(book(12,8,v=3))