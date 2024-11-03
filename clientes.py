# Importa a função de conexão com o banco de dados
from database import conectar_banco_completo

# Função para cadastrar um novo cliente
def cadastrar_cliente(nome, email, telefone):
    conexao = conectar_banco_completo()
    cursor = conexao.cursor()
    
    # Consulta SQL para inserção de um novo cliente
    query = "INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)"
    cursor.execute(query, (nome, email, telefone))
    conexao.commit()
    conexao.close()
