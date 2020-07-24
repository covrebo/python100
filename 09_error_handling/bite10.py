
num = 4
den = 2

def positive_divide(numerator, denominator):
    try:
        q =  numerator / denominator
    except ZeroDivisionError:
        return 0
    if q < 0:
        raise ValueError
    return q

quotient = positive_divide(num, den)

print(quotient)