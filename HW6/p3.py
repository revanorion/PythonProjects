import random
from itertools import islice


def gen_rndtup(n):
    while True:
        yield (random.randint(0, n), random.randint(0, n))


gen = gen_rndtup(7)

lst = [p for p in islice(gen, 10) if p[0] + p[1] >= 7 // 2]
print(lst)

result = ((random.randint(0, 7), random.randint(0, 7)) for x in range(10))
for r in result:
    print(r)
