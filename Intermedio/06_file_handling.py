## File Handling ##
import os

txt_file = open("Intermedio/my_file.txt", "w+")

txt_file.write("Mi nombre es Nicolas \nMi apellido es Laderach \nTengo 37 años \nMi lenguaje es Python")

#print(txt_file.read())
#print(txt_file.read(10)) // Lee los primeros 10 caracteres
#print(txt_file.readline()) //
#print(txt_file.readline()) // Lee primer y segunda linea
for line in txt_file.readlines():
       print(line)  

txt_file.write("\nAgrego esta linea")
print(txt_file.readline())

txt_file.close()

##os.remove("Intermedio/my_file.txt")

################################################################################################

import json

json_file = open("Intermedio/my_file_json.json", "w+")

json_test = {
    "name":"Nicolas"
    , "surname":"Laderach"
    , "age":37
    , "languages":["Python", "Swift", "Kotlin"]       
}

json.dump(json_test, json_file, indent=4)
json.dump(json_test, json_file, indent=4)