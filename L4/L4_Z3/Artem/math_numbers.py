def is_prime(x):
    flag = True
    for i in range(2,x):
        if x//i==x/i:
            flag = False
            break
    return flag

def fibonacci(x):
    list = [0,1]
    y1 = 1
    y2 = 0
    for i in range(2,x):
        list.append(list[i-1]+list[i-2])
    return list
        
