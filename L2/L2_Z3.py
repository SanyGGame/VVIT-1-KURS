def is_prime(number):
    flag = True
    for i in range(2, number):
        if number//i == number/i:
            flag = False
            break
    return flag

print(is_prime(113))
print(is_prime(144))
        
