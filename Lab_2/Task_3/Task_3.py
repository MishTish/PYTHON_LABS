def lies_in_circle(x, y, r, a, b):
    if(x-a)**2 + (y-b)**2 < r**2:
        return True
    else:
        return False

while True:
    try:
        circle1 = float(input("enter circle center x: "))
        circle2 = float(input("enter circle center y: "))
        circle3 = float(input("enter circle radius: "))
        p1 = float(input("enter pont P x: "))
        p2 = float(input("enter pont P y: "))
        f1 = float(input("enter point F x: "))
        f2 = float(input("enter point F y: "))
        l1 = float(input("enter point L x: "))
        l2 = float(input("enter point L y: "))
        break
    except ValueError:
        print("not a valid input")

if lies_in_circle(circle1, circle2, circle3, p1, p2):
    print("point p is inside the circle")
else:
    print("point p is not inside the circle")
if lies_in_circle(circle1, circle2, circle3, f1, f2):
    print("point f is inside the circle")
else:
    print("point f is not inside the circle")
if lies_in_circle(circle1, circle2, circle3, l1, l2):
    print("point l is inside the circle")
else:
    print("point l is not inside the circle")
