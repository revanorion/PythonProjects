def compute_Pythagoreans(n):
    try:
        n = int(n)
        pythagoreans = [(a, b, c) for a in range(1, n + 1) for b in range(1, n + 1) for c in range(1, n + 1) if
                        (a * a + b * b == c * c)]
        return pythagoreans
    except:
        return []


print(compute_Pythagoreans(input("Enter n: ")))
