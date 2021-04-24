module Main where

getList :: Read a => IO [a]
getList = do 
    line <- getLine
    return line 

main :: IO ()
main = do 

