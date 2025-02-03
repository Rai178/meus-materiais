favorite_languages = {'rai':'python', 'michaela':'business', 'xavier':'eletronics', 'gilson':'nada', 'eduardo':'viadagem', 'valdecir':None, 'julio':None, 'marcos':None}
for name, value in favorite_languages.items():
    if value == None:
        print(f'{name}, you need to answer the poll')
    else:
        print(f'thanks for answer the poll')
