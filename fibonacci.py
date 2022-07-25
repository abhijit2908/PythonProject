def fibonacci(x: int) -> int:
    """Return the 'n'th fibonacci number"""
    if 0 <= x <= 1:
        print(x)
        return x
    a = 0
    b = 1
    for v in range(x-1):
        v = a + b
        b = a
        a = v
        print(v)
    return v

fibonacci(10)
fibonacci(5)

