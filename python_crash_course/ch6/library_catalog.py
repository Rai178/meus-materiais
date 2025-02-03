pets = {
    'nino':{
        'porte':'grande',
        'raça':'labrador',
        'dono':'rai'
    },

    'vovo':{
        'porte':'pequeno',
        'raça':'pintin',
        'dono':'rosimere',
    },

    'costela':{
        'porte':'grande',
        'raça':'rotvaler',
        'dono':'valtecir',
    }
}
    
for name, pet in pets.items():
    print(f'Pet name: {name}')
    for key, value in pet.items():
        print(f'\t{key}:{value}')