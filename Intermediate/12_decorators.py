# function decorators

def start_end_decorator(func):
    
    def wrapper(*args, **kwards):
        print("start")
        result = func(*args, **kwards)
        print("end")
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

result = add5(10)
print(result)
