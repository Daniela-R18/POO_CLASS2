class Salsa:
    def __init__(self):
        # Método constructor / Declaración de atributos de clase
        self.motivacion=True
        self.energia=100
        self.edad=0

    def hacer_patineta(self):
        self.energia=self.energia-1
        if (self.energia<=0):
            print("Me cansé")
        else:
            print ("Estoy haciendo la patineta")
    def hacer_dinos(self):
        self.energia=self.energia-1
        if (self.energia<=0):
            print("Me cansé")
        else:
            print ("Estoy haciendo dinos")   
    def hacer_basico(self):
        self.energia=self.energia-1
        if (self.energia<=0):
            print("Me cansé")
        else:
            print ("Estoy haciendo basicos") 
    def bailar_pareja(self):
        self.energia=self.energia-1
        print ("Jose Baila con Maria")
    def parar (self):
        pass

jose = Salsa()
maria = Salsa()

jose.bailar_pareja()
for _ in range (2):
    jose.hacer_basico()
    jose.hacer_patineta()
    for _ in range (3):
        maria.hacer_basico()
        maria.hacer_patineta()

# Iterable, es cualquier elemento que se pueda contar (Ej: lista) 
# (Lista: conjunto de valores que ocupan una pósición, iterable)

# La lista es mutable, la tupla es inmutable
