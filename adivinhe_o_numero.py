import PySimpleGUI as Psg
from random import randint

# Criando janelas


def janela_regras():
    Psg.theme('DarkBrown')
    layout = [
        [Psg.Push(), Psg.Text('Jogo Adivinhe o número!', font=('times', 30)), Psg.Push()],
        [Psg.Push(), Psg.Text('Chute números de 1 à 10 até acertar o número aleátorio',
                              font=('times', 18)), Psg.Push()],
        [Psg.Push(), Psg.Button('INICIAR', font=('times', 20)), Psg.Push()]
    ]
    return Psg.Window('ADIVINHE O NÚMERO', layout, size=(600, 200), finalize=True)


def janela_jogo():
    Psg.theme('DarkBrown')
    layout = [
        [Psg.Push(), Psg.Text('Digite o número abaixo!', font=('times', 20)), Psg.Push()],
        [Psg.Push(), Psg.InputText(key='input', size=(30, 0)), Psg.Push()],
        [Psg.Push(), Psg.Button('CONFIRMAR'), Psg.Push()]
    ]
    return Psg.Window('ADIVINHE O NÚMERO', layout, size=(600, 300), finalize=True)


def verifica_input(x: str):  # Função que verifica se o valor digitado no input é um numero ou se está entra 1 e 10.
    try:
        num = int(x)
        if num > 10 or num < 1:
            return False
        else:
            return True
    except ValueError:
        return False


numero_aleatorio = randint(1, 10)
janelaRegras, janelaJogo, janelaErro = janela_regras(), None, None

while True:
    janela_em_uso, evento, valor = Psg.read_all_windows()
    if evento == Psg.WIN_CLOSED:
        break
    elif evento == 'INICIAR':
        janelaRegras.close()
        janelaJogo = janela_jogo()
    if evento == 'CONFIRMAR':
        if verifica_input(valor['input']):
            input_user = int(valor['input'])
            if input_user > numero_aleatorio:
                Psg.popup('Menor!')
            elif input_user < numero_aleatorio:
                Psg.popup('Maior!')
            else:
                Psg.popup(f'Parabéns, você acertou! O número era {numero_aleatorio}', title='PARABÉNS'),
        else:
            Psg.popup('O valor digitado não é um numero ou não está entre 1 e 10!', title='ERRO!')



