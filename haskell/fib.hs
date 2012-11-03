module Fibonacci where

fibTuple :: (Integer, Integer, Integer) -> (Integer, Integer, Integer)
fibTuple (x, y, 0) = (x, y, 0)
fibTuple (x, y, n) = fibTuple (y, x + y, n - 1)

fibFirst :: (Integer, Integer, Integer) -> Integer
fibFirst (x, _, _) = x

fib :: Integer -> Integer
fib n = (fibFirst . fibTuple) (0, 1, n)

res = [fib x | x <- [1..100]]

main :: IO ()
main = do
  print res
