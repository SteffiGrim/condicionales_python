# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

tempe_1 = int(input('Ingrese la primer temperatura:\n'))
tempe_2 = int(input('Ingrese la primer temperatura:\n'))
tempe_3 = int(input('Ingrese la primer temperatura:\n'))

if(tempe_1 > tempe_2):
    if(tempe_1 > tempe_3):
        print("la mayor temperatura es ", tempe_1)
        if(tempe_2 > tempe_3):
            print("la menor temperatura es ", tempe_3)
        else:
            print("la menor temperatura es ", tempe_2)
    else:
        print("la mayor temperatura es ", tempe_3)
        print("la menor temperatura es ", tempe_2)
else:
    if(tempe_2 > tempe_3):
        print("la mayor temperatura es ", tempe_2)
        if(tempe_1 < tempe_3):
            print("la menor temperatura es ", tempe_1)
        else:
            print("la menor temperatura es ", tempe_3)
    else:
        print("la mayor temperatura es ", tempe_3)
        print("la menor temperatura es ", tempe_1)
promedio = (tempe_1 + tempe_2 + tempe_3) / 3
print("el promedio de las temperaturas es ", promedio)