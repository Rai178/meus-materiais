import random

class Personagem:
    def __init__(self, nome, vida, forca, agilidade, destreza):
        self.nome = nome
        self.vida = vida
        self.forca = forca
        self.agilidade = agilidade
        self.destreza = destreza

    def eficacia_ataque(self, forca_atacante, agilidade_atacante, vida_defensor, destreza_defensor):
        # Implemente a lógica de ataque aqui
        random_factor = random.uniform(0.8, 1.2)
        self.eficacia = (forca_atacante * agilidade_atacante - vida_defensor * destreza_defensor) * random_factor
        return self.eficacia
    
    def eficacia_defesa(self, forca_atacante, agilidade_atacante, vida_defensor, destreza_defensor):

class Combate:
    # Implemente a classe Monstro de forma similar à classe personagem
    pass

    def combate(personagem, monstro):
        # Implemente a lógica de combate aqui
        pass

# Criação de um personagem e um monstro
heroi = Personagem("Arthur", 100, 12, 10, 8)
goblin = Monstro("Gobrin", 50, 8, 12, 6)

# Inicio do combate
combate(heroi, goblin)