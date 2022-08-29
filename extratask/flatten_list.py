L = [['a', ['cat'], 2],[[[3]], 'dog'], 4, 5]

def flatten(L):
    assert type(L) is list
    if type(L[0]) == list:
        result = flatten(L[0]) + flatten(L[1:])
    else:
       result = [L[0]] + flatten(L[1:])

    return result

lis = [['a', ['cat'], 2],[[[3]], 'dog'], 4, 5]
print(flatten(lis))