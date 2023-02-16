def newTem(tem):
    print("\n           ",tem,"            \n")


newTem("Operadores aritmeticos")
print("Operacior dicvicion entera 10//3:",10//3)
print("Operacior potencia 5**3:",5**3)

#Actividad:Imprimir la terminal de operadores

newTem("Operadores logicos")

newTem("AND")
print("Operador and(True and False)",True and False)
print("Operador and(True and True)",True and True)
print("Operador and(False and True)",False and True)
print("Operador and(False and False)",False and False)

newTem("OR")
print("Operador and(True or False)",True or False)
print("Operador and(True or True)",True or True)
print("Operador and(False or True)",False or True)
print("Operador and(False or False)",False or False)

newTem("Not")
print("Operador and(not False)",not False)
print("Operador and(not True)",not True)

newTem("a")
#Actividad:Agregar los demas operadores de operacion

newTem("Operadores Comparativos")
print("2==5",2==5)
print("6!=10",6!=10)
print("10<5",10<5)
print("8<=8",8<=8)
print("3>1",3>1)
print("7>=10",7>=10)

newTem("Variables")
variable1=10
variable2=6.2456
variable3="Juancho"
dosPalabra="Hola"
dos_palabra="Hi"

print(variable1,variable2,variable3,dosPalabra,dos_palabra)

a,b,c=6,25.25,"Palabra"

print(a,b,c)

newTem("Entero")
w=666
x=89756745121231
y=-58
z=0b010110
h=0x2f

print(w,type(w))
print(x,type(x))
print(y,type(y))
print(z,type(z))
print(h,type(h))

newTem("Flotantes")#Precicion de 15 desimales 

x=164.54
print(x,type(x))
y=0.1545479
print(y,type(y))

newTem("Numeros complejos")

x=-25j
y=45+10j
z=3j

print(x,type(x))
print(y,type(y))
print(z,type(z))

newTem("Booleanos")

lis=[6]
print(lis,"es",bool(lis))
t=()
print(t,"es",bool(t))
new= "Hi :v"
print(new,"es",bool(new))
num=66
print(num,"es",bool(num))
com=1+0j
print(com,"es",bool(com))
val=None
print(val,"es",bool(val))

newTem("Listas")
a=[10,6.5,"Lista"]
print(a)
print(a[2])
a[1]="H"
print(a)

newTem("Tuplas")
t=(6,"HU",16-4j,18.5)
print(t)
print(t[1])
print("t[0:2]:",t[0:2])

newTem("Sets")
a={50,20,30,40,10,50}
print("a=",a)
print(type(a));

newTem("Diccionario")
d={1:'gg','hu':2j}
print(d,type(d))
print("d[1]=",d[1])
print("d[2]=",d["hu"])

newTem("Cadenas")
sd="Esto es una simple cadena"
ss='cadena simple simple'
print(sd,type(sd));
print(ss,type(ss))
s2='''Esto es 
una multiple cadena
con             tab'''
print(s2,type(s2))
#segmentado
print(s2)
print("Segmento de cadenas")
print(sd[2:6])
print(sd[:5])
print(sd[6:])
print(sd[-6:-3])
#sancada
print(sd[0:10:1])
print(sd[0:10:2])
print(sd[0:10:3])

cadena1="Hola"
cadena2=(cadena1+" ")*5
print(cadena2)
cadena3=cadena2.upper()
print(cadena3)
#t[1]=12 opcion no valida en tupla