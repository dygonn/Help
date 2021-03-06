# Digitos verificadores (CNPJ)

def somentenumeros(entrada: object) -> bool:
    try:
        int(entrada)
        return True
    except:
        return False

while True:

    while True:
        cnpj = input ('Digite os sete primeiros digitos de seu CNPJ: ')
        if somentenumeros(cnpj) and (len(cnpj) == 7):
            filial = input ('Digite os 4 digitos da filial em questão: ')
            break
        else:
            print ('Erro! Valor digitado é invalido.')

    a = [int(i) for i in list (cnpj)]
    x = [int(i) for i in list (cnpj)]
    
    if (x[0] * 2) > 9:
        x[0] = (x[0] * 2) - 9
    else:
        x[0] = x[0] * 2
    if (x[1] * 1) > 9:
        x[1] = (x[1] * 1) - 9
    else:
        x[1] = x[1] * 1
    if (x[2] * 2) > 9:
        x[2] = (x[2] * 2) - 9
    else:
        x[2] = x[2] * 2
    if (x[3] * 1) > 9:
        x[3] = (x[3] * 1) - 9
    else:
        x[3] = x[3] * 1
    if (x[4] * 2) > 9:
        x[4] = (x[4] * 2) - 9
    else:
        x[4] = x[4] * 2
    if (x[5] * 1) > 9:
        x[5] = (x[5] * 1) - 9
    else:
        x[5] = x[5] * 1
    if (x[6] * 2) > 9:
        x[6] = (x[6] * 2) - 9
    else:
        x[6] = x[6] * 2

    y = x[0] + x[1] + x[2] + x[3] + x[4] + x[5] + x[6]

    if (y % 10) == 0:
        d1 = 0
    else:
        d1 = 10 - (y % 10)

# Digito verificador 1 encontrado.

    parcial1 = cnpj[:2]
    parcial2 = cnpj[2:5]
    parcial3 = cnpj[5:7] + str(d1)
    cnpjParcial = parcial1 + '.' + parcial2 + '.' + parcial3 + '/' + filial + '-'

    a.append(d1)

    lista_filial = [int(i) for i in list(filial)]
    
    a = a + lista_filial

    b = (a[0] * 5) + (a[1] * 4) + (a[2] * 3) + (a[3] * 2) + (a[4] * 9) + (a[5] * 8) + (a[6] * 7) + (a[7] * 6) + (a[8] * 5) + (a[9] * 4) + (a[10] * 3) + (a[11] * 2)

    c = 11 - (b % 11)

    if c == 10 or c == 11:
        d2 = 0
    else:
        d2 = c

# Digito verificador 2 encontrado.

    b = (a[0] * 6) + (a[1] * 5) + (a[2] * 4) + (a[3] * 3) + (a[4] * 2) + (a[5] * 9) + (a[6] * 8) + (a[7] * 7) + (a[8] * 6) + (a[9] * 5) + (a[10] * 4) + (a[11] * 3) + (d2 * 2)

    c = 11 - (b % 11)
    
    if c == 10 or c == 11:
        d3 = 0
    else:
        d3 = c

# Digito verificador 3 encontrado.

    digitosFinais = str(d2) + str(d3)
    cnpjCompleto = cnpjParcial + digitosFinais

    print ('Seu CNPJ completo é: ' + cnpjCompleto)    

# Desenvolvido por: @dygonn
# www.github.com/dygonn
# Comp.
