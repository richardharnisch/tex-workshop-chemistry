def foo(n): #recursive function to determine a Fibonacci number
    fib = 0
    if n >= 2:
        n_min_one = foo(n-1)
        n_min_two = foo(n-2)
    else:
        n_min_one = 1
        n_min_two = 0
    fib = n_min_one + n_min_two
    return fib #return Fibonacci number
    
fib_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for item in fib_list:
    print(foo(fib_list))