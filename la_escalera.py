import math
import os
import random
import re
import sys
''''''''''
def staircase(n):
    print("Ingrese el tamaño de la escalera: ")
    valor = int(input())

    for i in range(1, n+1):
        print("/n".join(" "*(n-i) + "#"*i))
        print("")

print("/n".join(" "*((n-i)/2) + "#"*i))

        return "\n".join([" "*(n-i) + "#"*(i) for i in range(1, n+1)])

'''''''''

def staircase(n):
    if n % 2 == 0:
        for i in range(1, n+1):
            "\n".join([" "*(n-i) + "#"*(i) for i in range(1, n+1)])
            print("")
    else:
        for i in range(1, n+1):
            print("/n".join(" "*round((n-i)/2) + "#"*i))
            print("")

altura = int(input("Ingrese la altura de la escalera:"))

print(staircase(altura))
