from math import sqrt, ceil, gcd
def modulo(coso, somu, n):
    # bien so mu thanh binary
    bin = []
    while (somu != 0):
        if (somu % 2 == 0):
            bin.insert(0,0)
            somu /= 2
        else:
            bin.insert(0,1)
            somu -= 1
            somu /= 2
    # tinh so du
    mod = 1
    for i in range (len(bin)):
        mod = ((mod * mod) % n)
        if (bin[i] == 1):
            mod = ((mod * coso) % n)
    return mod

def isPrime(n):
    if (n <= 11):
        arr =[2,3,5,7,11]
        if (n in arr):
            prime = True
        else:
            prime = False
    else:
        #Find k and q 
        q = n - 1
        k = 0
        while(q % 2 == 0):
            q /= 2
            k += 1
        #Use miller-rabin for 10 times
        for i in range(n-11, n-1):
            prime = False
            if (pow(i, int(q), n) == 1):
                prime = True
            else:
                for j in range(k):
                    if (modulo(i, (2**j) * q, n) == n-1):
                        prime = True
                        break

            if (prime == False):
                break
    return prime

def FermatFact(n):
    if(n % 2 == 0):
        return [int(n/2), 2]
    else:
        a = ceil(sqrt(n))
        if (a * a == n):
            return [a,a]
        else:
            while(True):
                b2 = a * a - n
                b = int(sqrt(b2))
                if(b * b == b2):
                    break
                else:
                    a += 1
        return [a - b, a + b]

def isSemiPrime(n):
    # Fermat factorize n
    a = FermatFact(n)[0]
    b = FermatFact(n)[1]
    #check prime of factors
    if (isPrime(a) and isPrime(b)):
        return True
    else:
        return False

# Calculate inverse modulo using extended Euclidean
def inverseMod(d, n):
    t, newt = 0, 1
    r, newr = n, d
    
    while(newr != 0):
        q = r // newr
        r, newr = newr, (r % newr)
        t, newt = newt, (t - q*newt)
    if r > 1:
        print("not in vertible")
    else:
        if (t < 0):
            t += n
        return int(t)




