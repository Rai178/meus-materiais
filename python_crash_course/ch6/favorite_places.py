favorite_places = {
    'rai':{
        'place1':'praia',
        'place2':'casa',
        'place3':'trabalho'
    },

    'valtecir':{
        'place1':'igreja',
        'place2':'casa',
        'place3':'monte'
    },

    'rosaly':{
        'place1':'praia',
        'place2':'brecho',
        'place3':'casa'
    }
}

for name, place in favorite_places.items():
    print(f'The favorite places for {name} is:')
    for key, value in place.items():
        print(f'{value}')