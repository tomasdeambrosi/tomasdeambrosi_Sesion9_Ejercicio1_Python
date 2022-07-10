'''Crea un script que le pida al usuario una lista de países (separados por comas). 
Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). 
Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.'''

lista = input("Introduce una lista de países separados por comas: ")

paises = [pais for pais in lista.split(",")]

print(",".join(sorted(list(set(paises)))))