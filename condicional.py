print ("Hola, ¿cuál es tu edad?")
edad = int(input())
if edad >= 18 and edad < 65:
    print ("Eres mayor de edad")
elif edad > 65:
    print ("Eres jubilado")
else:
    print ("Eres menor de edad")