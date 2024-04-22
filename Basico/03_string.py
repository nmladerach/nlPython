texto1 = "Mi cadena de texto"
texto2 = " y mi otra cadena de texto"
texto3 = "Esta es una cadena de texto con \nsalto de linea"
texto4 = " \tEsta es una cadena de texto con tabulación"
texto5 = " \\tEsta es una cadena de texto \\n escapado"


print(len(texto1))
print(texto1 + " " + texto2)
print(texto3)

print(texto4)
print(texto5)

######

name, surname, age = "Juan", "Perez", 35

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

#Desempaquetado de caracteres

lenguaje = "Python"
a, b, c, d, e, f = lenguaje
print(a)
print(b)