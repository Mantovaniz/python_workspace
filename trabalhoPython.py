#Integrantes: Beatriz, Sofia, Gabriel S, Giovana    -    CC2P12
import random
def exercicioTres():
    
    for i in range(5000):
        
        if not (i%3) :
            print(i," é múltiplo de 3")
        
    return

def exercicioQuatro():

    numeros = int(input("Quantos números deseja digitar? "))

    listaNumerica = []
    
    for i in range(numeros):

        numeroDigitado = float(input("Digite um número: "))
        
        listaNumerica.append(numeroDigitado)
        
    print("Lista completa:", listaNumerica)
    print("Maior valor: ", max(listaNumerica))
    return 

def exercicioCinco():

    lista = []
    soma = sum

    for i in range(5): 

            x= int (input("Entre com um valor: "))

            lista.insert (i, x)

    print(lista)
    print(soma(lista))
    return

def exercicioSeis():
    quant = int (input("Digite a quantidade de números que serão sorteados de -100 a 100: "))
    lista=[]

    for i in range(quant):
        x = int(random.randrange(-100,100))
        lista.insert(i, x)
        i+=1

    print("\n",lista, "\n\nMaior número: ", max(lista), "\nMenor número: ", min(lista), "\nSomatória: ", sum(lista), "\nMédia: ", sum(lista)/quant)
    return

def exercicioSete():
  
    for i in range(20):
            
        print(random.randrange(0,9))
    return

def exercicioOito():

    n1 = str(input ("Digite o nome do primeiro jogador: "))
    n2= str(input ("Digite o nome do segundo jogador: "))
    lista_1 = []

    for x in range(20):
        elen =random.randrange(0,9)
        lista_1.insert(x, elen)

        num1 = int (input("Primeiro jogador escolha os números de 0 á 9:"))
        num2 = int (input("Segundo jogador escolha os números de 0 á 9:"))

        qtd1 = lista_1.count(num1)
        qtd2 = lista_1.count(num2) 

        print (n1, "O seu numero", num1, "apareceu", qtd1, "vezes")
        print (n2, "O seu numero", num2, "apareceu", qtd2, "vezes")

        print("lista_1: ", lista_1)

        if (qtd1 > qtd2):
            print("Quem venceu foi o Jogador(a): ", n1)

        else:
            print("Quem venceu foi o Jogador(a): ", n2)

    return

def exercicioNove():

    lista =["Giovanna", "Sofia","Beatriz","Sandrin","Carmen","Ana Paula","Ivone","Glauber","Giovanni","Leonardo"]
    print(lista)

    nome= str(input("Digite o nome que deseja remover: "))
    lista.remove(nome)

    for i in range(1):
            print(lista," ")
    return

def exercicioDez():
    lista1=[]
    lista2=[]

    for i in range(9):
        x = int(random.randrange(-100,100))
        lista1.insert(i, x)
        y = int(random.randrange(-100,100))
        lista2.insert(i, y)
        i+=1


    z = int(input("Digite um número para colocar no final da lista: "))
    lista1.append(z)
    lista2.append(z)

    print("\nListas: ", lista1, " , ", lista2)
    print("\nListas concatenadas: ", lista1 + lista2)

    lista1.sort()
    lista2.reverse()

    print("\nLista 1 ordenada", lista1)
    print("\nLista 2 invertida: ", lista2)

    return

escolha = int(input("Digite uma opção entre 3 à 10: "))

if(escolha == 3):
        exercicioTres()
elif(escolha == 4):
        exercicioQuatro()
elif(escolha == 5):
        exercicioCinco()
elif(escolha == 6):
    exercicioSeis()
elif(escolha == 7):
        exercicioSete()
elif(escolha == 8):
        exercicioOito() 
elif(escolha == 9):
        exercicioNove()   
elif(escolha == 10):
        exercicioDez()
