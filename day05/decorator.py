import functools

def log(level: str="DEBUG"):
    def log_level(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{level}]调用了 {greet.__name__}")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return log_level

@log(level="INFO")
def greet(name: str):
    return f"你好, {name} "

print(greet("张三"))
print(greet.__name__)