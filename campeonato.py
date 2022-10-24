quantTimes = 0
quantChaves = 0
cont = 0

times = []
chaves = []

quantTimes = int(input("Digite a quantidade de times que deseja cadastrar: "))

for i in range(quantTimes):
    times.append(str(input("Digite o nome do time: ")))

print("\nTimes cadastrados: " , times)

quantChaves = int(input("\nDigite a quantidade de chaves que deseja criar: "))

print("\nChaves criadas: ")
splited = [times[i::quantChaves] for i in range(quantChaves)]
print(splited)
