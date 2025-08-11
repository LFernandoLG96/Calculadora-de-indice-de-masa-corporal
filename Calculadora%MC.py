#Con las siguientes lineas imprimimos un texto dando la bienvenida al usuario
texto_1 = ('''Saludos, usuario. Bienvenido a la calculadora del indice de masa corporal(CIMC). 
  Si deseas saber tu indice de masa corporal por favor proporcionanos los siguientes datos:  ''')
print(texto_1)

#Con las siguientes lineas solicitamos los datos del usuario y los almacenamos en variables. Ademas con los comandos if y else 
#nos aseguramos de que el usuario no deje el campo en blanco 
while True:

  nombre = input("¿Cuál es tu/s nombre/s? ")
  if nombre != '':
    break
  else:
    print('Este campo no puede quedar vacio')

while True: 

  apellidoP = input('¿Cuál es el tu apellido paterno? ')
  if apellidoP != '':
    break
  else:
    print('Este campo no puede quedar vacio')

while True:
  apellidoM = input('¿Cuál es tu apellido materno? ')
  if apellidoM != '':
    break
  else:
    print('Este campo no puede quedar vacio')

#Podemos concatenar el/los nombres y los apellidos obtenidos hasta ahora para imprimir después el nombre completo. 
nombre_C = nombre + ' ' + apellidoP + ' '+ apellidoM
#Utilizamos el comando title para poner todas las primeras letras de el/los nombre/s y apellidos en mayusculas
nombre_f = nombre_C.title()

#Edad y verificación: Con el comando float cambiamos el tipo de la variable de cadena a decimales y con int a enteros. 
while True:
 try:
    edad = int(input('¿Cuántos años tienes? '))
    if edad > 0:
     break
    print("La edad debe de ser un numero entero positivo")
 except ValueError:
    print(f'Por favor introduzca su edad con números. Este campo no puede quedar vacio')

#Peso en kilogramos y verificació
while True:
 try:
    peso = float(input('¿Cuántos kilogramos pesas? '))
    if peso >= 0 :
      break
    print('El peso debe de ser un numero entero positivo. Puede contener decimales')
 except ValueError:
    print(f'introduce tu peso en en digitos, este campo no puede quedar vacio')   
    
#Estatura y verificación de parametros 
while True:
  try:
    estatura =float(input('¿Cuál es tu estatura en metros?'))
    if peso > 0  and peso != '' and estatura <= 3:
        break
        
    else:
      if estatura <= 0 or estatura > 3:  
       print('Introduce una edad valida. Esta no puede ser un numero negativo o quedar en cero.Recuerda introducir tu edad en metros')
  except ValueError:
      print('Por favor introduce tu estatura en digitos y en metros' )

#Con la siguiente formula calculamos el indice de masa corporal
imc = float(peso / (estatura ** 2))

#Con las siguientes lineas imprimmos el indice de masa corporal del usuario 
print(f'Querido  {nombre_f} tu indice de masa corporal es de {imc:.2f} %')  


#Con las sigueintes lineas imprimimos todos los datos restantes del usuario y adicionalmente la categoría
categoria = ''
if imc < 18.49: 
  categoria = 'bajo de peso'
elif 18.5 <= imc <= 24.99:
  categoria = 'en un peso normal' 
elif 25.0 <= imc <= 29.99:
  categoria = 'en pre-obesidad o Sobrepeso'
elif 30.0 <= imc <= 34.99:
  categoria = 'en obesidad clase I'
elif 35.00 <= imc <= 39.99:
  categoria = 'en obesidad clase II'
else:
  categoria = "en obesidad morbida"

print(f'''Considerando los datos de la Organización mundial de la Salud,  
dada tu estatura de {estatura} m, tu peso {peso} kg y tus {edad} años de edad.
 Te encuentras {categoria}''')