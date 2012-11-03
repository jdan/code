-- Binary Tree Module
-- Jordan Scales
-- 2 November 2012

module BinaryTree(insert, height, arrayToBST) where

-- we'll treat it as a `binary search tree`
data BinaryTree a = Node a (BinaryTree a) (BinaryTree a) |
                    EmptyTree
                    deriving (Show)

-- insert into a BST
insert :: (Ord a) => BinaryTree a -> a -> BinaryTree a
insert EmptyTree n = Node n EmptyTree EmptyTree
insert (Node val left right) n
  | n < val   = Node val (insert left n) right
  | otherwise = Node val left (insert right n)

-- height of a BST
height :: BinaryTree a -> Integer
height EmptyTree = 0
height (Node _ left right) = 1 + max (height left) (height right)

-- convert an array to a BST
arrayToBST :: (Ord a) => [a] -> BinaryTree a
arrayToBST (x:xs) = arrayToBST' (x:xs) EmptyTree
  where
    arrayToBST' [] t     = t
    arrayToBST' (x:xs) t = arrayToBST' xs (insert t x)

-- search the tree (this doesn't do much...)
find :: (Ord a) => BinaryTree a -> a -> a
find EmptyTree e = undefined
find (Node val left right) e
  | e == val  = e
  | e < val   = find left e
  | otherwise = find right e

-- check if a node is a leaf
isLeaf :: BinaryTree a -> Bool
isLeaf EmptyTree                    = False
isLeaf (Node _ EmptyTree EmptyTree) = True
isLeaf (Node _ _ _)                 = False

-- find the max element of a tree
findMax :: (Ord a) => BinaryTree a -> a
findMax EmptyTree              = undefined
findMax (Node val _ EmptyTree) = val
findMax (Node _ _ right)       = findMax right

-- removes the max element and produces a new teee
removeMax :: (Ord a) => BinaryTree a -> BinaryTree a
removeMax EmptyTree                    = EmptyTree
removeMax (Node _ EmptyTree EmptyTree) = EmptyTree
removeMax (Node _ left EmptyTree)      = Node (findMax left) (removeMax left) EmptyTree
removeMax (Node val left right)        = Node val left (removeMax right)

