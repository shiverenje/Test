def manipulate_data(n):
    if type(n) != list:
        return 'Only list allowed'
    else:
        l = []
        summation = 0
        count = 0
        for i in n:
            if i >= 0:
                count += 1
            else:
                summation = summation + i
        l = [count, summation]
        return l


l = [-1, -5, -5, 1, 8]
print(manipulate_data(l))
