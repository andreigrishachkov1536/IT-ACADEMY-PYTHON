def ignore_duplicates(func):
    last_args = None

    def wrapper(*args, **kwargs):
        nonlocal last_args

        current_args = (args, kwargs)

        if current_args == last_args:
            print("Повторный вызов проигнорирован.")
            return

        last_args = current_args
        return func(*args, **kwargs)

    return wrapper

@ignore_duplicates
def send_message(text):
    print(f"Отправлено: {text}")

send_message("Привет")
send_message("Привет")
send_message("Как дела?")
send_message("Как дела?")
send_message("Привет")