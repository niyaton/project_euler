fibonacci = 1:2:zipWith (+) fibonacci (tail fibonacci)

fibos = [x | x <- takeWhile (<4000000) fibonacci, even x]

main = print $ sum fibos
