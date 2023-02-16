    #Operadores
#!operadores logicos
#?representa verdadero o falso solamente
#NOT
#NOT True = false
#NOT True == false = true
#AND
#true AND true = true
#true AND false = false
#false AND false = false
a=11
print(a>10 and a<20)

#OR 
#TRUE OR TRUE = true
#true OR false = true
#false OR true = true
# false OR false = false


x = 1+1==3
y = 1+1==2
print(x)
print(y)

#!operadores aritmeticos
# igual que ==
# Distinto de !=
# mayor que >
# menor que <
# mayor o igual que >=
# menor o igual que <=


#! regla 
#?1. primero se resuelven los parentesis 
#?2. expresiones aritmeticas(exponentes y raices , multiplicaciones y divisiones, sumas y restas)
#?3. relacionales (izquierda a derecha)
#?4. logicos (izquierda a derecha)

#!operadores de asignacion
#!Operadores de asignacion

a = 0

a +=1#?SUMA
print(a)

a -=1#?RESTA
print(a)

c = 5
c *=3 #?MULTIPLICACION
print(c)

c /= 3#?DIVICION
print(c)

x = 5
x %=2#?MODULO
print(x)

y = 2
y **=7 #?POTENCIA
print(y)

#!EJEMPLO
"""
n = 0
while n<10:
    if(n%2) == 0:
        print(n,"es un numero par")
    else:
        print(n,"es un numero impar")
    n +=1
"""
#!EJEMPLO 2 : OPERADORES Y EXPRESIONES
#!ENUNCIADO : 1) REALIZA UN PROGRAMA QUE LEA DOS NUMEROS POR TECLADO Y DETERMINE LOS SIGUIENTES ASPECTOS(ES SUFICIENTE MOSTRAR TRUE O FALSE)
#* si los dos numeros son iguales
#* Si los dos niumeros son diferentes
#* Si el primero es mayor que el segundo
#* Si el segundo es mayor o igual que el primero
"""
n1 = float(input("introduce el primer numero: "))
n2 = float(input("introduce el segundo numero: "))

print("¿Son iguales?", n1 == n2 )
print("¿Son diferentes?", n1 != n2)
print("¿el n1 es mayor que n2?",n1 > n2 )
print("¿El segundo es mayor o igual que el primero?", n2 >= n1)
"""
#!ENUNCIADO : 2) UTILIZANDO OPERADORES LOGICOS, DETERMINA SI UNA CADENA DE TEXTO INTRODUCIDA POR EL USUARIO TIENE UNA LONGITUD MAYOR O IGUAL QUE 3 Y A SU VEZ ES MENOR QUE 10(MOSTRAR TRUE OR FALSE)
"""
cadena = input("ingresa una cadena de texto: ")
x = len(cadena)
print(x>=3 and x<10)
"""
#!ENUNCIADO : 3) REALIZA UN PROGRAMA QUE CUMPLA EL SIGUIENTE ALGORITMO UTILIZANDO SIEMPRE QUE SEA POSIBLE OPERADORES EN ASIGNACION:
#* Guarda en una variable numero_magico el valor 12345679 (sin el 8)
#* Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9(asegurate que sea un numero)
#*Multiplique el numero_usuario por 9 en si mismo
#*Multiplica el numero_magico por el numero_usuario en si mismo
#*Finalmente muestra el valor final del numero_magico por pantalla

numero_magico = 12345679
numero_usuario = int(input("introduce un numero del 1 al 9: "))
numero_usuario *= 9
numero_magico *= numero_usuario
print("El numero magico es",numero_magico)







