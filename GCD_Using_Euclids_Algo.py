####################################################
## Objective : Compute the Greatest Common Divisor (GCD) of 2 numbers (a,b)
####################################################


####################################################
#Theory
####################################################
#Greatest common divisor for 2 numbers (a,b) is the largest number which can divide both 'a' and 'b'.


####################################################
# Algo 1 ( Suboptimal : O(sqrt(n) )
####################################################
#	Find all factors of the smaller of (a,b) (say 'a' is smaller)  	< Time Complexity (sqrt(n))
#		f1, f2, f3 .. 
#	Divide 'b' by each of these factors and find out common factors of 'a' and 'b'
#	Output the largest Common Factor
#
####################################################
#	Time  Complexity : Sqrt(n) ( which looks very good ) 
####################################################


####################################################
#Algo 2 : (Optimal : Euclid's Algorithm : O(log(b)) ; where b is smaller of a,b
####################################################
#	Say out of a,b ; a < b
#	a = divisor
#	b = dividend
#	while (divisor != 0) :
#		Divide b(dividend) / a (Divisor) 
#		remainder (r) = dividend % divisor
#		dividend = divisor 
#		divisor = remainder
#
#	This loop exits when divisor = 0.
#	In that case dividend is the GCD.
#	If a,b do not have any common divisor ( say both are primes ), then GCD = 1

#Time Complexity : 
#	All other operations are constant
#	We need to determine how many number of times while loop is running
#	It was proved that while loop runs = number of digits in 'b' ( i.e smaller of a,b )
#	and 
#	So Time Complexity = O(log(b))
# 
######## Note : 
#	we say that out of a,b ; smaller one (say a) is divisor and larger one (say b) is dividend. ( so we do b / a )
#	It is not necessary to assign it this way.
#	even if assignment was done in reverse order, (say dividend < divisor), then remainder produced in this case will be = dividend
#	In the next iteration, this remainder becomes divisor and previous divisor becomes dividend.
#	so things automatically shuffle up.

####################################################



def euclids_gcd_iterative (a,b):
	dividend = max(a,b)
	divisor = min(a,b)
	while (divisor != 0):
		remainder = dividend % divisor
		dividend = divisor
		divisor = remainder
	return dividend

def euclids_gcd_recursive (a,b):
	# I am assuming a is dividend and b is divisor (i.e a / b ; and a > b)
	# Even if a was < b, it will correct itself in the next iteration automatically
	if (b == 0):
		return a
	# new dividend = previous divisor 
	# new divisor = remainder of previous division.
	return euclids_gcd_recursive (b,a%b)

print ( ' -- Iterative -- ' )
print ('euclids_gcd_iterative (10,15)', euclids_gcd_iterative (10,15) )
print ('euclids_gcd_iterative (7,29)', euclids_gcd_iterative (7,29) )
print ('euclids_gcd_iterative (80,10)',  euclids_gcd_iterative (80,10))
print ('euclids_gcd_iterative (546,353)',  euclids_gcd_iterative (546,353))
print ('euclids_gcd_iterative (2432,2534)', euclids_gcd_iterative (2432,2534) )

print ( ' -- Recursive -- ' )
print ('euclids_gcd_recursive (10,15)', euclids_gcd_recursive (10,15) )
print ('euclids_gcd_recursive (7,29)', euclids_gcd_recursive (7,29) )
print ('euclids_gcd_recursive (80,10)',  euclids_gcd_recursive (80,10))
print ('euclids_gcd_recursive (546,353)',  euclids_gcd_recursive (546,353))
print ('euclids_gcd_recursive (2432,2534)', euclids_gcd_recursive (2432,2534) )





