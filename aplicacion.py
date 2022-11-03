
def agregar_contenido_archivo(nombre, contenido):
    archivo = open(nombre,"at")
    archivo.write("\n" + contenido)
    archivo.close()



def leer_archivo(nombre):
    archivo = open(nombre, "rt", encoding='utf8')
    contenido = archivo.read()
    return contenido 

user_ = open("login.txt")
pwd_ = open("clave.txt")

usuario = user_.read()
clave = pwd_.read()

print("Bienvenido, ingrese sus datos")
print("Usuario: ")
user =input()
print("Contrasena: ")
pwd = input()

if user == usuario and pwd==clave:
    print("Bienvenido al programa")
else:
    print("Usuario: ")
    user =input()
    print("Contrasena: ")
    pwd = input()
if user == usuario and pwd==clave:
    print("Bienvenido al programa")
else:
    print("usuario o contraseña invalido!")

if user==usuario and pwd==clave:
    print("Datos Persona")
    print("1. Listar Personas")
    print("2. Agregar Personas")
    print("3. Salir")

lista = open("nombre.txt")
print("Seleccione una opcion")
opcion=input()

if opcion==1:
    leer_archivo(lista)
    

if opcion==2:
    print("Nombre de la persona a agregar:")
    nombren=input()
    agregar_contenido_archivo(lista,nombren)

if opcion==3:
    print("b")

