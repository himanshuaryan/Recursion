#Program for Fibonacci sequence
def fib_seq(n):
   '''Enter the value of n, and get fibonacci sequence of nth value.'''
   if n==0:
       return 0
   if n <= 1:
       return 1
   else:
       return(fib_seq(n-1) + fib_seq(n-2))

print(f'''{"by @himanshuaryan".center(117)}
{"Fibonacci sequence ".center(60)}
\n{fib_seq.__doc__}''')
num = int(input("\nEnter the number : ")) # Input value
print("\nFibonacci Number of",num, "is : ", fib_seq(num))
print("\nFibonacci Sequence to", f"{num}th", "is :- ")
for i in range(num+1):
    print(fib_seq(i))