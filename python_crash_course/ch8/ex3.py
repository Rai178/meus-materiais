def transfer_data(source_list, destination_list):
    # Função para transferir dados de uma lista para outra
    while source_list:
        # Remove o primeiro item da lista de origem
        item = source_list.pop(0)
        destination_list.append(item)
        #mostra o processo para o usuário
        print(f"Transferindo {item} para a nova lista...")
        print(f"Lista de origem: {source_list}")
        print(f"Lista de destino: {destination_list}")

def main():
    # Lista inicial de números 
    original_list = [1, 2, 3, 4, 5]
    # Lista de destino vazia
    new_list = []

    # Chama a função para transferir dados
    transfer_data(original_list, new_list)

    # Mostra o resultado final
    print("transferencia completa!")
    print(f"Lista de origem: {original_list}")
    print(f"Lista de destino: {new_list}")

if __name__ == "__main__":
    main()