import math
import collections


class PrimeSeq(collections.Iterator):
    def __init__(self, max):
        self.__primes = []
        self.max = max
        return

    def __next__(self):
        count = len(self.__primes)
        if count == 0:
            self.__primes.append(2)
            return 2
        n = self.__primes[count - 1]
        while n < self.max:
            result = calculate_prime(n)
            if result:
                self.__primes.append(result)
                return result
            n += 1
        raise StopIteration


def calculate_prime(n=2):
    # Wilson's theorem
    result = math.floor((math.factorial(n) % (n + 1)) / n) * (n - 1) + 2
    if result != 2:
        return result
    return 0


def prime_gen(n):
    prime = 2
    while prime < n:
        result = calculate_prime(prime)
        if result:
            yield result
        prime += 1


def main():
    for p in prime_gen(100):
        print(p)
    primes_lst = [p for p in PrimeSeq(100)]
    print(primes_lst)


main()
