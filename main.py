class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == 'mago':
            ataque = 'magia'
        elif self.tipo == 'guerreiro':
            ataque = 'espada'
        elif self.tipo == 'monge':
            ataque = 'artes marciais'
        elif self.tipo == 'ninja':
            ataque = 'shuriken'
        else:
            ataque = 'um ataque genérico'

        print(f"O {self.tipo} atacou usando {ataque}")
        

nome = input("Digite o nome do herói: ")
idade = int(input("Digite a idade do herói: "))
tipo = input("Digite o tipo do herói (mago, guerreiro, monge ou ninja): ")

heroi = Heroi(nome, idade, tipo)
heroi.atacar()