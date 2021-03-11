def iloraz(ciag):
    return("q =", ciag[1]/ciag[0])

def nty_wyraz(ciag, n, q):
    return("a", n, "=", ciag[0]*pow(q,n-1))

def suma(ciag, n, q):
    return("Suma n wyrazów:", ciag[0]*(1-pow(q,n))/(1-q))