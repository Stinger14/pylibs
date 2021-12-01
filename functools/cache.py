import functools

@functools.cache
def factorial(n):
    return n * factorial(n - 1) if n else 1

print(factorial(10))        # no previously cached result, makes 11 recursive calls

print(factorial(12))        # makes two new recursive calls, the other 10 are cached
