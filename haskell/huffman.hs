-- Huffman Encoding Module
-- by Jordan Scales
-- 4 November 2012

module Huffman where
import BinaryTree

type Entry = ([Char], Integer)

-- computes the frequency of each letter in a given string
letterFrequency :: [Char] -> [Entry]
letterFrequency = letterFrequency' []
  where
    -- helper function with TCO
    letterFrequency' ls []     = ls
    letterFrequency' ls (x:xs) = letterFrequency' (increment ls x) xs

    -- increments a character entry in a given frequency list
    increment [] e = [([e], 1)]
    increment (x:xs) e
      | e == ((head . fst) x) = ((fst x), (snd x) + 1) : xs
      | otherwise = x : increment xs e

-- rolled my own QuickSort to sort entries
entrySort :: [Entry] -> [Entry]
entrySort [] = []
entrySort (pivot:xs) = (entrySort lessThan) ++ [pivot] ++ (entrySort greaterThan)
  where lessThan    = [e | e <- xs, (snd e) < (snd pivot)]
        greaterThan = [e | e <- xs, (snd e) >= (snd pivot)]

-- converts a list of entries to a list of binary trees
makeEntryLeaves :: [Entry] -> [BinaryTree Entry]
makeEntryLeaves []     = []
makeEntryLeaves (x:xs) = (Node x EmptyTree EmptyTree) : makeEntryLeaves xs

-- combines the first two elements and returns a new tree list
-- not safe, BinaryTree's have to be Node's
combine :: [BinaryTree Entry] -> [BinaryTree Entry]
combine [] = []
combine (only:[]) = [only]
combine ((Node e1 l1 r1):(Node e2 l2 r2):rest) = mergeInto newNode rest
  where newNode = (Node combined (Node e1 l1 r1) (Node e2 l2 r2))
        combined = ((fst e1) ++ (fst e2), (snd e1) + (snd e2))

        mergeInto e [] = [e]
        mergeInto (Node e1 l1 r1) ((Node e2 l2 r2):xs)
          | (snd e1) < (snd e2) = (Node e1 l1 r1) : (Node e2 l2 r2) : xs
          | otherwise           = (Node e2 l2 r2) : mergeInto (Node e1 l1 r1) xs

-- calls combine until the length is one
formTree :: [BinaryTree Entry] -> [BinaryTree Entry]
formTree (e:[]) = [e]
formTree ls = formTree (combine ls)

makeDictionary :: BinaryTree Entry -> [(Char, [Char])]
makeDictionary tree = makeDictionary' tree []
  where makeDictionary' EmptyTree c = []
        makeDictionary' (Node val EmptyTree EmptyTree) c = [((head . fst) val, c)]
        makeDictionary' (Node _ left right) c = (makeDictionary' left (c ++ "0")) ++ (makeDictionary' right (c ++ "1"))


