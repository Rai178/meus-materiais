sandwich_orders = ['banana', 'presunto', 'salame', 'cacau', 'nutela', 'morango']
finished_sandwich = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"fazendo seu sanduiche de {sandwich.title()}")
    finished_sandwich.append(sandwich)

print("\nForam feitos esses sanduiches")
for finished in finished_sandwich:
    print(finished.title())
