n = int(input("Enter n: "))
while n < 0:
    n = float(input("Enter n: "))
for a in range(1, n + 1):
    for b in range(1, n + 1):
        for c in range(1, n + 1):
            #if (b > a):
                if (a * a + b * b == c * c):
                    print(a, b, c)
