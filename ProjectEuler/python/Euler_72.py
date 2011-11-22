def main():
    total = 0
    for i in range(2, 1000001):
        total += totient(i)
        
    print 'Total: %s' % total
    
def totient(k):
    n, d, t = 1, 1, k
    curr = 2
    while k > 1:
        if k % curr == 0:
            k /= curr
            while k % curr == 0:
                k /= curr
            
            n *= curr - 1
            d *= curr
            
            curr = 2
        else:
            curr += 1
            
    return t * n / d
    
if __name__ == '__main__':
    main()