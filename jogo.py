import random

frutas = [['Morango'], ['Coco'], ['Banana'], ['Abacaxi'], ['Limão'], ['Laranja'], ['Maçã'], ['Pera'], ['Uva']]
veiculos = [['Onibus'], ['Carro'], ['Moto'], ['Trem'], ['Carro'], ['Trator'], ['Caminhão'], ['Carroça']]
animais = [['Macaco'], ['Girafa'], ['Gato'], ['Cachorro'], ['Gorila'], ['Zebra'], ['Boi'], ['Cavalo'], ['Rato']]
listaErradas = list()
listaCertas = list()

def linha():
    print('\033[1;94m' + '~' * 30 + '\033[0;0m')


def f_jogo():
    lista_frutas = random.choice(frutas)
    lista_veiculos = random.choice(veiculos)
    lista_animais = random.choice(animais)
    tudo = (lista_frutas[0], lista_veiculos[0], lista_animais[0])
    fase = random.choice(tudo)
    
    print(f'Digite a relação do item: {fase}')
    print(f'[1] para Fruta\n'
          f'[2] para Veículo\n'
          f'[3] para Animal\n')
    linha()
    escolha = int(input('Escolha uma opção: '))

    print(f'Resultado fase {fase} e escolha {escolha}')

    if escolha == 1:
        if fase in lista_frutas:
            print('\033[1;92m' + 'CERTA RESPOSTA!' + '\033[0;0m')
            listaCertas.append(1)
        else:
            print('\033[1;31m' + 'RESPOSTA ERRADA!' + '\033[0;0m')
            listaErradas.append(1)

    elif escolha == 2:
        if fase in lista_veiculos:
            print('\033[1;92m' + 'CERTA RESPOSTA!' + '\033[0;0m')
            listaCertas.append(1)
        else:
            print('\033[1;31m' + 'RESPOSTA ERRADA!' + '\033[0;0m')
            listaErradas.append(1)

    elif escolha == 3:
        if fase in lista_animais:
            print('\033[1;92m' + 'CERTA RESPOSTA!' + '\033[0;0m')
            listaCertas.append(1)
        else:
            print('\033[1;31m' + 'RESPOSTA ERRADA!' + '\033[0;0m')
            listaErradas.append(1)


    else:
        print('Opção invalida, tente novamente.')

    linha()
    querJogar= int(input('\nQuer jogar de novo?\n'
                         '[1] Sim     [2] Não: '))
    linha()
    while querJogar == 1:
        print('\n\n')
        f_jogo()
        break
    

linha()
print(('\033[;1m' + '\033[1;33m' + 'JOGO DE RELACIONAR' + '\033[0;0m'))
linha()

f_jogo()


print('\033[;1m' + '\033[1;33m' + 'Fim do jogo!! Seu resultado foi:' + '\033[0;0m')
print(f'\nA quantidade de respostas certas foram: {len(listaCertas)}\nA quantidade de respostas erradas foram: {len(listaErradas)}')
linha()
