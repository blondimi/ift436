max (x1:x') = max' x' x1 where
  max' [] m = m
  max' (xi:x') m | xi > m    = max' x' xi
                 | otherwise = max' x' m
