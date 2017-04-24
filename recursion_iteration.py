def replicate_recur(times, data):
    L = []
    check = (int, float)
    check2 = (int, float, str)
    if isinstance(times, check) and isinstance(data, check2):
        try:
            if times == 0 or times < 0:
                return L
            else:
                value = replicate_recur(times - 1, data)
                value.append(data)
                return value
        except:
            raise ValueError
    else:
        raise ValueError


def replicate_iter(times, data):
    L = []
    check = (int, float)
    check2 = (int, float, str)
    if isinstance(times, check) and isinstance(data, check2):
        try:
            while times > 0:
                L.append(data)
                times -= 1
            return L
        except:
            raise ValueError
    else:
        raise ValueError


print(replicate_recur(2, 5))
print(replicate_iter(3, 5))
