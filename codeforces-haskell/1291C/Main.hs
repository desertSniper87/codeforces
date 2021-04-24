module Main where

import Control.Monad (replicateM_)
solve :: (Ord a2, Ord a1, Num a1) => a1 -> a1 -> [a2] -> a2
solve myPos options x
    | myPos == 1 = maximum [head x, last x]
    | myPos > 1 && options > 0 = solve (myPos - 1) (options - 1) (choosingBegger x)
    | myPos > 1 = solve (myPos - 1) options (freeForAll x)


freeForAll :: Ord a => [a] -> [a]
freeForAll x
    | head x < last x = tailRemoved
    | otherwise = tail x
    where tailRemoved = take (length x - 1) x

choosingBegger :: Ord a => [a] -> [a]
choosingBegger x
    | head x > last x = tailRemoved
    | otherwise = tail x
    where tailRemoved = take (length x - 1) x


main :: IO ()
main = do
    tests <- readLn
    replicateM_ tests $ do
        [_, m, k] <- map read . words <$> getLine
        items <- map read . words <$> getLine :: IO [Int]
        print $ solve m k items