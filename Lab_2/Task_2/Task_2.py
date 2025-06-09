import math

def compare_hypotenuses(tri1a, tri1b, tri2a, tri2b):

    tri1hyp = math.sqrt(tri1a ** 2 + tri1b ** 2)
    tri2hyp = math.sqrt(tri2a ** 2 + tri2b ** 2)
    print("\ntriangle 1 hypotenuse = ", tri1hyp)
    print("triangle 2 hypotenuse = ", tri2hyp)
    if tri1hyp > tri2hyp:
        print("\nTriangle 1 has the longer hypotenuse.")
    elif tri1hyp < tri2hyp:
        print("\nTriangle 2 has the longer hypotenuse.")
    else:
        print("\nBoth triangles have the same hypotenuse length.")


tri1a = float(input("enter first triangle side a: "))
tri1b = float(input("enter first triangle side b: "))
tri2a = float(input("enter second triangle side a: "))
tri2b = float(input("enter second triangle side b: "))

compare_hypotenuses(tri1a, tri1b, tri2a, tri2b)