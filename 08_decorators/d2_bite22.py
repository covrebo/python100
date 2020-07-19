from functools import wraps


def make_html(element):
    def decorator_make_html(func):
        """Wraps text in html tags"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            return f'<{element}>' + func(*args, **kwargs) + f'</{element}>'
        return wrapper
    return decorator_make_html


@make_html('p')
@make_html('strong')
def get_text(text):
    """Text to display on website"""
    return text

# print(get_text('hello'))

# @strong
# @emphasis
# def greet():
#     return 'Hello'
#
#
# print(greet())

# @trace
# def say(name, line):
#     """Test function"""
#     return f'{name}: {line}'
#
# say('Jane', 'Hello, World')
# print(say.__doc__)




# def make_html(*args):
#     print(args)
#     def wrap(f):
#         def wrapped_f(*args):
#             tag = f(*args)
#             text = f(*args)
#             print(f'<{tag}>{text}</{tag}>')
#         return wrapped_f
#     return wrap
#
# @make_html('p')
# @make_html('strong')
# def get_text(text):
#     return text
#
# get_text('markup')