class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.prestado = False  # Está libre para prestar
    
    def prestar(self):
        if not self.prestado:
            self.prestado = True
            print(f"Gracias por prestar {self.titulo} :)")
        else:
            print(f"{self.titulo} no se puede prestar, ya alguien lo tiene :(")  # en lugar de "ya ha sido prestado :("
    
    def devolver(self):
        if self.prestado:
            self.prestado = False
            print(f"Gracias por devolver {self.titulo} :)")
        else:
            print(f"{self.titulo} no estaba prestado, imposible devolver")  # en lugar del mensaje original
    
    def mostrarInfo(self):
        estado = "EN USO" if self.prestado else "LIBRE"  # en lugar de "PRESTADO"/"DISPONIBLE"
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año: {self.año}")
        print(f"Estado: {estado}")
        print("-" * 25)

# Creación de los tres libros
libro1 = Libro("Orgullo y Prejuicio", "Jane Austen", 1811)  # cambio para conflicto
libro2 = Libro("Harry Potter", "J.K. Rowling", 1999)
libro3 = Libro("Hunger Games", "Suzanne Collins", 2010)

print("\nInformación inicial de los libros:")
libro1.mostrarInfo()
libro2.mostrarInfo()
libro3.mostrarInfo()

print("\nPrestar y devolver los libros:")

print("***Prestando 'Orgullo y Prejuicio'***")
libro1.prestar()

print("\n***Prestando 'Harry Potter'***")
libro2.prestar()

print("\n***Prestando 'Orgullo y Prejuicio'***") # Ya está prestado
libro1.prestar()

print("\n***Devolviendo 'Orgullo y Prejuicio'***")
libro1.devolver()

print("\n***Devolviendo 'Hunger Games'***") # Nunca se prestó
libro3.devolver()