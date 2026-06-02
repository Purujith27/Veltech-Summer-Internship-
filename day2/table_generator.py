def times_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

for _ in range(3):
    num = int(input("Enter a number: "))
    times_table(num)