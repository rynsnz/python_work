def prime_checker(number):

    value_prime = True

    for i in range(2, number):
        if number % i == 0:
            print('Not Prime!')
            value_prime = False
            break
    
    if value_prime:
        print('Prime!')

n = int(input("Check this number: "))
prime_checker(number = n)