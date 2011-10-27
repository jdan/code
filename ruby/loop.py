i = 2
sum = 0

def isprime(n)
  if n == 2
    return True
  else
    for i in (3..Math.sqrt(n)).step(2)
      if n % i == 0
        return False
    return True

while i < 2000000
  if isPrime(i)
    sum += i
  i += 1
  
puts sum