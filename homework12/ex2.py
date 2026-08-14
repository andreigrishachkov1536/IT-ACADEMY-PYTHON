def limit_calls(limit, message, default):
    def decorator(func):
        calls = 0

        def wrapper(*args, **kwargs):
            nonlocal calls

            if calls >= limit:
                print(message)
                return default

            calls += 1
            return func(*args, **kwargs)

        return wrapper

    return decorator


@limit_calls(
    limit=3,
    message="Лимит вызовов исчерпан!",
    default=None
)
def get_data(name, age):
    print(f"Получаем данные: {name}, {age}")
    return f"{name}: {age}"


print(get_data("Иван", 20))
print(get_data("Анна", 25))
print(get_data("Петр", 30))
print(get_data("Мария", 22))
print(get_data("Олег", 35))


"""На доп условие не хватило"""