"""Ejercicio 1.8. Implementar un algoritmo que resuelva el siguiente problema: a) Dado un número natural n,
imprimir su tabla de multiplicar desde 0 hasta n."""

def tabla_multiplicar():
        n = int(input("Ingrese el numero que quiera multiplicar: "))
        for i in range(n):
                print(n, "por", i, "es igual a:", n*i)
                
        
tabla_multiplicar()


