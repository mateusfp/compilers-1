
email = 'guihss.cs@gmail.com'


# Exemplo
def verify_email(email):
    prefix = True
    domain = False

    for c in list(email):

        if prefix:

            if c.isalnum() or c == '.':
                continue
            elif c == '@':
                prefix = False
                domain = True
                continue
            else:
                print(c, 'is invalid')
                return False

        elif domain:

            if c.isalnum() or c == '.':
                continue

            else:
                print(c, 'is invalid')
                return False


    if prefix:
        return False

    return True


def verify_date(date):

    pass



def toInt(number):

    pass

#Crie um programa que verifica se uma data está correta

def data(dia, mes, ano):
    dia = int(input("Digite O Dia: "))
    mes = int(input("Digite o Mês: "))
    ano = int(input("Digite o Ano: "))

    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        M_Dias = 31
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        M_Dias = 30
    elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        M_Dias = 29
    else:
        M_Dias = 28

    if mes < 1 or mes > 12:
        print("Data Inválida: ")
    elif dia < 1 or dia > M_Dias:
        print("Data inválida")
    else:
        print("Data Válida")





#Crie um programa que converta de string para números inteiros


string1 = '12,20,21,22,23,24,25'

int_list = list(map(int,string1.split(',')))
print(int_list)
print(string1.isnumeric())
print('----------------------')


