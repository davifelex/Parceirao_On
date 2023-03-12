def cpf_mask(cpf):
    responce = ''
    position = 0
    for digit in str(cpf):
        responce += digit
        if position in [2, 5]:
            responce += '.'
        if position == 8:
            responce += '-'
        position += 1
    return responce

def cnpj_mask(cnpj):
    responce = ''
    position = 0

    for digit in str(cnpj).replace('.', '').replace('/', ''). replace('-', ''):
        responce += digit
        if position in [1, 4]:
            responce += '.'
        if position  == 7:
            responce += '/'
        if position == 11:
            responce += '-'
        position += 1
    return responce


# 1458.35
def money_mask(number):
    responce = ''
    try:
        item = f'{float(number):.2f}'
    except:
        return str(number)
        pass
    else:
        if not '.' in item:
            item += '.00'

        list_money = item.split('.')
        cents = list_money[1]
        item = list_money[0]
        invert_item = item[::-1]

        i = 0
        p = 0
        for digit in invert_item:
            if digit in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                responce += digit
            if p == 2 and (i + 1) != len(invert_item):
                responce += '.'
                p = 0
            else:
                p += 1
            i += 1

        responce = f'{responce[::-1]},{cents[0:2]}'
        return responce


def thousand_mask(number):
    responce = ''
    decimal = ''
    item = str(number)
    if '.' in item:
        list_item = item.split('.')
        decimal = list_item[1]
        item = list_item[0].replace(',', '')

    i = 0
    p = 0
    for digit in item[::-1]:
        if digit != '\n' and digit in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            responce += digit
            if p == 2 and i != (len(item) - 1):
                responce += '.'
                p = 0
            else:
                p += 1
        i += 1

    responce = responce[::-1]
    if decimal:
        responce = f'{responce},{decimal}'
    return responce


def number_input_mask(input_number):
    # 123456,45
    decimal = ''
    responce = ''
    item = rf'{input_number}'
    if ',' in item:
        sep = item.split(',')
        decimal = sep[1]
        item = sep[0]

    for digit in item:
        if digit == ',':
            responce += '.'
        if digit in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            responce += digit

    if decimal != '':
        responce = f'{responce}.{decimal}'
    return responce


def str_input_mask(input_str):
    responce = ''
    item = rf'{input_str}'.rstrip()
    responce = item
    return responce.strip()