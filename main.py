import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Função para conectar ao banco de dados
def conectar_banco_completo():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",  # Substitua pela sua senha do MySQL
            database="sistema_vendas"
        )
        return conexao
    except mysql.connector.Error as err:
        print(f"Erro de conexão: {err}")
        return None

# Funções de Login e Cadastro de Usuários
def login_usuario(usuario, senha):
    conexao = conectar_banco_completo()
    cursor = conexao.cursor(dictionary=True)
    query = "SELECT * FROM usuarios WHERE usuario = %s AND senha = %s"
    cursor.execute(query, (usuario, senha))
    resultado = cursor.fetchone()
    conexao.close()
    return resultado

def cadastrar_usuario(nome, usuario, senha, tipo="vendedor"):
    conexao = conectar_banco_completo()
    cursor = conexao.cursor()
    query = "INSERT INTO usuarios (nome, usuario, senha, tipo) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (nome, usuario, senha, tipo))
    conexao.commit()
    conexao.close()

# Funções de Clientes
def cadastrar_cliente(nome, email, telefone):
    conexao = conectar_banco_completo()
    cursor = conexao.cursor()
    query = "INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)"
    cursor.execute(query, (nome, email, telefone))
    conexao.commit()
    conexao.close()

# Funções de Produtos
def cadastrar_produto_bd(nome, descricao, preco, categoria, codigo_barras, estoque):
    conexao = conectar_banco_completo()
    cursor = conexao.cursor()
    query = "INSERT INTO produtos (nome, descricao, preco, categoria, codigo_barras, estoque) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (nome, descricao, preco, categoria, codigo_barras, estoque))
    conexao.commit()
    conexao.close()

def listar_produtos():
    conexao = conectar_banco_completo()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conexao.close()
    return produtos

# Funções de Vendas
def realizar_venda_bd(produto_id, quantidade, valor_total):
    conexao = conectar_banco_completo()
    cursor = conexao.cursor()
    query = "INSERT INTO vendas (produto_id, quantidade, valor_total) VALUES (%s, %s, %s)"
    cursor.execute(query, (produto_id, quantidade, valor_total))
    conexao.commit()
    conexao.close()

def listar_vendas():
    conexao = conectar_banco_completo()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vendas")
    vendas = cursor.fetchall()
    conexao.close()
    return vendas

# Função para gerar relatório de vendas
def gerar_relatorio_vendas():
    return listar_vendas()

