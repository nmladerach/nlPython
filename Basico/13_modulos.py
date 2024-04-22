### Modulos ###
### Son librerias ###

# import 10_function -> no tiene correcta nomenclatura , no puede empezar con numero

import function

num1 = 5
num2 = 4

function.sum_two_values(num1, num2)

##result =  sum_two_values(num1, num2)
##print(result)

from function import sum_two_values

result2 = sum_two_values(num1, num2)
print(result2)