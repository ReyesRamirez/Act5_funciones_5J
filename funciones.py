print("Ejemplo de funciones")
# declarando funciones
def hola():
    print("Alguien uso la funcion hola")
    
def chat(mensa):
    print(f"chat {mensa}")
    
def ellacontesta(mensa):
    print(f"chat ella: {mensa}")
    
def escribenombre(ap,n):
    print(f"Tu nombre completo es: {n} {ap}")

def suma(a,b):
    s=a+b
    return s

def resta(c,d):
    s=c-d
    return s

def multiplicacion(e,f):
    s=e*f
    return s

def division(g,h):
    s=g/h
    return s

# llamadas a funciones
hola()
chat("que bonita estas")
ellacontesta("gracias")
escribenombre("Ramirez","Reyes")

print("Operacion suma")
c1=int(input("Ingresa un numero"))
c2=int(input("Ingresa un numero"))
damesuma=suma(c1,c2)
print(f"La suma de {c1} + {c2} = {damesuma}")

print("Operacion resta")
c1=int(input("Ingresa un numero"))
c2=int(input("Ingresa un numero"))
dameresta=resta(c1,c2)
print(f"La resta de {c1} - {c2} = {dameresta}")

print("Operacion multiplicacion")
c1=int(input("Ingresa un numero"))
c2=int(input("Ingresa un numero"))
damemultiplicacion=multiplicacion(c1,c2)
print(f"La division de {c1} * {c2} = {damemultiplicacion}")

print("Operacion multiplicacion")
c1=int(input("Ingresa un numero"))
c2=int(input("Ingresa un numero"))
damedivision=division(c1,c2)
print(f"La multiplicacion de {c1} / {c2} = {damedivision}")