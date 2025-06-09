import math

def quadrilateral_area(X, Y, Z, T):

    area1 = 0.5 * X * Y

    d = math.sqrt(X ** 2 + Y ** 2)
    s = (Z + T + d) / 2
    area2 = math.sqrt(s * (s - Z) * (s - T) * (s - d))

    area = area1 + area2
    return area

while True:
    try:
        x = float(input("enter quadrilateral side x length: "))
        y = float(input("enter quadrilateral side y length: "))
        z = float(input("enter quadrilateral side z length: "))
        t = float(input("enter quadrilateral side t length: "))
        break
    except ValueError:
        print("not a valid input")

print("quadrilateral area =", quadrilateral_area(x, y, z, t))