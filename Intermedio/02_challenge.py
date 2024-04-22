### Challenge ###


'''
    FIZZBUZZ
    * Escribe un programa que muestre por consola (con un print) los
    * números de 1 a 100 (ambos incluidos y con un salto de línea entre
    * cada impresión), sustituyendo los siguientes:
    * - Múltiplos de 3 por la palabra "fizz".
    * - Múltiplos de 5 por la palabra "buzz".
    * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".


variable = 1

while variable <=100:
    if variable % 3 == 0 and variable % 5 == 0:
        print("fizzbuzz")
    elif variable % 3 == 0:
        print("fizz")
    elif variable % 5 == 0:
        print("buzz")
    else: 
        print(variable)
    variable += 1



## Resolucion Moure

def fizzbus():
    for index in range(1,101):
        if variable % 3 == 0 and variable % 5 == 0:
            print("fizzbuzz")
        elif variable % 3 == 0:
            print("fizz")
        elif variable % 5 == 0:
            print("buzz")
        else: 
            print(index)

fizzbus()


##################################################################################################

ANAGRAMA
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
'''

'''
def is_anagram(word_one, word_two):

    count = 0
    if word_one == word_two or len(word_one) != len(word_two):
        return "No anagram"
    else:
        for index in range(1, len(word_one)):
            if word_one[index] in word_two:
                count +=1
    if len(word_one) == count:
        return "anagram"


result = is_anagram("animales", "milanesa")

print(result)


## Resolucion Moure

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())

print(is_anagram("Amor", "Roma"))


 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 '''




def fibonacci():

    prev = 0
    next = 1
    fib = 0

    for index in range(1, 49):
        fib = prev + next
        print(fib)
        prev = next
        next = fib
    

fibonacci()