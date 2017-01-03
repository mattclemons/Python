x = float(raw_input("Enter a value for x: "))
a = float(raw_input("Enter a value for a: "))

while True:
    print x
    y = (x + a/x) / 2
    if y == x:
        break
    x = y
