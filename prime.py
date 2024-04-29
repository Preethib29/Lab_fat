def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

print("Prime numbers between", start_range, "and", end_range, "are:")
print(find_primes(start_range, end_range))
