studants = {
    'Rai': {
        'matematica': '10',
        'fisica': '10',
        'quimica': '5',
        'historia': '9.5',
        'artes': '4',
        'geografia': '6',
        'filosofia': '6',
        'portugues': '6',
        'redação': '8'
    },
    'Dara': {
        'matematica': '5',
        'fisica': '5',
        'quimica': '5',
        'historia': '10',
        'artes': '10',
        'geografia': '6',
        'filosofia': '6',
        'portugues': '8',
        'redação': '6'
    },
    'xico':  {
        'matematica': '10',
        'fisica': '10',
        'quimica': '5',
        'historia': '5',
        'artes': '4',
        'geografia': '6',
        'filosofia': '6',
        'portugues': '6',
        'redação': '8'
    }
}

for studant, data in studants.items():
    print(f'{studant}:')
    for key, value in data.items():
        print(f'\t{key}: {value}')