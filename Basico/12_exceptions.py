num1 = 5
num2 = 3
num2 = "4"

try:
    print(num1 + num2)
#except:
#    print("Se produjo un error")
#except ValueError as error:
    #print(error)
except TypeError as error:
    print(error)
except Exception as exception:
    print(exception)
