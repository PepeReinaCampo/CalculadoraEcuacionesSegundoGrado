import math 
import cmath
from math import sqrt
import time
print('HOLA, SOY UNA CALCULADORA DE ECUACIONES DE SEGUNDO GRADO, TE PEDIRÉ QUE INTRODUZCAS NUMEROS')
time.sleep(1)
print('Como ya sabes la ecuacion de segundo grado es tal que así "ax² + bx + c = 0"')
time.sleep(2)
print('Para resolver la ecuacion igualaremos X a 0')
time.sleep(1)
print('Bueno, empezamos... ve metiendo los terminos A, B y C conforme se te pidan, mete solo numeros, utiliza la tecla "," correcta en caso de usar numeros con decimales. ')

while True:
    try:
        a= float(input('¡VENGA! introduce el valor del coeficiente a, tiene que ser distinto de 0 : '))
        
        if a==0:
             print("'a' no puede ser 0, mira que te lo he dicho.")
        else:
            print('Gracias')
            break
    except ValueError:
        print("Mete un número correcto melón")
while True:
    try:
        b= float(input('VAS BIEN, ahora introduce el valor del coeficiente b : '))
        print('Gracias, otra vez')
        break
    except ValueError:
        print('MAAAALLLL ¿TAN DIFICIL ES?')
while True:
    try:
        c= float(input('¡CASI HAS TERMINADO!, introduce el valor del coeficiente C : '))
        print('Gracias, ya has terminado tu parte, ahora te toca esperar')
        break
    except ValueError:
        print('Numero....NUMEROOOOOO, ¡AY DIOS!')

discriminante =  b * b - 4 * a * c

if discriminante < 0:
    print('La ecuación no tiene solución real.') 
    time.sleep(1)
    print('La ecuación no tiene solución real ¿ahora si lo has leido?')
    time.sleep(3) 
    print('A ver, cuchame, python se raia cuando no le salen bien las cosas asi que intenta no preguntar por cosas sin solucion real')
    time.sleep(2)
    print ('vale')
    sol1 = (-b + cmath.sqrt(discriminante)) / (2 * a)
    sol2 = (-b - cmath.sqrt(discriminante)) / (2 * a)
    print("Las soluciones imaginarias son:", sol1, "y", sol2)
    time.sleep(0.5)
    print('¿Te has quedado contenta?')
    exit()
   
else:
    print('Dame un segundito que piense') 
    time.sleep(1.5)
    raiz = sqrt(discriminante)
    s1 = (-b + raiz) / (2 * a)
    s2 = (-b - raiz) / (2 * a)
    if s1==s2:
        print('Solo hay una solucion y es: x =', s1)
    else:
        print('Las soluciones son: ')
        print('x =',s1)
        print('x =',s2)
