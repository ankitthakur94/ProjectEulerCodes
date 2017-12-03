#############################################################
### Objective :
#############################################################

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?
#############################################################



#############################################################
# ALGO (Simple brute Force) ##
#############################################################

# Keep on generating numbers from 1 -> Infinite and check for each one whether it is a prime or not.
# Stop when you have 100001th prime
#############################################################


import matplotlib.pyplot as plt
import math

def is_prime (n):
	#print ( ' Check for prime : ', n )
	
	max_val_to_check = math.ceil(math.sqrt(n)) +1
	is_prime = True
	for i in range (2,max_val_to_check):
		if ( n % i == 0):
			is_prime = False
			#print ( ' Factors : {} and {}'.format( i , n/i) )
	return is_prime

def generate_primes_infi ():
	i = 0
	while (1):
		i += 1
		if ( is_prime (i) ):
			yield i

max_count = 100000
def plot_prime_nums (primes_list):

	x = [i for i in range(1,max_count+1)]
	y = primes_list

	plt.plot(x,y)
	plt.show()


count = 0
primes_list = []
for i in generate_primes_infi ():
	count += 1
	print (' {}th prime = {}'.format(count,i) )
	primes_list.append(i)
	if (count == max_count):
		break

#print (primes_list)

plot_prime_nums (primes_list)





#############################################################
