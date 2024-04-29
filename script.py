def is_prime(num):
    """
    Check if a number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
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
    """
    Find prime numbers within a given range.

    Args:
        start (int): The start of the range.
        end (int): The end of the range.

    Returns:
        list: A list of prime numbers within the specified range.
    """
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes
