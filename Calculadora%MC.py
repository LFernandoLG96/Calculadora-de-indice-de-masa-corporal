#Con las siguientes lineas imprimimos un texto dando la bienvenida al usuario
texto_1 = ('''Saludos, usuario. Bienvenido a la calculadora del indice de masa corporal(CIMC). 
  Si deseas saber tu indice de masa corporal por favor proporcionanos los siguientes datos:  ''')
print(texto_1)

#Con las siguientes lineas solicitamos los datos del usuario y los almacenamos en variables
nombre = input("¿Cuál es tu/s nombre/s? ")
apellidoP = input('¿Cuál es el tu apellido paterno? ')
apellidoM = input('¿Cuál es tu apellido materno? ')
#Podemos concatenar el/los nombres y los apellidos obtenidos hasta ahora para imprimir después el nombre completo. 
nombre_C = nombre + ' ' + apellidoP + ' '+ apellidoM
nombre_f = nombre_C.title()

#Edad y verificación: Con el comando float cambiamos el tipo de la variable de cadena a decimales y con int a enteros. 
while True:
 try:
    edad = int(input('¿Cuál es tú edad? '))
    if edad > 0:
     break
    print("La edad debe de ser un numero entero positivo")
 except ValueError:
    print(f'Por favor introduzca su edad con digitosa. Ejemplo: 11, 15 o 30')

#Peso en kilogramos y verificació
while True:
 try:
    peso = float(input('¿Cuántos kilogramos pesas? '))
    if peso >= 0 :
      break
    print('El peso debe de ser un numero entero positivo. Puede contener decimales')
 except ValueError:
    print(f'introduce tu peso en en digitos')   
    
#Estatura y verificación
while True:
  try:
    estatura =float(input('¿Cuál es tu estatura?'))
    if peso > 0:
      break
    print('Tu edad no puede ser un número negativo')
  except ValueError:
    print('Por favor introduce tu estatura en digitos' )

#Con la siguiente formula calculamos el indice de masa corporal
imc = str(peso / (estatura ** 2))

#Con las siguientes lineas imprimmos el indice de masa corporal del usuario 
print(f'Querido ' + nombre_f  + '. tu indice de masa corporal es de = ' +  imc  + '%')  

