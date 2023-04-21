from functools import partial

pow(3,2)
pow(4,2)

square = partial(pow, exp=2)
cube = partial(pow, exp=3)

print(square(4))
print(cube(4))


from functools import wraps

def decorator(func):
    @wraps(func)
    def processor():
        func()
    return processor

@decorator
def somefunc():
    """docstring of somefunc"""
    return 0