# Interface gráfica com Tkinter
class SistemaVendas:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Vendas de Eletrônicos")
        self.root.geometry("800x600")
        
        self.tabControl = ttk.Notebook(root)
        self.tab_login = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab_login, text="Login")
        self.tabControl.pack(expand=1, fill="both")
        self.tela_login()

    def tela_login(self):
        tk.Label(self.tab_login, text="Usuário:").grid(row=0, column=0, padx=10, pady=10)
        self.usuario_entry = tk.Entry(self.tab_login)
        self.usuario_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(self.tab_login, text="Senha:").grid(row=1, column=0, padx=10, pady=10)
        self.senha_entry = tk.Entry(self.tab_login, show="*")
        self.senha_entry.grid(row=1, column=1, padx=10, pady=10)
        
        login_button = tk.Button(self.tab_login, text="Login", command=self.fazer_login)
        login_button.grid(row=2, column=0, columnspan=2, pady=10)
    
    def fazer_login(self):
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()
        resultado = login_usuario(usuario, senha)
        if resultado:
            messagebox.showinfo("Login", "Login realizado com sucesso!")
            self.criar_abas_principais()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

    def criar_abas_principais(self):
        self.tabControl.forget(self.tab_login)
        
        self.tab_cadastro_usuario = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab_cadastro_usuario, text="Cadastro de Usuários")
        
        self.tab_clientes = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab_clientes, text="Clientes")
        
        self.tab_produtos = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab_produtos, text="Produtos")
        
        self.tab_vendas = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab_vendas, text="Vendas")
        
        self.tab_relatorios = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab_relatorios, text="Relatórios")

        # Botão de sair para retornar ao login
        sair_button = tk.Button(self.root, text="Sair", command=self.sair)
        sair_button.pack(pady=10)

        self.tela_cadastro_usuario()
        self.tela_clientes()
        self.tela_produtos()
        self.tela_vendas()
        self.tela_relatorios()

    def sair(self):
        """Função para sair da sessão e retornar à tela de login."""
        for tab in self.tabControl.tabs():
            self.tabControl.forget(tab)  # Remove todas as abas principais
        self.tabControl.add(self.tab_login, text="Login")  # Volta à tela de login
        self.usuario_entry.delete(0, tk.END)
        self.senha_entry.delete(0, tk.END)

    def tela_cadastro_usuario(self):
        tk.Label(self.tab_cadastro_usuario, text="Nome Completo:").grid(row=0, column=0, padx=10, pady=10)
        self.nome_usuario_entry = tk.Entry(self.tab_cadastro_usuario)
        self.nome_usuario_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(self.tab_cadastro_usuario, text="Usuário:").grid(row=1, column=0, padx=10, pady=10)
        self.usuario_novo_entry = tk.Entry(self.tab_cadastro_usuario)
        self.usuario_novo_entry.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(self.tab_cadastro_usuario, text="Senha:").grid(row=2, column=0, padx=10, pady=10)
        self.senha_nova_entry = tk.Entry(self.tab_cadastro_usuario, show="*")
        self.senha_nova_entry.grid(row=2, column=1, padx=10, pady=10)
        
        tk.Button(self.tab_cadastro_usuario, text="Cadastrar", command=self.cadastrar_usuario).grid(row=3, column=0, columnspan=2, pady=10)

    def cadastrar_usuario(self):
        nome = self.nome_usuario_entry.get()
        usuario = self.usuario_novo_entry.get()
        senha = self.senha_nova_entry.get()
        cadastrar_usuario(nome, usuario, senha)
        messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")

    def tela_clientes(self):
        tk.Label(self.tab_clientes, text="Nome Completo:").grid(row=0, column=0, padx=10, pady=10)
        self.nome_cliente_entry = tk.Entry(self.tab_clientes)
        self.nome_cliente_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(self.tab_clientes, text="Email:").grid(row=1, column=0, padx=10, pady=10)
        self.email_cliente_entry = tk.Entry(self.tab_clientes)
        self.email_cliente_entry.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(self.tab_clientes, text="Telefone:").grid(row=2, column=0, padx=10, pady=10)
        self.telefone_cliente_entry = tk.Entry(self.tab_clientes)
        self.telefone_cliente_entry.grid(row=2, column=1, padx=10, pady=10)
        
        tk.Button(self.tab_clientes, text="Cadastrar Cliente", command=self.cadastrar_cliente).grid(row=3, column=0, columnspan=2, pady=10)

    def cadastrar_cliente(self):
        nome = self.nome_cliente_entry.get()
        email = self.email_cliente_entry.get()
        telefone = self.telefone_cliente_entry.get()
        cadastrar_cliente(nome, email, telefone)
        messagebox.showinfo("Cadastro", "Cliente cadastrado com sucesso!")

    def tela_produtos(self):
        tk.Label(self.tab_produtos, text="Nome do Produto:").grid(row=0, column=0, padx=10, pady=10)
        self.nome_produto_entry = tk.Entry(self.tab_produtos)
        self.nome_produto_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(self.tab_produtos, text="Descrição:").grid(row=1, column=0, padx=10, pady=10)
        self.descricao_produto_entry = tk.Entry(self.tab_produtos)
        self.descricao_produto_entry.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(self.tab_produtos, text="Preço:").grid(row=2, column=0, padx=10, pady=10)
        self.preco_produto_entry = tk.Entry(self.tab_produtos)
        self.preco_produto_entry.grid(row=2, column=1, padx=10, pady=10)
        
        tk.Label(self.tab_produtos, text="Código de Barras:").grid(row=3, column=0, padx=10, pady=10)
        self.codigo_barras_entry = tk.Entry(self.tab_produtos)
        self.codigo_barras_entry.grid(row=3, column=1, padx=10, pady=10)
        
        tk.Button(self.tab_produtos, text="Cadastrar Produto", command=self.cadastrar_produto).grid(row=4, column=0, columnspan=2, pady=10)

    def cadastrar_produto(self):
        try:
            nome = self.nome_produto_entry.get()
            descricao = self.descricao_produto_entry.get()
            preco = float(self.preco_produto_entry.get())
            codigo_barras = self.codigo_barras_entry.get()
            estoque = 10

            if not nome or not descricao or not preco or not codigo_barras:
                messagebox.showerror("Erro", "Preencha todos os campos.")
                return

            produtos = listar_produtos()
            for produto in produtos:
                if produto["codigo_barras"] == codigo_barras:
                    messagebox.showerror("Erro", "Este código de barras já está em uso. Tente outro.")
                    return

            cadastrar_produto_bd(nome, descricao, preco, "Eletrônicos", codigo_barras, estoque)
            messagebox.showinfo("Cadastro", "Produto cadastrado com sucesso!")

            self.nome_produto_entry.delete(0, tk.END)
            self.descricao_produto_entry.delete(0, tk.END)
            self.preco_produto_entry.delete(0, tk.END)
            self.codigo_barras_entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um valor numérico válido para o preço.")
        except mysql.connector.errors.IntegrityError as e:
            if "Duplicate entry" in str(e):
                messagebox.showerror("Erro", "Erro de duplicidade: o código de barras já existe.")
            else:
                messagebox.showerror("Erro", f"Erro de integridade no banco de dados: {e}")
        except mysql.connector.errors.DatabaseError as e:
            if "Lock wait timeout exceeded" in str(e):
                messagebox.showerror("Erro", "Timeout de transação excedido. Tente novamente.")
            else:
                messagebox.showerror("Erro", f"Erro no banco de dados: {e}")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao cadastrar o produto: {e}")

    def tela_vendas(self):
        tk.Label(self.tab_vendas, text="ID do Produto:").grid(row=0, column=0, padx=10, pady=10)
        self.produto_id_entry = tk.Entry(self.tab_vendas)
        self.produto_id_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(self.tab_vendas, text="Quantidade:").grid(row=1, column=0, padx=10, pady=10)
        self.quantidade_entry = tk.Entry(self.tab_vendas)
        self.quantidade_entry.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Button(self.tab_vendas, text="Realizar Venda", command=self.realizar_venda).grid(row=2, column=0, columnspan=2, pady=10)

    def realizar_venda(self):
        try:
            produto_id = int(self.produto_id_entry.get())
            quantidade = int(self.quantidade_entry.get())
            
            # Verifica se o produto existe e obtém o preço
            conexao = conectar_banco_completo()
            cursor = conexao.cursor(dictionary=True)
            cursor.execute("SELECT preco FROM produtos WHERE id = %s", (produto_id,))
            produto = cursor.fetchone()
            conexao.close()

            if not produto:
                messagebox.showerror("Erro", "Produto não encontrado. Verifique o ID do produto.")
                return

            # Calcula o valor total da venda
            preco = produto["preco"]
            valor_total = preco * quantidade

            # Realiza a venda se o produto for encontrado
            realizar_venda_bd(produto_id, quantidade, valor_total)
            messagebox.showinfo("Venda", f"Venda realizada com sucesso! Valor total: R${valor_total:.2f}")

        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
        except mysql.connector.Error as e:
            messagebox.showerror("Erro no banco de dados", f"Ocorreu um erro ao registrar a venda: {e}")

    def tela_relatorios(self):
        tk.Button(self.tab_relatorios, text="Gerar Relatório de Vendas", command=self.gerar_relatorio).pack(pady=10)

    def gerar_relatorio(self):
        """Função para gerar e exibir o relatório de vendas"""
        vendas = gerar_relatorio_vendas()
        
        if not vendas:
            messagebox.showinfo("Relatório de Vendas", "Nenhuma venda registrada.")
            return
        
        relatorio_texto = "Relatório de Vendas\n\n"
        relatorio_texto += f"{'ID Venda':<10}{'ID Produto':<12}{'Quantidade':<12}{'Valor Total':<12}\n"
        relatorio_texto += "-" * 50 + "\n"
        
        for venda in vendas:
            relatorio_texto += f"{venda['id']:<10}{venda['produto_id']:<12}{venda['quantidade']:<12}{venda['valor_total']:<12.2f}\n"

        relatorio_janela = tk.Toplevel(self.root)
        relatorio_janela.title("Relatório de Vendas")
        relatorio_janela.geometry("400x300")

        texto = tk.Text(relatorio_janela, wrap="word")
        texto.insert("1.0", relatorio_texto)
        texto.config(state="disabled")
        texto.pack(expand=True, fill="both")

        botao_fechar = tk.Button(relatorio_janela, text="Fechar", command=relatorio_janela.destroy)
        botao_fechar.pack(pady=10)

# Inicialização do sistema
if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaVendas(root)
    root.mainloop()
