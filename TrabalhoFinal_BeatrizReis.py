import random

def exerc1():
    lista=[]

    for i in range(20):
        x = int(random.randrange(0,10))
        lista.insert(i, x)
        i+=1

    def ordenadaCrescente(lista):
        lista.sort()
        print("\nA - Lista ordenada crescente: ", lista)

    def ordenadaDecrescente(lista):
        lista.reverse()
        print("B - Lista ordenada decrescente: ", lista)

    def maiorNum(lista):
        print("C - Maior número da lista: ", max(lista))

    def menorNum(lista):
        print("D - Menor número da lista: ", min(lista))

    def soma(lista):
        print("E - Soma dos valores da lista: ", sum(lista))

    def tira5(lista):
        for i in lista:
            if(5 in lista):
                lista.remove(5)

            else:
                break
        print("F - Lista sem o número 5: ", lista)

    print("\n\n-- Exercício 1 --")
    ordenadaCrescente(lista)
    ordenadaDecrescente(lista)
    maiorNum(lista)
    menorNum(lista)
    soma(lista)
    tira5(lista)

    clear()
    exerc5()
    return

def exerc2():
    print("\n\n-- Exercício 2 --")
    array=[]
    
    for i in range(10):
        x = int(random.randrange(0,50))
        array.insert(i, x)
        i+=1

    print("\nValores sorteados: ", array)

    for i in range(10):
        if(array[i]<25):
            array[i] = array[i] + 10

        elif(array[i]>=25):
            array[i] = array[i] - 5 
        i+=1

    print("\n\nValores depois do calculo: ", array)

    clear()
    exerc5()
    return

def exerc3():
    print("\n\n-- Exercício 3 --")

    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

    dia, mes, ano = input("\nDigite uma data de nascimento (dd/mm/aaaa): ").split('/')
    
    print("\nVocê nasceu no dia ", dia, " de ", meses[int(mes)-1], " de ", ano)

    clear()
    exerc5()
    return

def exerc4():
    print("\n\n-- Exercício 4 --")

    conteudo = 'This is just a simple string'

    conteudo2 = conteudo.split('simple')
    conteudo2 = str(conteudo2[1])

    print("\nA - Frase: ", conteudo)
    print("\nB - Quantidade de caracteres da frase: ", len(conteudo))
    print("\nC - Substituição de simple por short: ", conteudo.replace('simple', 'short'))
    print("\nD - Posição da primeira letra da palavra 'string': ", conteudo2.find('s') )
    print("\nE - Primeira letra de cada palavra em maiúsculo: ", conteudo.title())

    clear()
    exerc5()
    return

def exerc5():
    print("________________________")
    print("|-_-_-_- OPÇÕES -_-_-_-|")
    print("|                      |")
    print("|  1. Exercício 1      |")
    print("|  2. Exercício 2      |")
    print("|  3. Exercício 3      |")
    print("|  4. Exercício 4      |")
    print("|  0. Encerrar         |")
    print("|                      |")
    print("+---+-+-+-+-+-+-+-+-+--+")
    escolha = int(input("\nDigite uma opção: "))

    if(escolha == 1):
        exerc1()
    elif(escolha == 2):
        exerc2()
    elif(escolha == 3):
        exerc3()
    elif(escolha == 4):
        exerc4()
    else:
        print("\nPrograma encerrado!")
    return

def clear():
    print("\n")

exerc5()