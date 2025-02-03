def send_messages(message, destination):
    while message:
        item = message.pop()
        destination.append(item)
        print(f'moving {item}...')
        print(f'Origin list: {message}')
        print(f'Destination: {destination}')
    
def show_messages():
    message = ['Aquele que habita no esconderijo do altissimo',
               'à sombra do onipotente descansará',
               'Direi do senhor: tu és o meu abrigo, o meu refúgio',
               'Ele te livrará do laço do caçador e da peste perniciosa',
               'Ele o cobrirá com suas penas e sub suas asas encontrarás refugio',
               'a fidelidade dele será o seu escudo protetor',
               'você não temerá o pavor da noite, nem a flecha que voa de dia',
               'nem a peste que se move sorrateira nas trevas, nem a praga que devasta ao meio dia',
               'mil poderão cair ao teu lado, dez mil a sua direi, mas nada o atingirá',]
    dest = []
    
    send_messages(message, dest)

show_messages()