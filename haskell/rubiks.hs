-- Rubik's Cube Module
-- by Jordan Scales
-- 11 January 2013

module RubiksCube where

data Color = Blue | Green | Orange | Red | White | Yellow

-- Row and Column types
type Row = (Color, Color)
type Column = (Color, Color)

-- Just a 2x2 cube for now
-- Top Left, Top Right, Bottom Left, Bottom Right
data Face = Face Color Color Color Color

-- Top, Back, Right, Front, Left, Down
data Cube = Cube Face Face Face Face Face Face

-- A solved cube with white in the front and red on top
solvedCube :: Cube
solvedCube =
  Cube
    (Face Red Red Red Red)
    (Face Yellow Yellow Yellow Yellow)
    (Face Green Green Green Green)
    (Face White White White White)
    (Face Blue Blue Blue Blue)
    (Face Orange Orange Orange Orange)

-- Some aliases for cube notation
u = upClockwise
b = backClockwise
r = rightClockwise
f = frontClockwise
l = leftClockwise
d = downClockwise

u' = triple upClockwise
b' = triple backClockwise
r' = triple rightClockwise
f' = triple frontClockwise
l' = triple leftClockwise
d' = triple downClockwise

-- Displaying colors (individual cubits)
instance Show Color where
  show Blue = "B"
  show Green = "G"
  show Orange = "O"
  show Red = "R"
  show White = "W"
  show Yellow = "Y"

-- Display faces
instance Show Face where
  show (Face a b c d) = (show a) ++ (show b) ++ "\n" ++ (show c) ++ (show d)

-- Displaying the cube
instance Show Cube where
  show (Cube up back right front left down) =
    join
      (
        (place [emptySquare, split (show up) '\n', emptySquare, emptySquare]) ++
        (place [split (show left) '\n', split (show front) '\n',
                split (show right) '\n', split (show back) '\n']) ++
        (place [emptySquare, split (show down) '\n', emptySquare, emptySquare])
      )
      '\n'

      where
        emptySquare = ["  ", "  "]
        place = foldl (\acc x -> next acc x) [""]

-- Applies a list of move functions to a cube (in order)
applyMoves :: Cube -> [Cube -> Cube] -> Cube
applyMoves c [] = c
applyMoves c (move:rest) = applyMoves (move c) rest

-- Functions to turn faces of a cube
upClockwise :: Cube -> Cube
upClockwise (Cube up back right front left down) =
  Cube
    (clockwise up)
    (changeTopRow back  $ topRow left)
    (changeTopRow right $ topRow back)
    (changeTopRow front $ topRow right)
    (changeTopRow left  $ topRow front)
    down

backClockwise :: Cube -> Cube
backClockwise (Cube up back right front left down) =
  Cube
    (changeTopRow up $ rightColumn right)
    (clockwise back)
    (changeRightColumn right $ invert $ bottomRow down)
    front
    (changeLeftColumn left $ invert $ topRow up)
    (changeBottomRow down $ leftColumn left)

rightClockwise :: Cube -> Cube
rightClockwise (Cube up back right front left down) =
  Cube
    (changeRightColumn up $ rightColumn front)
    (changeLeftColumn back $ invert $ rightColumn up)
    (clockwise right)
    (changeRightColumn front $ rightColumn down)
    (left)
    (changeRightColumn down $ invert $ leftColumn back)

frontClockwise :: Cube -> Cube
frontClockwise (Cube up back right front left down) =
  Cube
    (changeBottomRow up $ invert $ rightColumn left)
    back
    (changeLeftColumn right $ bottomRow up)
    (clockwise front)
    (changeRightColumn left $ topRow down)
    (changeTopRow down $ invert $ leftColumn right)

leftClockwise :: Cube -> Cube
leftClockwise (Cube up back right front left down) =
  Cube
    (changeLeftColumn up $ invert $ rightColumn back)
    (changeRightColumn back $ invert $ leftColumn down)
    right
    (changeLeftColumn front $ leftColumn up)
    (clockwise left)
    (changeLeftColumn down $ leftColumn front)

downClockwise :: Cube -> Cube
downClockwise (Cube up back right front left down) =
  Cube
    up
    (changeBottomRow back $ bottomRow right)
    (changeBottomRow right $ bottomRow front)
    (changeBottomRow front $ bottomRow left)
    (changeBottomRow left $ bottomRow back)
    (clockwise down)

-- Rotates a face clockwise
clockwise :: Face -> Face
clockwise (Face a b c d) = (Face c a d b)

-- Row operations (getters and setters sorta)
topRow :: Face -> Row
topRow (Face a b _ _) = (a, b)

bottomRow :: Face -> Row
bottomRow (Face _ _ c d) = (c, d)

changeTopRow :: Face -> Row -> Face
changeTopRow (Face _ _ c d) (a', b') = (Face a' b' c d)

changeBottomRow :: Face -> Row -> Face
changeBottomRow (Face a b _ _) (c', d') = (Face a b c' d')

-- Column operations (getters and setters sorta)
leftColumn :: Face -> Column
leftColumn (Face a _ c _) = (a, c)

rightColumn :: Face -> Column
rightColumn (Face _ b _ d) = (b, d)

changeLeftColumn :: Face -> Column -> Face
changeLeftColumn (Face _ b _ d) (a', c') = (Face a' b c' d)

changeRightColumn :: Face -> Column -> Face
changeRightColumn (Face a _ c _) (b', d') = (Face a b' c d')

invert :: (a, a) -> (a, a)
invert (a, b) = (b, a)

triple :: (Cube -> Cube) -> (Cube -> Cube)
triple f = (f . f . f)

-- Helper method to display two adjacent strings
-- used to print the cube
next :: [[Char]] -> [[Char]] -> [[Char]]
next a b = next' a b aWidth bWidth
  where
    aWidth = maximum $ map length a
    bWidth = maximum $ map length b

    -- base case
    next' [] [] _ _ = []

    -- AA + CC = AACC
    -- BB        BB
    next' (line:rest) [] _ width =
        (line ++ (take width $ repeat ' ')) : (next' rest [] 0 width)

    -- AA + CC = AACC
    --      DD     DD
    next' [] (line:rest) width _ =
        ((take width $ repeat ' ') ++ line) : (next' [] rest width 0)

    -- AA + CC = AACC
    -- BB   DD   BBDD
    next' (a:as) (b:bs) aWidth bWidth =
        (a ++ b) : (next' as bs aWidth bWidth)

-- Helper method to split a string
split :: [Char] -> Char -> [[Char]]
split = split' []
  where
    split' built [] _ = [built]
    split' built (char:rest) splitChar
      | char == splitChar = built : (split' [] rest splitChar)
      | otherwise         = split' (built ++ [char]) rest splitChar

-- Helper method to join an array of strings with a given character
join :: [[Char]] -> Char -> [Char]
join [] _ = []
join (x:[]) _ = x
join (x:xs) c = (x ++ [c]) ++ (join xs c)
