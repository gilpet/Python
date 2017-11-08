#Python 2.7.10
def fOnly(list):
    return [x for x in list if isinstance(x, float)]

def fNonPrimes(n):
    return list(filter(lambda x: not is_prime_number(x), range(2, n + 1)))

def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
	return False
    return True
