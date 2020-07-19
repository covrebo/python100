from functools import wraps
from decorators import make_html, strong, emphasis, uppercase, proxy, trace, make_html_input


# @repeat(num_times=4)
# def greet(name):
#     print(f'Hello {name}')


@make_html_input('p')
@make_html_input('br')
def get_text(text):
    """Text to display on website"""
    return text

print(get_text('hello'))

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