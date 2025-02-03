def transfer_data(source_list, destination_list):
    for item in source_list[:]:
        destination_list.append(item)
        source_list.remove(item)
    print(f"Transferindo {item} para a nova lista...")
    print(f"Lista de origem: {destination_list}")
    print(f"Lista de destino: {source_list}")

def tasks():
    to_make = ['clean', 'lunch', 'study', 'dog']
    finished = []

    transfer_data(to_make, finished)
    print("transfer complete!")
    print(f"origin list: {to_make}")
    print(f"destination list: {finished}")

tasks()