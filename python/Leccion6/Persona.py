class Persona: #Creamos una clase
    def __int__(self, nombre, apellido, edad): # Se lo llama método Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        def mostrar_detalle(self):
            print(f"Persona:{self.nombre}{self.apellido}{self.edad}")
persona1 = Persona("Belen", "Rabel", 41) # Necesitamos enviar argumentos
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)

persona2 = Persona("Matias", "Perez", 22)
print(f"El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}")

persona1.nombre = "Gianella"
persona1.apellido = "Zárate"
persona1.edad = 14
print(f"El objeto1 modificado de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}")

#Los atributos: son características
#Los métodos son:el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle()
persona2.mostrar_detalle()
