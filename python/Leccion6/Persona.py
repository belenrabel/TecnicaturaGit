class Persona:  # Creamos una clase
    def __init__(self, nombre, apellido, edad, *args, **kwargs):  # Se lo llama método Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self) -> object:  # self es igual a this
        print(
            f"La clase persona tiene los siguientes datos:{self.nombre}{self.apellido}{self.edad}, la direccion es {self.args}, los datos importantes son {self.kwargs}")


persona1 = Persona('Gonzalo', 'Rabel', 41)  # Necesitamos enviar arguments
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)

persona2 = Persona('Matias', 'Perez', 22)
print(f"El objet2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}")

persona1.nombre = "Gianella"
persona1.apellido = "Zárate"
persona1.edad = 14
print(f"El objeto1 modification de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}")

# Los atributos: son características
# Los métodos son:el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle()  # La referencia en este caso se pasa de manera automática
persona2.mostrar_detalle()

# Persona.mostrar_detalle(persona1) # Debemos pasarle una referencia para el sef o dará error
persona1.telefono = '456465321321'
print(f'Este es el telefono de: {persona1.nombre} {persona1.telefono}')  # Hemos creado un atributo de un objeto

# print(persona2.telefono) el ojeto persona2 no tiene atributo de error
persona3 = Persona('Rogelio', 'Romero', 27, 'Telefono', '26056564', 'Calle Lopez', 801, 'Manzana', 77, 'Casa', 18, Altura=1.83, Peso=90, CFavorito='Azul', Auto='Citroen', Modelo=2021,)
persona3.mostrar_detalle()