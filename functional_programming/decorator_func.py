import functools
def fence(func):
    # print(f"fence({func}) is called!")
    @functools.wraps(func)
    def add_fence(val):
        # print(f"add_fence({val}) called!")
        print("+"*10)
        func(val)
        print("-"*10)
    
    # print(f"Returning add_fence")
    return add_fence

# @fence
def log(val):
    # print(f"log({val}) called")
    print(val)

# @fence
def root(num):
    print(pow(num, 0.5))

root(25)
log("hello")