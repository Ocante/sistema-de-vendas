# Importando o conector MySQL para Python
import mysql.connector

# Função para conectar ao banco de dados com tratamento de erro
def conectar_banco_completo():
    try:
        # Conecta ao banco com parâmetros seguros
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
