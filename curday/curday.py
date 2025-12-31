def sum_of_divisors(n):
    total = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            # total += i
            if i != n // i:  # Add the complement divisor if it's different
                v = (n // i) // 2
                total += v
                print(v, total)
    return total

# Given string length
length = 281474976710761

# Calculate the sum of divisors
result = sum_of_divisors(length - 1) + 1

# Exclude the length itself from the sum
# result -= length  # Remove the string length itself

print(f"The sum of all amplitudes for the string length {length} is: {result}")
