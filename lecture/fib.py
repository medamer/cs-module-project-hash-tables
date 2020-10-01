# 0 1 1 2 3 5 8 13 21 34 55 ...
#
# fib(0): 0
# fib(1): 1
# fib(n): fib(n-1) + fib(n-2)
#
cache = {}

def fib(n):
	if n <= 1: return n

	if n not in cache:
		cache[n] = fib(n-1) + fib(n-2)

	return cache[n]

for i in range(100):
	print(f'{i:3} {fib(i)}')


"""
def foo(a, x, b):

	cache[(a,x,b)] = ...
"""
