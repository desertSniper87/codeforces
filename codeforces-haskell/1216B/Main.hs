module Main where

import Data.List (sort, sortBy)
import Data.Ord (comparing)


gallery :: (Ord a, Num b, Enum b) => [a] -> [(a, b)]
gallery cans = sortBy (flip (comparing fst)) (zip cans [1 .. ])

totalShots :: [Int] -> Int
totalShots cans = length cans + sum (map (\x -> fst x * snd x) canShot)
    where canShot = zip [fst g | g <- gallery cans ][0..]

shotPosition :: (Ord a1, Num a2, Enum a2) => [a1] -> [a2]
shotPosition cans = pos
    where pos = [snd g | g <- gallery cans]


main :: IO ()
main = do
    _ <- words <$> getLine
    cans <- map read . words <$> getLine
    print $ totalShots cans
    putStrLn $ unwords $ map show (shotPosition cans)
