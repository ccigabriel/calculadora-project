# Calculadora com interface que lê os gastos do cliente, onde esses gastos podem ser definidos por ele. E que no final diga quanto dinheiro sobrou calculando isso pelo valor do salario dele
gastos = {}

while True:

    valor_gastos = float(input('Digite o seu gasto: R$ '))
    if valor_gastos == str:
        print('Por favor, digite um valor. ')

    nome_gastos = input('Qual o nome do seu gasto? ')
    # Usar a variável nome_gastos como chave
    gastos[nome_gastos] = valor_gastos

    continuar = str(input('Quer continuar?  S/N  ')).upper().strip()
    if continuar != 'S':
        break

for nome, valor in gastos.items():  # Items = items do dicionario 'gastos'
    print(f'{nome}: R${valor:.2f}')

    #teste git
