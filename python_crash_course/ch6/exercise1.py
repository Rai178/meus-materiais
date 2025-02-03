shopping_list = {
    'casa':{'primeiro':'como melhorar a pressão da agua', 'segundo':'acabar com as goteiras na pia', 'terceiro':'colocar uma descarga',
            'quarto':'janela no banheiro e fechar a parte de cima', 'quinto':'porta no banheiro', 'sexto':'colocar a janela', 'setimo':'trocar a fechadura da casa',
            'oitavo':'organizar os fios que estão pela casa', 'nono':'passar argamassa nas paredes', 'decimo':'pintar as paredes', 'decimo primeiro':'pvc no teto'},
    'estudo':{'primeiro':'acessorios celular', 'segundo':'base superior notebook', 'terceiro':'parafusos notebook', 'quarto':'bateria notebook'}
}

for casa, position in shopping_list.items():
    print(f'{casa}:')
    for key, value in position.items():
        print(f'\t {key}:  {value}')