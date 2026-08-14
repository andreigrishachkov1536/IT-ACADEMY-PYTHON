def repeat(times:int, separator="---"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []

            for i in range(times):
                result = func(*args, **kwargs)
                results.append(str(result))

            print(separator.join(results))

            return result

        return wrapper

    return decorator

@repeat(times=5, separator="---")
def greet(name):
    return f"Привет, {name}!"

greet("Иван")

@repeat(times=2, separator="=")
def add(a, b):
    return a + b

add(5, 3)