cities = {
    'rio':{
        'country':'brazil',
        'population':'9 milions',
        'fact':'a very viotent place'
    },
    'são paulo':{
        'country':'brazil',
        'population':'50 milion',
        'fact':'the financial capital'
    },
    'espirito santo':{
        'country':'brazil',
        'population':'4 milions',
        'fact':'is a good place to live'
    }
}
for city, info in cities.items():
    print(f'{city}: ')
    for key, value in info.items():
        print(f'\n{key}:{value}')