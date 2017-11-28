### Problem :
#	- Find all factors of a number 'n'
#############


## Optimal Algo : ( We only need to check numbers from 1 > sqrt(n) )
#	for i = 1 -> sqrt(n)
#		if n % i == 0
#			i is a factor.
#			n/i is a factor.
	
import math

n = 56
list_of_factors = []
for i in range(1,int(math.sqrt(n))):
	if ( n % i == 0 ) :
		list_of_factors.append(i)
		if ( i != n/i ) :
			list_of_factors.append(n/i)

print ( " Checked till : " , i ) 
list_of_factors.sort()
print (list_of_factors)




