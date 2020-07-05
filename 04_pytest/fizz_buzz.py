
def fizzbuzz(num):
    '''
    Returns a phrase based on the divisibilty of a number by 3 and/or 5.
    :param
        arg1 : num : int to evaluate
    :return:
        str 'fizz buzz' if num is divisible by both 3 and 5
        str 'fizz' if num is divisible by only 3
        str 'buzz' if num is divisible by only 5
        int num of num is not divisible by 3 and/or 5
    '''
    if num % 5 == 0 and num % 3 == 0:
        return f'{num} fizz buzz'
    elif num % 3 == 0:
        return f'{num} fizz'
    elif num % 5 == 0:
        return f'{num} buzz'
    else:
        return num

for num in range(100):
    print(fizzbuzz(num))
