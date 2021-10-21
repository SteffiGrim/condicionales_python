# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

texto_1 = '5'
texto_2 = '7'

# 1-Verifique cual de los dos textos es mayor alfabéticamente
# La comparación alfabética es aquella que se logra cuando
# se utiliza el operador mayor o menor con Strings (textos)
# Imprima en pantalla según corresponda

if(texto_1 < texto_2):
    print("el texto_2 es mayor")
else:
    print("el texto_1 es mayor")

# 2-Transforma esas variables tipo texto en variables numéricas con (int)
# y almacénalas en nuevas variables.
# Compare las nuevas variables para ver cual es mayor o menor
# utilizando los operadores correspondientes
# ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda

texto_1 = int(texto_1)
texto_2 = int(texto_2)
if(texto_1 < texto_2):
    print("el texto_2 es mayor")
else:
    print("el texto_1 es mayor")

# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
# Esta pregunta estará repetida en el Campus para que puedan
# responder.

#RESPUESTA: no busqué en google, recuerdo que la primera clase hablaron acerca del programa y que por cada letra habia una posición establecida con números. 
#es decir que independientemente de los caracteres de texto que haya, cada letra, cada numero, cada simbolo del teclado 
#tiene un valor asignado y se contará (para mayor o menor) en base a lo ya establecido en la realización de ese programa.
#Siete y Cinco tienen la misma cantidad de letras en string. 
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)
