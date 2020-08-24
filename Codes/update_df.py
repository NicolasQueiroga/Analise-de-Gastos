from data_frame_class import Df


dates = []
categories = []
titles = []
amounts = []
n = Df(dates, categories, titles, amounts)


print('------------------------------------------------------------------------------------------------------')
print('0 -> Adiciona transações manualmente\n1 -> Adiciona extrato em formato .csv')
typ = int(input('Digite o numero da ação desejada: '))
if typ == 1:
    extrato = True
    adding = False
else:
    adding = True
    extrato = False


while extrato:
    print('------------------------------------------------------------------------------------------------------')
    file = input('Arraste o arquivo .csv do extrato: ')
    answer = input('Quer adicionar outro arquivo?\n(y/n) ')
    n.adiciona_extrato(file)
    if answer == 'n':
        extrato = False


while adding:
    print('------------------------------------------------------------------------------------------------------')
    d = input('Entre a data da transação (yyyy-mm-dd):\n ')
    c = input('Qual é sua categoria?:\n ')
    t = input('Qual é a descrição breve da transação?:\n ')
    a = input('Digite o valor da transação (com duas casas decimais):\n ')
    dates.append(d)
    categories.append(c)
    titles.append(t)
    amounts.append(a)
    answer = input('Quer adicionar outra transação?\n(y/n) ')
    if answer == 'n':
        adding = False
        n.adiciona_transacao()
