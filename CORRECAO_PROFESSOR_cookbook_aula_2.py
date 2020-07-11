#!/usr/bin/python3

#matriz = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
matriz = [ [6, 2, 8], [4, 5, 6], [3, 8, 9] ]

a, b = 0, 0

for x, y in enumerate(matriz):
    a += y[x]
    b += y[-(x+1)]

print(a + b)
