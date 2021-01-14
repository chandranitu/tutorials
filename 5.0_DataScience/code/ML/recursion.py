def exp(x, n):
    """  Computes the result of x raised to the power of n. """
    if n == 0:
        return 1
    else:
        return x * exp(x, n-1)


exp(2,3)

#make a program of fibonacci series
