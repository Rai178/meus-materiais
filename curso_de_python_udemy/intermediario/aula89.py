# dir, hasattr e getattr em python
string = 'luiz'
metodo = 'upper'

if hasattr(string, 'upper'):
    print('Existe upper')
    print(getattr(string, metodo))
    print(string)