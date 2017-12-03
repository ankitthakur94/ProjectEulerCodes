#################################################
## Objective : 
#################################################
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#################################################


#################################################
#Sol 1 : Brute Force
#################################################
#for i in range(1,,20):
#	if ( i is divisible by all nums from 1 -> 20 )
#	we have found i
#
#################################################
# ### Analysis ###
# to find a number which is divisible by all nums from 1 -> 23 this algo took 750 secs.
#################################################

#################################################
#Sol 2 : Create a unique prime factorization list of the number required.
#################################################
#prime_factors_list_of_required_num = []
#for i = 1 -> 20	( actually we can only go from 11 -> 20, since factors from 1->20 will be included in 11 -> 20		< O(n)
#	prime_factors_list = get_prime_factors_list(i) 										< O(sqrt(n))	
#	if (  prime_factors_list    is_not_a_subset_of   prime_factors_list_of_required_num ):					< log(n) * log(n)
#		add_missing_factors_to prime_factors_list_of_required_num

# Complexity : iterate_on_all_elements (n) * prime_fact (sqrt(n)) * log(n)  * log(n)
#################################################
# ### Analysis ###
# to find a number which is divisible by all nums from 1 -> 23 this algo took 1 sec.
################################################

import time
import math
def measure_execution_time (func):

	def wrapper(*args):
		start_at = time.time()
		to_return = func(*args)
		time_taken = time.time () - start_at
		print ( ' Time Taken : ', time_taken )
		return to_return

	return wrapper

@measure_execution_time
def find_smallest_num_divisible_by_all_nums_till_brute_force (n) :
	''' Returns smallest number divisible by all nums from 1->n '''

	num_to_return = 0
	while (1):

		num_to_return += n

		is_num_divisible_by_range = True
		for i in range (1,n+1):
			if (num_to_return % i != 0):
				is_num_divisible_by_range = False

		if (is_num_divisible_by_range == True):
			break

	return num_to_return




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
	

def return_list_of_unique_elements_in_first_list (list_1, list_2):
	''' Checks if entire list_1 is a subset of list_2. If not returns the remaining elements of list_1 ''' 
	list_2_cpy = list_2[:]

	unique_elements_list = []

	for l1 in list_1:
		if l1 in list_2_cpy:
			index = list_2_cpy.index(l1)
			list_2_cpy.pop(index)
		else:
			unique_elements_list.append(l1)

	#print ( ' List 1 : ', list_1 )
	#print ( ' List 2 : ', list_2 )
	#print ( ' Unique list : ', unique_elements_list )

	return unique_elements_list


def get_num_from_prime_factorization_list (prime_factor_list):
	num_to_return = 1
	for i in prime_factor_list :
		num_to_return = num_to_return*i
	return num_to_return

@measure_execution_time
def find_smallest_num_divisible_by_all_nums_till_n_sol2 (n) :

	# We will form the prime factorization list for the required number.
	prime_factor_list_for_required_num = []

	for i in range(1,n+1):

		# Get prime factors for i.
		prime_factors = get_prime_factors_list (i)

		# See if this prime factorization list is already a part of the prime_factor_list_for_required_num
		unique_factor_list = return_list_of_unique_elements_in_first_list (prime_factors, prime_factor_list_for_required_num) 

		# Add the missing factors to bigger list.
		prime_factor_list_for_required_num.extend (unique_factor_list)
		
	
	num_to_return = get_num_from_prime_factorization_list (prime_factor_list_for_required_num)
	return num_to_return



for i in range(1,41):
	
	print ( ' -- ' ) 
	
	smallest_num_divisible = find_smallest_num_divisible_by_all_nums_till_n_sol2 (i)
	print ( ' Sol 2 : Smallest number divisible from 1 to {} = {} '.format(i, smallest_num_divisible ) , )
	
	#smallest_num_divisible = find_smallest_num_divisible_by_all_nums_till_brute_force (i)
	#print ( ' Brute Force : Smallest number divisible from 1 to {} = {} '.format(i, smallest_num_divisible ) , )
	

















