# ===============================================================
#                 EJEMPLO DE TÉCNICAS DE PROGRAMACIÓN
#                        TEMA: ANIMALES
# Abstracción     → Clases que representan animales y su lógica.
# Encapsulación   → Atributos internos dentro de las clases.
# Herencia        → León y Elefante heredan de Animal.
# Polimorfismo    → Cada animal hace sonido y ataca diferente.
# ===============================================================


# ------------------------------ #
#            CLASE PADRE         #
# ------------------------------ #
class Animal:
    # Constructor con atributos básicos (Encapsulación)
    def __init__(self, nombre, fuerza, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.defensa = defensa
        self.vida = vida

    # Abstracción → Método que muestra atributos esenciales
    def atributos(self):
        print(f"\n{self.nombre}:")
        print("· Fuerza:", self.fuerza)
        print("· Defensa:", self.defensa)
        print("· Vida:", self.vida)

    # Metodo para saber si sigue vivo
    def esta_vivo(self):
        return self.vida > 0

    # Cuando muere
    def morir(self):
        self.vida = 0
        print(f"{self.nombre} ha fallecido...")

    # Daño base (se sobrescribe en clases hijas → polimorfismo)
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    # Acción de ataque
    def atacar(self, enemigo):
        daño_real = self.daño(enemigo)
        enemigo.vida -= daño_real
        print(f"{self.nombre} atacó a {enemigo.nombre} causando {daño_real} de daño.")
        
        if enemigo.esta_vivo():
            print(f"Vida de {enemigo.nombre}: {enemigo.vida}")
        else:
            enemigo.morir()


# ------------------------------ #
#        HERENCIA: LEÓN          #
# ------------------------------ #
class Leon(Animal):
    def __init__(self, nombre, fuerza, defensa, vida, melena):
        super().__init__(nombre, fuerza, defensa, vida)
        self.melena = melena  # Atributo adicional propio

    def atributos(self):
        super().atributos()
        print("· Melena:", self.melena)

    # Polimorfismo → El león causa daño usando su rugido feroz
    def daño(self, enemigo):
        return (self.fuerza + self.melena) - enemigo.defensa


# ------------------------------ #
#       HERENCIA: ELEFANTE       #
# ------------------------------ #
class Elefante(Animal):
    def __init__(self, nombre, fuerza, defensa, vida, peso):
        super().__init__(nombre, fuerza, defensa, vida)
        self.peso = peso  # Atributo adicional propio

    def atributos(self):
        super().atributos()
        print("· Peso:", self.peso)

    # Polimorfismo → El elefante hace daño con embestida pesada
    def daño(self, enemigo):
        return (self.fuerza + self.peso // 10) - enemigo.defensa


# ------------------------------ #
#        FUNCIÓN DE COMBATE      #
# ------------------------------ #
def combate(a1, a2):
    turno = 1
    while a1.esta_vivo() and a2.esta_vivo():
        print(f"\n======== Turno {turno} ========")

        print(f"Acción de {a1.nombre}:")
        a1.atacar(a2)

        if not a2.esta_vivo():
            break

        print(f"Acción de {a2.nombre}:")
        a2.atacar(a1)

        turno += 1

    print("\n===== FIN DEL COMBATE =====")
    if a1.esta_vivo():
        print("¡Ganador:", a1.nombre, "!")
    elif a2.esta_vivo():
        print("¡Ganador:", a2.nombre, "!")
    else:
        print("Empate inesperado ")


# ------------------------------ #
#      CREACIÓN DE OBJETOS       #
# ------------------------------ #

animal_1 = Leon("Simba", 20, 5, 120, melena=8)
animal_2 = Elefante("Dumbo", 18, 10, 150, peso=600)

animal_1.atributos()
animal_2.atributos()

combate(animal_1, animal_2)