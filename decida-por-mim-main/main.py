from time import sleep
import random


class DecidaPorMim():
    def __init__(self):
        self.respostas = [
            'Não faço ideia.',
            'Só sei que nada sei.',
            'Tá maluco?',
            'Com certeza... não.',
            'É claro que sim.',
            'Tá pegando fogo bicho!!!',
            'Oloko meu.',
            'Vamoooos aplaudiiirr!',
            'Loucura, loucura, loucura.',
            'Robooooooooooooooooooo!',
        ]

    def Menu(self):
        print('* Seja muito bem-vindo ao programa "Decida por mim". *')
        print()
        print()
        self.iniciar = input(
            'Espero que se divirta! (Digite I para iniciar) ').lower()

        if self.iniciar == 'i':
            self.Iniciar()
        elif self.iniciar != 'i':
            print('Até breve!')

    def Iniciar(self):
        self.DuvidaDoUsuario()
        print('Pensando...')
        sleep(3)
        self.resposta = self.EscolhendoAResposta()
        print(self.resposta)
        sleep(2)
        self.DesejaContinuar()

    def DesejaContinuar(self):
        self.deseja_continuar = input(
            'Deseja fazer-me outra pergunta?(s/n) ').lower()

        if self.deseja_continuar == 's':
            self.Iniciar()
        elif self.deseja_continuar == 'n':
            print('Até mais!')
            while True:
                break
        else:
            print('Por favor, digite "s" para sim ou "n" para não.')
            self.DesejaContinuar()

    def DuvidaDoUsuario(self):
        self.duvida = input("Faça-me uma pergunta: ")

    def EscolhendoAResposta(self):
        return random.choice(self.respostas)


start = DecidaPorMim()
start.Menu()
