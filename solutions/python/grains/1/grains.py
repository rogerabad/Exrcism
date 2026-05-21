def square(number):
    # when the square value is not in the acceptable range
    if number<1 or number>64:
        raise ValueError("square must be between 1 and 64")
    result = 1
    for i in range(number):
        if i == 0:
            result = 1
        else:
            result*=2 
    return result
    
def total():
    result = 1
    totall = 0
    for i in range (64):
        totall += result
        result *= 2
    return totall    
