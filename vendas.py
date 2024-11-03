# Importa a função de conexão com o banco de dados
from database import conectar_banco_completo

# Função para registrar uma nova venda
def realizar_venda(produto_id, quantidade, valor_total):
    conexao = conectar_banco_completo()
    cursor = conexao.cursor()
    
    # Consulta SQL para registrar a venda
    query = "INSERT INTO vendas (produto_id, quantidade, valor_total) VALUES (%s, %s, %s)"
    cursor.execute(query, (produto_id, quantidade, valor_total))
    conexao.commit()
    conexao.close()

# Função para listar todas as vendas
def listar_vendas():
    conexao = conectar_banco_completo()
    cursor = conexao.cursor(dictionary=True)
    query = "SELECT * FROM vendas"
    cursor.execute(query)
    vendas = cursor.fetchall()
    conexao.close()
    return vendas
