# Importa a função de conexão com o banco de dados
from database import conectar_banco_completo

# Função para gerar um relatório de vendas
def gerar_relatorio_vendas():
    conexao = conectar_banco_completo()
    cursor = conexao.cursor(dictionary=True)
    
    # Consulta SQL para obter todas as vendas
    query = "SELECT * FROM vendas"
    cursor.execute(query)
    vendas = cursor.fetchall()
    conexao.close()
    
    # Retorna o relatório das vendas
    return vendas
