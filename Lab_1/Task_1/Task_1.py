# 1
while True:
    try:
        n1 = int(input("enter a whole number: "))
        n2 = int(input("enter a whole number: "))
        n3 = float(input("enter a floating-point number: "))
        n4 = float(input("enter a floating-point number: "))

        print("\nthe numbers are:")
        print(n1, n2, n3, n4)
        break
    except ValueError:
        print("not a valid number")

# 2
addedX = n1 + n3
subtractedX = n1 - n3
multipliedX = n1 * n3
dividedX = n1 / n3
powerX = n1 ** n3
wholeNumberX = n1 // n3
remainderX = n1 % n3
listX = [addedX, subtractedX, multipliedX, dividedX, powerX, wholeNumberX, remainderX]

print("\nlist of results of operations with n1 and n3:")
listPrint = [["+", "-", "*", "/", "**", "//", "%"], [addedX, subtractedX, multipliedX, dividedX, powerX, wholeNumberX, remainderX]]

s = [[str(e) for e in row] for row in listPrint]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print('\n'.join(table))

# 3
print("\nlist length: ", len(listX))
print("\neven elements: ", listX[0:2])

# 4
print("\nswapping elements 2 and 5:")
listX[1], listX[4] = listX[4], listX[1]
print(listX)

# 5
name = input("\nEnter your last and first name: ")
print("\nYour full name is:", name)

print("\nLab task is complete.")
print("we created variables, gave them values, done operations with them, with results being saved to a list.")
print("then we've done other operations with the list.")
print("lastly, we've recorded our name in a variable.")


