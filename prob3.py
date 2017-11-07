## Largest prime factor of number 600851475143 


# Some  terminilogy : 
# Types of numbers :
    # Prime : Have only 2 divisors : 1 & itself.
    # Composite  : Are composed by multiplying 2 other numbers.
    # Unit-1 : Simply the number 1.

# Prime factors :  PFs of a number are the prime numbers which exactly divide the number (i.e remainder =0)
# Integer Factorization/prime factorization : Decomposition of a composite number into a product of smaller integers. If these integers are further restricted to prime numbers, the process is called prime factorization. 
# Ex of prime factorization : 360 : 2 x 2 x 2 x 3 x 3 x 5 
# Note : Every positive number will have a unique prime factorization.
# no efficient, non-quantum integer factorization algorithm is known. 

import math
import timeit

prime_factors = []

def get_prime_factors (n):
    
    print (" Querying all prime factors of : ", n)

    # Get all even prime facttors.
    while (n%2 == 0):
        prime_factors.append(2)
        n = n/2

    # Get all off prime factors.
    start = 3
    end = int(math.sqrt(int(n)))
    for i in list(range(start,end,2)):
            if (n%i == 0):
                prime_factors.append(i)
                n = n/i

    # In this case 'n' is now prime.
    if (n > 2):
        prime_factors.append(n)

    print ((prime_factors))
    return 


timeit.timeit(get_prime_factors (600851475143))



                


