work_lengths = {
    'naruto':6, 'rai':3, 'eduardo':7, 'valtecir':8, 'Deus': 4, 'gilcially':9
}
for name, value in work_lengths.items():
    if value>=5:
        print(f'{name}')
    else:
        print('The name is less than 5 letters')