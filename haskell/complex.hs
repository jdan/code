-- Complex Numbers Module
-- Jordan Scales (scalesjordan@gmail.com)
-- 21 November 2012

module Complex where

-- Complex consists of a real and imaginary part
--   for our purposes, they are represented as /Floats/

data Complex = Complex Float Float deriving (Eq, Show)

-- extract the real part
real :: Complex -> Float
real (Complex r _) = r

-- extract the imaginary part
imag :: Complex -> Float
imag (Complex _ i) = i

-- magnitude of the complex number
--   covers by `abs`, but that needs to return a Complex
magnitude :: Complex -> Float
magnitude (Complex r i) = sqrt $ r^2 + i^2

-- compliment
compliment :: Complex -> Complex
compliment (Complex r i) = Complex r (-i)

-- `Num` instance methods to allow (+) and (*)
--   and even (-), (^), etc.
instance Num Complex where
  -- (a + bi) + (x + yi) => (a + x) + (b + y)i
  Complex r1 i1 + Complex r2 i2 = Complex (r1 + r2) (i1 + i2)

  -- (a + bi) * (x + yi) => (ax - by) + (ay + bx)i
  Complex r1 i1 * Complex r2 i2 = Complex (r1 * r2 - i1 * i2) (r1 * i1 + r2 * i2)

  -- same as `magnitude`, but returns a Complex
  abs (Complex r i) = Complex (sqrt $ r^2 + i^2) 0

  -- vague implementation
  signum (Complex r i)
    | r == 0    = 0
    | r >  0    = 1
    | otherwise = -1

  -- any integer simply becomes the real part, imaginary is 0
  fromInteger i = Complex (fromInteger i) 0

-- mandel (a+bi) <precision> => True / False
mandel :: Int -> Complex -> Bool
mandel p c = mandel' p c 0
  where mandel' 0 _ _ = True
        mandel' p c z
          | (magnitude z) > 2 = False
          | otherwise         = mandel' (p - 1) c (z^2 + c)

