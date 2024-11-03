# Importa a função de conexão com o banco de dados
from database import conectar_banco_completo

# Função para cadastrar um novo produto
def cadastrar_produto(nome, descricao, preco, categoria, codigo_barras, estoque):
    conexao = conectar_banco_completo()
    cursor = conexao.cursor()
    
    # Consulta SQL para inserir um produto no sistema
    query = "INSERT INTO produtos (nome, descricao, preco, categoria, codigo_barras, estoque) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (nome, descricao, preco, categoria, codigo_barras, estoque))
    conexao.commit()
    conexao.close()

# Função para listar todos os produtos
def listar_produtos():
    conexao = conectar_banco_completo()
    cursor = conexao.cursor(dictionary=True)
    query = "SELECT * FROM produtos"
    cursor.execute(query)
    produtos = cursor.fetchall()
    conexao.close()
    return produtos
