# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 08:345:47 2025

@author: IAN CARTER KULANI

"""

from colorama import Fore
import pyfiglet
import os
font=pyfiglet.figlet_format("Random Prime Number Generator")
print(Fore.GREEN+font)

import random

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to generate 6 random prime numbers
def generate_prime_numbers():
    primes = []
    while len(primes) < 6:
        num = random.randint(1, 100)  # Generate random number between 1 and 100
        if is_prime(num):
            primes.append(num)
    return primes

# Generate and print the 6 prime numbers
prime_numbers = generate_prime_numbers()
print("Generated 6 random prime numbers:", prime_numbers)
