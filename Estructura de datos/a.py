#Dada una lista de palabras, crea un diccionario donde las claves sean las palabras y los valores sean las palabras al revés.


palabras = ["maria", "genesis", "dayana", "angeles", "aeio"]

duxc = {x : x[::-1] for x in palabras}

#print(duxc)

#Dada una lista de palabras, crea un diccionario donde las claves sean las palabras que 
# comienzan con una vocal y los valores sean True, y las demás palabras sean False.

vocales = 'aeiou'
        
res = { x : True if x[0].lower() in vocales else False for x in palabras }

#print(res)


#Dada una lista de palabras, crea un diccionario donde las claves sean 
#las palabras cuya longitud es impar y los valores sean la longitud de esas palabras.





xx = {x:len(x) for x in palabras if len(x)%2!=0 }

print(xx)
