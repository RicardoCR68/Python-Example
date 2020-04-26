'''
Exemplo de Mat Dis I
'''

def fact(n):
    if n >= 1:
        return n*(fact(n-1))
    else:
        return 1

def comb(n, k):
    res = fact(n)/((fact(n-k))*(fact(k)))
    return res

def arrj(n, k):
    res = ((fact(n))/(fact(n-k)))
    return res

def a(n = 7, n2 = 15):
    res_sum = 0
    for k in range(n-1, 2, -1):
	    res_k = comb(n, n-k)*arrj(n2, k)
	    res_sum += res_k
	    print("C({0}, {1}) x A({4}, {2}) = {3}".format(n, n-k, k, res_k, n2))
    return res_sum

print(a())
