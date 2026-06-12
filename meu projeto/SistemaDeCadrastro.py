clientes = []

def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    
    cliente = {
        "nome": nome,
        "email": email,
        "telefone": telefone
    }
    
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

def listar_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    
    print("Lista de Clientes:")
    for idx, cliente in enumerate(clientes, start=1):
        print(f"{idx}. Nome: {cliente['nome']}, Email: {cliente['email']}, Telefone: {cliente['telefone']}")
def menu():
    while True:
        print("\nSistema de Cadastro de Clientes")
        print("1. Cadastrar Cliente")
        print("2. Listar Clientes")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            cadastrar_cliente()
        elif escolha == '2':
            listar_clientes()
        elif escolha == '3':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":    menu()
