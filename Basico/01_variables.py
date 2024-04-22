# Variables
my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

# Concatenacion de variables en print
print(type(print(my_string_variable, my_int_to_str_variable, my_bool_variable)))

# Algunas funciones del sistema
print('Mi variable string "''my_string_variable''" tiene',len(my_string_variable), 'caracteres')

first_name = input('Cual es tu nombre?: ')
age = input('Cual es tu edad?: ')

print(first_name, ", tienes ", age, " años" )

