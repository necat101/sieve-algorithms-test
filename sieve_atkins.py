#!/usr/bin/env python3
"""
Sieve of Atkins - Prime Number Generator
=========================================

The Sieve of Atkins is a modern algorithm for finding all prime numbers
up to a specified integer. Created by A. O. L. Atkins and Daniel J. Bernstein
in 2004, it is more efficient than the Sieve of Eratosthenes for large numbers.

Time Complexity: O(n / log log n)
Space Complexity: O(n)

Algorithm Overview:
1. Initialize results array with False values
2. Mark numbers as prime candidates using quadratic forms:
   - n = 4x² + y² where n % 12 == 1 or 5
   - n = 3x² + y² where n % 12 == 7
   - n = 3x² - y² where x > y and n % 12 == 11
3. Eliminate squares of primes
4. Add 2 and 3 to results
"""

import math
from typing import List

def sieve_of_atkins(limit: int) -> List[int]:
    """
    Generate all prime numbers up to limit using Sieve of Atkins.
    
    Args:
        limit: Upper bound for prime search (inclusive)
    
    Returns:
        List of prime numbers up to limit
    """
    if limit < 2:
        return []
    
    # Initialize sieve array
    is_prime = [False] * (limit + 1)
    
    # Put in candidate primes using quadratic forms
    # n = 4x² + y²
    sqrt_limit = int(math.sqrt(limit)) + 1
    for x in range(1, sqrt_limit):
        for y in range(1, sqrt_limit):
            # First quadratic: 4x² + y²
            n = 4 * x * x + y * y
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                is_prime[n] = not is_prime[n]
            
            # Second quadratic: 3x² + y²
            n = 3 * x * x + y * y
            if n <= limit and n % 12 == 7:
                is_prime[n] = not is_prime[n]
            
            # Third quadratic: 3x² - y² (x > y)
            if x > y:
                n = 3 * x * x - y * y
                if n <= limit and n % 12 == 11:
                    is_prime[n] = not is_prime[n]
    
    # Eliminate composites by sieving
    for n in range(5, sqrt_limit):
        if is_prime[n]:
            # Mark multiples of squares as non-prime
            k = n * n
            for multiple in range(k, limit + 1, k):
                is_prime[multiple] = False
    
    # Collect results
    primes = []
    if limit >= 2:
        primes.append(2)
    if limit >= 3:
        primes.append(3)
    
    for n in range(5, limit + 1):
        if is_prime[n]:
            primes.append(n)
    
    return primes


def main():
    """Demo the Sieve of Atkins"""
    print("=" * 60)
    print("SIEVE OF ATKINS - Prime Number Generator")
    print("=" * 60)
    print()
    
    # Test with different limits
    test_limits = [30, 100, 1000]
    
    for limit in test_limits:
        primes = sieve_of_atkins(limit)
        print(f"Primes up to {limit}:")
        print(f"  Count: {len(primes)}")
        print(f"  Primes: {primes[:20]}{'...' if len(primes) > 20 else ''}")
        print()
    
    # Performance test
    import time
    limit = 1000000
    print(f"Performance test: Finding primes up to {limit:,}...")
    start = time.time()
    primes = sieve_of_atkins(limit)
    elapsed = time.time() - start
    print(f"  Found {len(primes):,} primes in {elapsed:.3f} seconds")
    print(f"  Last 10 primes: {primes[-10:]}")
    print()
    print("=" * 60)


if __name__ == "__main__":
    main()
