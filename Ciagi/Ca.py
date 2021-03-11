def roznica(ciag):
    return("r =", ciag[0]-ciag[1])

def nty_wyraz(ciag,n,r):
    return("a", n, "=", ciag[0]+(n-1)*r)

def suma(ciag,n):
    return("Suma n elementów:", (ciag[0]+ciag[n-1])/2*n)
