sumOfDivs [] = 0
sumOfDivs n = do
    if ((n `mod` 3) == 0 || (n `mod` 5) == 0)
main = do
    print(sumOfDivs 999)