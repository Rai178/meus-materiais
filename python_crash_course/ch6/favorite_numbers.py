favorite_number = {'rai':{'color':'blue',
                          'color1':'roxo',
                          'color2':'amarelo'}, 
                    'valtecir':{'color':'green',
                                'color1':'roxo',
                                'color2':'gray'}, 
                    'eduardo':{'color':'rosa',
                               'color1':'borboleta',
                               'color2':'arcoiris'}, 
                    'joaquim':{'color':'preto',
                                'color1':'rosa',
                                'color2':'roxo'}
}
for name, colors in favorite_number.items():
    print(f'The favorite number of {name} is:')
    for key, value in colors.items():
        print(f'\t{value}')