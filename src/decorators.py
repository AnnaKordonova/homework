from functools import wraps
from typing import Any, Optional


def log(filename: Optional[str] = None) -> Any:
    """Декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""

    def decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:

            log_text_start = f"Начало работы функции '{func.__name__}'\n"
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_text_start)
            else:
                print(log_text_start, end="")

            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(str(result) + "\n")
                else:
                    print(str(result), end="")
                log_text_end = f"Конец работы функции '{func.__name__}'\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_text_end)
                else:
                    print(log_text_end, end="")
                return result
            except Exception as e:
                log_text_error = f"'{func.__name__}' error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_text_error)
                else:
                    print(log_text_error, end="")
                raise

        return wrapper

    return decorator
