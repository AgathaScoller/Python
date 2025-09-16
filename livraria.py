from datetime import datetime

class Autor:
    def __init__(self, nome: str, nacionalidade: str, ano_nascimento: int):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.ano_nascimento = ano_nascimento

    def __str__(self):
        return f"{self.nome} ({self.nacionalidade}, {self.ano_nascimento})"


class Livro:
    def __init__(self, titulo: str, autor: Autor, genero: str, edicao: int, paginas: int, preco: float):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.edicao = edicao
        self.paginas = paginas
        self.preco = preco

    def __str__(self):
        return f"'{self.titulo}' - {self.autor.nome} | Gênero: {self.genero} | {self.paginas} págs. | R${self.preco:.2f}"


class Cliente:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf
        self.historico_compras = []

    def adicionar_compra(self, pedido):
        self.historico_compras.append(pedido)

    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf})"


class Pedido:
    def __init__(self, cliente: Cliente):
        self.cliente = cliente
        self.livros = []
        self.data = datetime.now()
        self.status = "Em aberto"

    def adicionar_livro(self, livro: Livro, quantidade: int = 1):
        self.livros.append((livro, quantidade))

    def calcular_total(self):
        return sum(livro.preco * qtd for livro, qtd in self.livros)

    def finalizar_pedido(self):
        self.status = "Finalizado"
        self.cliente.adicionar_compra(self)

    def __str__(self):
        livros_str = "\n".join([f"{livro.titulo} (x{qtd})" for livro, qtd in self.livros])
        return (
            f"Pedido de {self.cliente.nome} em {self.data.strftime('%d/%m/%Y %H:%M')}\n"
            f"Livros:\n{livros_str}\n"
            f"Total: R${self.calcular_total():.2f} | Status: {self.status}"
        )


class Livraria:
    def __init__(self, nome: str):
        self.nome = nome
        self.catalogo = []
        self.clientes = []
        self.pedidos = []

    def adicionar_livro(self, livro: Livro):
        self.catalogo.append(livro)

    def cadastrar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def registrar_pedido(self, pedido: Pedido):
        self.pedidos.append(pedido)

    def listar_livros(self):
        if not self.catalogo:
            print("\nNenhum livro cadastrado.")
            return
        print(f"\nCatálogo da {self.nome}:")
        for i, livro in enumerate(self.catalogo, start=1):
            print(f"{i}. {livro}")

    def listar_clientes(self):
        if not self.clientes:
            print("\nNenhum cliente cadastrado.")
            return
        print("\nClientes cadastrados:")
        for i, cliente in enumerate(self.clientes, start=1):
            print(f"{i}. {cliente}")

    def listar_pedidos(self):
        if not self.pedidos:
            print("\nNenhum pedido registrado.")
            return
        print("\nPedidos registrados:")
        for i, pedido in enumerate(self.pedidos, start=1):
            print(f"\n{i}. {pedido}")

    def __str__(self):
        return f"Livraria {self.nome} | Livros: {len(self.catalogo)} | Clientes: {len(self.clientes)}"


def main():
    livraria = Livraria("Mundo dos Livros")
    print("=== Bem-vindo à Livraria Mundo dos Livros ===")

    while True:
        print("\nEscolha uma opção:")
        print("1 - Cadastrar autor e livro")
        print("2 - Cadastrar cliente")
        print("3 - Fazer pedido")
        print("4 - Listar livros")
        print("5 - Listar clientes")
        print("6 - Listar pedidos")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            nome_autor = input("Nome do autor: ")
            nacionalidade = input("Nacionalidade: ")
            ano_nasc = int(input("Ano de nascimento: "))
            autor = Autor(nome_autor, nacionalidade, ano_nasc)

            titulo = input("Título do livro: ")
            genero = input("Gênero: ")
            edicao = int(input("Edição: "))
            paginas = int(input("Número de páginas: "))
            preco = float(input("Preço: "))
            livro = Livro(titulo, autor, genero, edicao, paginas, preco)
            livraria.adicionar_livro(livro)
            print(f"\nLivro cadastrado: {livro}")

        elif opcao == "2":
            nome_cliente = input("Nome do cliente: ")
            cpf_cliente = input("CPF do cliente: ")
            cliente = Cliente(nome_cliente, cpf_cliente)
            livraria.cadastrar_cliente(cliente)
            print(f"\nCliente cadastrado: {cliente}")

        elif opcao == "3":
            if not livraria.clientes:
                print("\nCadastre pelo menos um cliente antes de fazer um pedido.")
                continue
            if not livraria.catalogo:
                print("\nCadastre pelo menos um livro antes de fazer um pedido.")
                continue

            print("\nEscolha o cliente pelo número:")
            livraria.listar_clientes()
            idx_cliente = int(input("Número do cliente: ")) - 1
            cliente = livraria.clientes[idx_cliente]
            pedido = Pedido(cliente)

            while True:
                livraria.listar_livros()
                escolha = input("Número do livro para adicionar ao pedido (0 para finalizar): ")
                if escolha == '0':
                    break
                try:
                    indice = int(escolha) - 1
                    qtd = int(input("Quantidade: "))
                    pedido.adicionar_livro(livraria.catalogo[indice], qtd)
                    print(f"Livro adicionado: {livraria.catalogo[indice].titulo} x{qtd}")
                except (IndexError, ValueError):
                    print("Opção inválida. Tente novamente.")

            pedido.finalizar_pedido()
            livraria.registrar_pedido(pedido)
            print("\nPedido finalizado com sucesso!")

        elif opcao == "4":
            livraria.listar_livros()

        elif opcao == "5":
            livraria.listar_clientes()

        elif opcao == "6":
            livraria.listar_pedidos()

        elif opcao == "0":
            print("Saindo... Até logo!")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()

