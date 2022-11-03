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

    



