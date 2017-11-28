## Objective : Find the prime factorizaion of a number
######################################################

######################################################
## Theory :
######################################################
# Each number 'n' will have a unique prime factorization.
# Ex : 36 = 2x2x3x3
######################################################


######################################################
## Optimal Algo :
######################################################
# 	for i = 1 -> sqrt(n)
# 		Divide n till it is divisible by i and increase the count of 'i' as a factor, by 1 each time.
#			 n = n/i
#	After the loop exits, either n will be a prime number or 1. 
# 	If it is prime, add that as a final factor.
######################################################

######################################################
## Time Complexity : sqrt(n)
######################################################


import math

def get_prime_factors_list (n):
	''' Returns the list of prime factors of n '''
	prime_factors_list = []
	
	max_range = math.ceil(math.sqrt(n)) +1
	for i in range (2,max_range):
		if ( n % i == 0 ):
			while ( n % i == 0 ):
				n = n/i
				prime_factors_list.append(i)
	
	if ( n != 1 ): # Means the number left is prime. Add it as is.
		prime_factors_list.append(int(n))

	return prime_factors_list 

for n in range(1,11):
	prime_factors = get_prime_factors_list (n)
	print ( ' Prime factors for ' , n , ' = ' , 'x'.join( str(i) for i in prime_factors))


