def filter_prime(a, b):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    return list(filter(is_prime, range(a, b+1)))


a = int(input())
b = int(input())
prime_numbers = filter_prime(a, b)
print(prime_numbers)
