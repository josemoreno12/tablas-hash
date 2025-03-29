class DirectorioTelefonico:
    def __init__(self):
        self.directorio = {}

    def agregar_contacto(self, nombre, telefono):
        self.directorio[nombre] = telefono
        print(f"Contacto {nombre} agregado correctamente.")

    def buscar_contacto(self, nombre):
        return self.directorio.get(nombre, "Contacto no encontrado")

    def eliminar_contacto(self, nombre):
        if nombre in self.directorio:
            del self.directorio[nombre]
            print(f"Contacto {nombre} eliminado correctamente.")
        else:
            print("Contacto no encontrado.")

    def mostrar_directorio(self):
        if self.directorio:
            contactos = "\n".join(f"{nombre}: {telefono}" for nombre, telefono in self.directorio.items())
            print(contactos)
            return contactos
        else:
            print("El directorio está vacío.")
            return "El directorio está vacío."

directorio = DirectorioTelefonico()
directorio.agregar_contacto("Sofia", "312-578-4590")
directorio.agregar_contacto("Melani", "987-123-4567")
directorio.agregar_contacto("Juan Perez", "123-456-7890")
directorio.agregar_contacto("Maria Lopez", "987-654-3210")
print(directorio.buscar_contacto("Juan Perez"))
contactos = directorio.mostrar_directorio()
directorio.eliminar_contacto("Maria Lopez")
contactos = directorio.mostrar_directorio()
