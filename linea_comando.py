# Taller-json
import json
import os

# Archivo donde se guardan los contactos
ARCHIVO = 'contacts.json'

# Menú visual con arte ASCII
menu_texto = """

/====================================================================================/
|| __   __  _______  __    _  __   __                                               ||
|||  |_|  ||       ||  |  | ||  | |  |                                              ||
|||       ||    ___||   |_| ||  | |  |                                              ||
|||       ||   |___ |       ||  |_|  |                                              ||
|||       ||    ___||  _    ||       |                                              ||
||| ||_|| ||   |___ | | |   ||       |                                              ||
|||_|   |_||_______||_|  |__||_______|                                              ||
|| _______  _______  __    _  _______  _______  _______  _______  _______  _______  ||
|||       ||       ||  |  | ||       ||   _   ||       ||       ||       ||       | ||
|||       ||   _   ||   |_| ||_     _||  |_|  ||       ||_     _||   _   ||  _____| ||
|||       ||  | |  ||       |  |   |  |       ||       |  |   |  |  | |  || |_____  ||
|||      _||  |_|  ||  _    |  |   |  |       ||      _|  |   |  |  |_|  ||_____  | ||
|||     |_ |       || | |   |  |   |  |   _   ||     |_   |   |  |       | _____| | ||
|||_______||_______||_|  |__|  |___|  |__| |__||_______|  |___|  |_______||_______| ||
/====================================================================================/

                        1) Mostrar Contactos 
                        2) Crear Contacto 
                        3) Actualizar Contacto
                        4) Eliminar Contacto
                        5) Salir 
"""

# Limpiar consola según sistema operativo
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

# Cargar contactos desde archivo JSON
def cargar_contactos():
    if not os.path.exists(ARCHIVO):
        return []
    try:
        with open(ARCHIVO, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("⚠️ No se puede leer el archivo JSON.")
        return []

# Guardar contactos en archivo JSON
def guardar_contactos(contactos):
    with open(ARCHIVO, 'w', encoding='utf-8') as file:
        json.dump(contactos, file, indent=2)

# Mostrar todos los contactos
def mostrar_contactos():
    contactos = cargar_contactos()
    if not contactos:
        print("📭 No hay contactos registrados.")
    else:
        for contacto in contactos:
            print(f"ID: {contacto['ID']} | Nombre: {contacto['Nombre']} | Teléfono: {contacto['Telefono']} | Email: {contacto['Email']}")

# Crear un nuevo contacto
def crear_contacto():
    contactos = cargar_contactos()
    nuevo_id = max([c['ID'] for c in contactos], default=0) + 1
    nombre = input("📝 Ingrese nombre: ").strip()
    telefono = input("📞 Ingrese telefono: ").strip()
    email = input("📧 Ingrese email: ").strip()

    if not nombre or not telefono or not email:
        print("Todos los campos son obligatorios.")
        return

    nuevo_contacto = {
        "ID": nuevo_id,
        "Nombre": nombre,
        "Telefono": telefono,
        "Email": email
    }

    contactos.append(nuevo_contacto)
    guardar_contactos(contactos)
    print("✅ Contacto agregado.")

# Actualizar un contacto existente
def actualizar_contacto():
    contactos = cargar_contactos()
    try:
        id_actualizar = int(input("🔁 Ingrese ID del contacto a actualizar: "))
        for contacto in contactos:
            if contacto['ID'] == id_actualizar:
                contacto['Nombre'] = input(f"Nuevo nombre ({contacto['Nombre']}): ") or contacto['Nombre']
                contacto['Telefono'] = input(f"Nuevo teléfono ({contacto['Telefono']}): ") or contacto['Telefono']
                contacto['Email'] = input(f"Nuevo email ({contacto['Email']}): ") or contacto['Email']
                guardar_contactos(contactos)
                print("✅ Contacto actualizado.")
                return
        print("ID no encontrado.")
    except ValueError:
        print(" Ingrese un ID valido.")

# Eliminar un contacto por ID
def eliminar_contacto():
    contactos = cargar_contactos()
    try:
        id_eliminar = int(input("🗑️ Ingrese ID del contacto a eliminar: "))
        nuevos = [c for c in contactos if c['ID'] != id_eliminar]
        if len(nuevos) == len(contactos):
            print("ID no encontrado.")
        else:
            guardar_contactos(nuevos)
            print("✅ Contacto eliminado.")
    except ValueError:
        print("Ingrese un ID valido.")

# Menú principal
def menu():
    while True:
        limpiar_consola()
        print(menu_texto)
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == '1':
            mostrar_contactos()
        elif opcion == '2':
            crear_contacto()
        elif opcion == '3':
            actualizar_contacto()
        elif opcion == '4':
            eliminar_contacto()
        elif opcion == '5':
            print("👋 Saliendo del programa...")
            break
        else:
            print("Opcion invalida.")
        
        input("\nPresione Enter para seguir...")

# Ejecutar si se corre este archivo
if __name__ == '__main__':
    menu()
