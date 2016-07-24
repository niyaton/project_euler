is3or5 x | mod x 3 == 0 = True
         | mod x 5 == 0 = True
         | otherwise = False

main = print $ sum [x | x <- [3..1000], is3or5 x]
