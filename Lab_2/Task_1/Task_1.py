def rectangle_area(wid, len):
    return wid*len


while True:
    try:
        rec1wid = float(input("enter first rectangle width: "))
        rec1len = float(input("enter first rectangle length: "))
        rec2wid = float(input("enter second rectangle width: "))
        rec2len = float(input("enter second rectangle length: "))
        rec3wid = float(input("enter third rectangle width: "))
        rec3len = float(input("enter third rectangle length: "))
        break
    except ValueError:
        print("not a valid input")
print("rectangle 1 area:", rectangle_area(rec1wid, rec2len), ", rectangle 2 area:", rectangle_area(rec2wid, rec2len), ", rectangle 3 area:", rectangle_area(rec3wid, rec3len))
