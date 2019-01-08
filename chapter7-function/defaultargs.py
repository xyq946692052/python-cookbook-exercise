def foo(a, b=None):
    if b is None:
        b = []
        b.append(a)
    return b

print(foo(1))
print(foo(2))
print(foo(1,2))

