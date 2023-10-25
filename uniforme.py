import datetime

nomes = []
tamanhos = []

while True:
    nome = input("Digite um nome (ou 'sair' para encerrar): ")

    if nome.lower() == 'sair':
        break  # Encerrar o loop se a entrada for 'sair'
    
    tamanho = input("Digite um tamanho (ou 'sair' para encerrar): ")

    if tamanho.lower() == 'sair':
        break  # Encerrar o loop se a entrada for 'sair'
    
    nomes.append(nome)
    tamanhos.append(tamanho)

data = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

for i in range(len(nomes)):
    print(f"O {nomes[i]} retirou o uniforme de tamanho {tamanhos[i]} às {data}")