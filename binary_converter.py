def binary_converter(n):
    kit = ''
    check = (int, float)
    if isinstance(n, check):
        if n == 0:
            return '0'
        elif n < 0:
            return 'Invalid input'
        elif n > 255:
            return 'Invalid input'
        else:
            while 1 <= n <= 255:
                y = divmod(n, 2)
                n, x = y[0], y[1]
                kit += str(x)
                r = kit[::-1]
            return r
    else:
        return 'Invalid input'

print(binary_converter(52))
