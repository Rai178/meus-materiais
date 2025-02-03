sandwich_orders = ['banana', 'pastrami', 'presunto', 'pastrami', 'salame',
                    'cacau', 'pastrami', 'nutela', 'morango']
finished_sandwich = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove("pastrami")

print("Pastrami has been removed of your code")

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"fazendo seu sanduiche de {sandwich.title()}")
    finished_sandwich.append(sandwich)

print("\nForam feitos esses sanduiches")
for finished in finished_sandwich:
    print(finished.title())
