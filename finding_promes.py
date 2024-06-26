def is_prime(num):
    """Function to check if a number is prime."""
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Generate prime numbers up to a specified limit
def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Example usage:
print(generate_primes(20))  # Output: [2, 3, 5, 7, 11, 13, 17, 19]
