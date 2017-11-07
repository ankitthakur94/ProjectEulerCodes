##### Problem statement ############
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
####################################


######## Agorithm 1 ( Brute Force ) #######
 ## try multiplying all numbers of n-length digits and check if that product is a palindrome ##


 ############################# Algo -2 (This one ) #######################
 ## Say num_of_digits = 3
 ## Generate min product possible ( 100*100 = 10000 ) and max product possible (999*999 = 998001 ).
#     All the possible products of 3 digit nums will lie in this range only.
## palindromes_list = Iterate on all nums b.w this range ( 10000 -> 998001) and collect all palindromes. (O(n))
## iterate on palindromes_list and check if number is a product of 3 digit nums <== O(p*sqrt(n))
#        For this
#             min_divisor_of_3_digit_len = 100
#             max_divisor_of_3_digit_len = 999  .. we can optimize this max to = sqrt(number)
#             try dividing num with range (min_divisor_of_3_digit_len to max_divisor_of_3_digit_len)
#             if divisor and remainder are of length = 3 then we have got our answer
#
######################################################

import math 

num_of_digits = 3
print ( " Running for number of digits : ", num_of_digits )

def get_max_num(n):
    ''' returns the maximum possible number which can be formed by n digit numbers '''
    max_num = 0
    for i in range(0,n):
        max_num += (9*(10**i))
    return max_num


def get_min_num(n):
    ''' returns the minimum possible number which can be formed by n digit numbers '''
    min_num = 0
    min_num = (get_max_num(n-1) + 1)
    return min_num


def get_range(n):
    return (get_min_num(n) , get_max_num(n))

def get_product_range(n):
    ''' Range of product of 2 n digit numbers ''' 
    min, max = get_range(n)
    print ( " Num range : ", min , ", " ,max )
    min_product = min*min
    max_product = max*max
    return (min_product, max_product)

def is_panlindrome(i):
    ''' Checks if a number i is a palindrome or not '''
    is_palindrome = 1
    i_str = str(i)
    len_i_str = float(len(i_str))
    iterate_till = int(math.ceil(len_i_str/2))
    for index in range(0,iterate_till):
        if ( i_str[index] != i_str[-1-index] ):
            is_palindrome = 0
    return is_palindrome

def generate_palindromes_for_product_of_n_digit_nums(n):
    min, max = get_product_range(n)
    print ( " Product Range : " , min , " , " , max )
    for i in (range(max+1, min, -1)):
        if (is_panlindrome(i)):
            yield i

def  are_nums_of_same_digit_len (num1, num2, num_of_digits):
    len1 = len(str(int(num1)))
    len2 = len(str(int(num2)))
    if ( len1 == len2) :
            if (len1 == num_of_digits) :
                return 1
    else:
        return 0

def is_product_of_n_digit_nums (i, num_of_digits):
    ''' Checks if 'i' is a product of 2 'num_of_digits' number of digits. '''
    is_product_of_n_digit_nums = 0
    
    min_divisor = get_min_num(num_of_digits)
    # Need to check only till sqrt(i). Otherwise repetition of divisors will occur
    max_divisor = int(math.ceil(math.sqrt(i)))
   
    num_of_divisors_to_check = max_divisor - min_divisor

    for divisor in range(min_divisor, max_divisor+1):
        if (i % divisor == 0):
            remainder =  int(i/divisor)
            print ( " ", divisor , "x", remainder)
            if (are_nums_of_same_digit_len(divisor, remainder, num_of_digits)):
                is_product_of_n_digit_nums = 1
                print ( " ", divisor , "x", remainder)
    
    return is_product_of_n_digit_nums
    
    

def get_max_palindrome_for_product_of_num_of_digits (num_of_digits):
    max_palindrome_for_product_of_num_of_digits = 0
    g = generate_palindromes_for_product_of_n_digit_nums(num_of_digits)
    for i_palindrome in g:
        print (" Got palindrome : ", i_palindrome)
        if ( is_product_of_n_digit_nums (i_palindrome,  num_of_digits) ):
            max_palindrome_for_product_of_num_of_digits = i_palindrome
            print ( " max_palindrome_for_product_of_num_of_digits " , max_palindrome_for_product_of_num_of_digits )
            break


    return max_palindrome_for_product_of_num_of_digits


get_max_palindrome_for_product_of_num_of_digits(num_of_digits)


