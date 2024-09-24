def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

if __name__ == '__main__':
    @memoize
    def fibonacci(n):
        if n < 2:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    print(fibonacci(10))
    print(fibonacci(20))
    print(fibonacci(30))
    print(fibonacci(40))
    print(fibonacci(50))    