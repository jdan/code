def convertbase(n, _from, _to):
    # convert to base 10
    digits = list(str(n))[::-1]
    i = 0
    for exp in range(0, len(digits)):
        i += int(digits[exp]) * (_from ** exp)
        
    # convert to base _to
    n = ''
    while i > 0:
        n += str(i % _to)
        i /= _to
    return int(n[::-1])
