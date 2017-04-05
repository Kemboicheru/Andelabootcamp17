def generate_prime_numbers(number):
    primenumbers = []
    if number <= 1:
        return primenumbers
        primenumbers.append(number)
    else:
        for x in xrange(2, number + 1):
            if prime(x):
                primenumbers.append(x)
                
        return primenumbers
    
def prime(number):
    if number == 2 or number == 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    elif number % 5 == 0:
        return False
    else:
        return True
    


