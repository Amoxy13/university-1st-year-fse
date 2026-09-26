
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))


same_color = (x1 + y1) % 2 == (x2 + y2) % 2

cell_color = "White" if (x1 + y1) % 2 != 0 else "Black"

if same_color:
    print("YES")
    print(cell_color)
else:
    print("NO")
