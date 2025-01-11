def spacing(x):
    y = ''
    for i in x:
        y = y + i +' '
    return y

def reverse_str(x):
    y = ''
    for i in x:
        y = i + y
    return y

def censored(x):
    y = '*'*(len(x))
    return y
