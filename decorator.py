def log(func):
    def wrapper(*args, **kwargs):
        print(f"Функция {func.__name__} была вызвана")
        return func(*args, **kwargs)
    return wrapper