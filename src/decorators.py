from functools import wraps


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log_text = f"Начало работы функции '{func.__name__}'\n"
            if filename:
                with open(filename, 'a', encoding='utf-8') as file:
                    file.write(log_text)
            else:
                print(log_text, end='')

            try:
                result = func(*args, **kwargs)
                log_text = f"Конец работы функции '{func.__name__}'\n"
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(log_text)
                else:
                    print(log_text, end='')
                return result
            except Exception as e:
                log_text = f"'{func.__name__}' error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(log_text)
                else:
                    print(log_text, end='')
        return wrapper
    return decorator
