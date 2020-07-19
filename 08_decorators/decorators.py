import functools


# def repeat(num_times):
#     def decorator_re


def make_html(func):
    """Wraps text in html tags"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return '<strong>' + func(*args, **kwargs) + '</strong>'
    return wrapper


def make_html_input(tag):
    def decorator_make_html_input(func):
        """Wraps text in html tags"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return f'<{tag}>' + func(*args, **kwargs) + f'</{tag}>'
        return wrapper
    return decorator_make_html_input



def strong(func):
    """Wraps text in html tags"""
    @functools.wraps()
    def wrapper(*args, **kwargs):
        return '<strong>' + func(*args, **kwargs) + '</strong>'
    return wrapper


def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

def proxy(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
              f'with {args}, {kwargs}')

        original_result = func(*args, **kwargs)

        print(f'TRACE: {func.__name__}() '
              f'returned {original_result!r}')

        return original_result
    return wrapper