#Program for Factorial number.
def factorial(n):
    '''Enter the value of n, and get the factoial of nth value.'''
    if (n==1 or n==0):
        return 1 
    else:
        return n * factorial(n-1)
print(f'''{"by @himanshuaryan".center(117)}
{"Factorial Number ".center(60)}
\n{factorial.__doc__}\n''')
n = int(input('Enter the number : ')) # Input value
print("\nFactorial of",n, "is :",factorial(n)) 