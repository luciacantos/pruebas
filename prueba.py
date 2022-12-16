def staircase(n):
    if n % 2 == 0:
    print('\n'.join([" "*((n-i)/2) + "#"*(i) for i in range(1, n+1)]))
    else:
    print('\n'.join([" "*round((n-i)/2) + "#"*(i) for i in range(1, n+1)]))


altura = int(input("Ingrese la altura de la escalera: "))

print(staircase(altura))
