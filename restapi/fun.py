def sum(a,b):
    return a+b

def avg(a,b):
    return (a+b)/2

def check_armstrong_number(n):
    digits = str(n)  
    num_digits = len(digits)  
    sum_of_powers = 0
    for digit in digits:
        sum_of_powers += int(digit) ** num_digits
    
    if sum_of_powers == n:
        return f"{n} is an Armstrong number."
    else:
        return f"{n} is not an Armstrong number."
