def pyth(n):
    if n <= 1:
        return n
    else:
        return (pyth(n-1)**2) + (pyth(n-2)**2)

print(pyth(3))