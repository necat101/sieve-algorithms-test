#!/usr/bin/env python3
"""
Sieve of Eratosthenes - Prime Number Generator
===============================================

The Sieve of Eratosthenes is an ancient algorithm for finding all prime
numbers up to a specified integer. Created by Eratosthenes of Cyrene
(~276-194 BCE), it remains one of the most efficient ways to find
small primes.

Time Complexity: O(n log log n)
Space Complexity: O(n)

Algorithm Overview:
1. Create a list of consecutive integers from 2 to n
2. Start with first prime (2)
3. Mark all multiples of current prime as composite
4. Move to next unmarked number and repeat
5. Continue until sqrt(n)
"""

from typing import List
import math

def sieve_of_eratosthenes(limit: int) -> List[int]:
    """
    Generate all prime numbers up to limit using Sieve of Eratosthenes.
    
    Args:
        limit: Upper bound for prime search (inclusive)
    
    Returns:
        List of prime numbers up to limit
    """
    if limit < 2:
        return []
    
    # Initialize sieve - True means prime
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    # Sieve process
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            # Mark multiples of i as not prime
            # Start from i² (smaller multiples already marked)
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    
    # Collect primes
    return [i for i in range(2, limit + 1) if is_prime[i]]


def sieve_optimized(limit: int) -> List[int]:
    """
    Optimized version using only odd numbers.
    Reduces memory usage by ~50%.
    """
    if limit < 2:
        return []
    
    # Only track odd numbers: index i represents number 2*i + 1
    size = (limit + 1) // 2
    is_prime = [True] * size
    is_prime[0] = False  # 1 is not prime
    
    for i in range(1, int(math.sqrt(limit)) // 2 + 1):
        if is_prime[i]:
            prime = 2 * i + 1
            # Start marking from prime²
            start = (prime * prime) // 2
            # Step by prime (skip even multiples)
            for j in range(start, size, prime):
                is_prime[j] = False
    
    # Collect primes
    primes = [2] if limit >= 2 else []
    primes.extend([2 * i + 1 for i in range(1, size) if is_prime[i]])
    
    return primes


def main():
    """Demo the Sieve of Eratosthenes"""
    print("=" * 60)
    print("SIEVE OF ERATOSTHENES - Prime Number Generator")
    print("=" * 60)
    print()
    
    # Test with different limits
    test_limits = [30, 100, 1000]
    
    for limit in test_limits:
        primes = sieve_of_eratosthenes(limit)
        print(f"Primes up to {limit}:")
        print(f"  Count: {len(primes)}")
        print(f"  Primes: {primes[:20]}{'...' if len(primes) > 20 else ''}")
        print()
    
    # Compare standard vs optimized
    import time
    limit = 1000000
    
    print(f"Performance comparison for limit = {limit:,}:")
    print("-" * 60)
    
    start = time.time()
    primes1 = sieve_of_eratosthenes(limit)
    time1 = time.time() - start
    print(f"Standard version:  {len(primes1):,} primes in {time1:.3f}s")
    
    start = time.time()
    primes2 = sieve_optimized(limit)
    time2 = time.time() - start
    print(f"Optimized version: {len(primes2):,} primes in {time2:.3f}s")
    print(f"Speedup: {time1/time2:.2f}x")
    print()
    print(f"Last 10 primes: {primes1[-10:]}")
    print()
    print("=" * 60)


if __name__ == "__main__":
    main()
