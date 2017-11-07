
start_num = 1
end_num = 1000
divisors_to_check = (3,5)

def is_num_a_multiple_of (num_to_check, divisor):
    is_multiple = False
    rem = (num_to_check) % (divisor)
    if (rem == 0):
        is_multiple = True
    return is_multiple
    

def is_num_a_multiple_of_any_of (num_to_check, *divisors):
    is_multiple_of_any_of_divisors = False
    for divisor in divisors:
        is_multiple_of_any_of_divisors = (is_multiple_of_any_of_divisors| (is_num_a_multiple_of(num_to_check, divisor)))
    return is_multiple_of_any_of_divisors

    

def get_required_nums ():
    sum = 0
    for num in range(start_num, end_num):
        if (is_num_a_multiple_of_any_of (num, *divisors_to_check)):
            sum += num
    return sum 



#sum = get_required_nums()

#print ( " Starting from : ", start_num, " upto ", end_num, " . Multiples of ", divisors_to_check )
#print ( " Sum : " , sum ) 



