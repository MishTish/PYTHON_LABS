def nat_numbers(n, a, b, c):
    nat_num_list = []
    for i in range(n+1):
        if i != 0 and i % a == 0 and i % b == 0 and i % c == 0:
            nat_num_list.append(i)
        else:
            continue
    return nat_num_list

while True:
    try:
        N = int(input("enter n: "))
        A = int(input("enter number a: "))
        B = int(input("enter number b: "))
        C = int(input("enter number c: "))
        break
    except ValueError:
        print("not a valid input")
print(f"natural numbers less or equal than {N} that are divisible by {A}, {B} and {C}")
print(nat_numbers(N, A, B, C))
