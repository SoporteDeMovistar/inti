import re

archivo = open("log.txt","r") 
lineas = archivo.readlines()
Comentarios = []

for texto in lineas:
    if texto.find("commit") and texto.find("Author") and texto.find("Date"):
            if re.search('[a-zA-Z]', texto):
                Comentarios.append(texto)

print(Comentarios)