# Problem Statememt : Sum of even valued terms in fibonacci sequence (for f(n) = 4 million)

from prob1 import is_num_a_multiple_of_any_of

max_fib_num = 4000000
divisors_to_check = (2)

def gen_fibo_nums ():
    a = 0
    b = 1
    while (b <= max_fib_num):
        yield b
        next = a + b
        a = b
        b = next

def gen_fibo_nums_a_multiple_of ():
    fib_nums = gen_fibo_nums()
    for f_num in fib_nums:
        print ( " fib num : ", f_num )
        if ( is_num_a_multiple_of_any_of (f_num, divisors_to_check) ):
            yield f_num


def sum_given_num ():
    sum = 0
    fib_num_series = gen_fibo_nums_a_multiple_of()
    for some_fib_num in fib_num_series:
        sum += some_fib_num
        print ( "       Sum : ", sum ) 
    return sum

sum = sum_given_num()
print ( " Sum of even valued terms in fibonacci sequence (for f(n) = 4 million = " , sum )



