import datetime
import json
from typing import List


class LivroIndisponivelError(Exception):
    pass


class UsuarioNaoRegistradoError(Exception):
    pass


class LimiteEmprestimosError(Exception):
    pass


class Livro:
    def __init__(self, titulo: str, autor: str, categoria: str):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.emprestado = False
        self.data_emprestimo = None
        self.usuario_atual = None

    def emprestar(self, usuario):
        if self.emprestado:
            raise LivroIndisponivelError(f"O livro '{self.titulo}' já está emprestado.")
        self.emprestado = True
        self.data_emprestimo = datetime.date.today()
        self.usuario_atual = usuario

    def devolver(self):
        self.emprestado = False
        self.data_emprestimo = None
        self.usuario_atual = None

    def esta_atrasado(self, dias_prazo=7):
        if not self.emprestado or not self.data_emprestimo:
            return False
        return (datetime.date.today() - self.data_emprestimo).days > dias_prazo

    def __str__(self):
        status = "Disponível" if not self.emprestado else f"Emprestado para {self.usuario_atual.nome}"
        return f"📖 {self.titulo} ({self.autor}) - {self.categoria} | {status}"


class Usuario:
    def __init__(self, nome: str, email: str, limite=3):
        self.nome = nome
        self.email = email
        self.limite = limite
        self.historico = []

    def __str__(self):
        return f" {self.nome} ({self.email}) - Já pegou {len(self.historico)} livros"


class Emprestimo:
    def __init__(self, livro: Livro, usuario: Usuario):
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = datetime.date.today()

    def calcular_multa(self, dias_prazo=7, valor_por_dia=2):
        dias_atraso = (datetime.date.today() - self.data_emprestimo).days - dias_prazo
        return max(0, dias_atraso * valor_por_dia)

    def __str__(self):
        return f"{self.livro.titulo} emprestado para {self.usuario.nome} em {self.data_emprestimo}"


class Biblioteca:
    def __init__(self):
        self.lista_livros: List[Livro] = []
        self.lista_usuarios: List[Usuario] = []
        self.lista_emprestimos: List[Emprestimo] = []

    def adicionar_livro(self, livro: Livro):
        self.lista_livros.append(livro)

    def registrar_usuario(self, usuario: Usuario):
        self.lista_usuarios.append(usuario)

    def buscar_usuario(self, nome: str):
        for u in self.lista_usuarios:
            if u.nome == nome:
                return u
        raise UsuarioNaoRegistradoError(f"Usuário {nome} não encontrado.")

    def buscar_livro(self, titulo: str):
        for l in self.lista_livros:
            if l.titulo == titulo:
                return l
        return None

    def emprestar_livro(self, usuario: Usuario, livro: Livro):
        if livro not in self.lista_livros:
            raise ValueError("Livro não pertence à biblioteca.")
        if len([e for e in self.lista_emprestimos if e.usuario == usuario]) >= usuario.limite:
            raise LimiteEmprestimosError("Usuário atingiu o limite de empréstimos.")

        livro.emprestar(usuario)
        emprestimo = Emprestimo(livro, usuario)
        self.lista_emprestimos.append(emprestimo)
        usuario.historico.append(livro)

    def devolver_livro(self, usuario: Usuario, livro: Livro):
        emprestimo = next((e for e in self.lista_emprestimos if e.livro == livro and e.usuario == usuario), None)
        if not emprestimo:
            raise ValueError("Este usuário não pegou este livro emprestado.")
        self.lista_emprestimos.remove(emprestimo)
        livro.devolver()

    def mostrar_catalogo(self):
        for livro in self.lista_livros:
            print(livro)

    def buscar_por_titulo_autor(self, termo: str):
        return [l for l in self.lista_livros if termo.lower() in l.titulo.lower() or termo.lower() in l.autor.lower()]

    def relatorio_emprestimos(self):
        for e in self.lista_emprestimos:
            multa = e.calcular_multa()
            print(f"{e} | Multa atual: R${multa:.2f}")


    def salvar(self, arquivo="biblioteca.json"):
        dados = {
            "livros": [{"titulo": l.titulo, "autor": l.autor, "categoria": l.categoria, "emprestado": l.emprestado} for l in self.lista_livros],
            "usuarios": [{"nome": u.nome, "email": u.email} for u in self.lista_usuarios]
        }
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def carregar(self, arquivo="biblioteca.json"):
        with open(arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
        for l in dados["livros"]:
            livro = Livro(l["titulo"], l["autor"], l["categoria"])
            livro.emprestado = l["emprestado"]
            self.lista_livros.append(livro)
        for u in dados["usuarios"]:
            self.lista_usuarios.append(Usuario(u["nome"], u["email"]))


def menu():
    bib = Biblioteca()
    while True:
        print("\n=== MENU BIBLIOTECA ===")
        print("1 - Adicionar livro")
        print("2 - Registrar usuário")
        print("3 - Emprestar livro")
        print("4 - Devolver livro")
        print("5 - Mostrar catálogo")
        print("6 - Relatório de empréstimos")
        print("7 - Salvar")
        print("8 - Carregar")
        print("0 - Sair")
        opcao = input("Escolha: ")

        try:
            if opcao == "1":
                titulo = input("Título: ")
                autor = input("Autor: ")
                categoria = input("Categoria: ")
                bib.adicionar_livro(Livro(titulo, autor, categoria))
            elif opcao == "2":
                nome = input("Nome: ")
                email = input("Email: ")
                bib.registrar_usuario(Usuario(nome, email))
            elif opcao == "3":
                nome = input("Usuário: ")
                titulo = input("Livro: ")
                u = bib.buscar_usuario(nome)
                l = bib.buscar_livro(titulo)
                if not l:
                    print("Livro não encontrado.")
                else:
                    bib.emprestar_livro(u, l)
            elif opcao == "4":
                nome = input("Usuário: ")
                titulo = input("Livro: ")
                u = bib.buscar_usuario(nome)
                l = bib.buscar_livro(titulo)
                bib.devolver_livro(u, l)
            elif opcao == "5":
                bib.mostrar_catalogo()
            elif opcao == "6":
                bib.relatorio_emprestimos()
            elif opcao == "7":
                bib.salvar()
                print("Dados salvos.")
            elif opcao == "8":
                bib.carregar()
                print("Dados carregados.")
            elif opcao == "0":
                break
        except Exception as e:
            print("Erro:", e)


if __name__ == "__main__":
    menu()
