class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __repr__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

# Uso de los métodos __repr__ y __str__
persona = Persona("Juan", 30)
print(repr(persona))  # Utiliza __repr__: Persona(nombre=Juan, edad=30)
print(str(persona))   # Utiliza __str__: Nombre: Juan, Edad: 30
print(persona)        # Utiliza __str__: Nombre: Juan, Edad: 30
