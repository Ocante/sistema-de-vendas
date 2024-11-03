# Importa a função de conexão com o banco de dados
from database import conectar_banco_completo

# Função para realizar o login do usuário
def login_usuario(usuario, senha):
    conexao = conectar_banco_completo()
    cursor = conexao.cursor(dictionary=True)
    
    # Consulta SQL para verificar usuário e senha
    query = "SELECT * FROM usuarios WHERE usuario = %s AND senha = %s"
    cursor.execute(query, (usuario, senha))
    
    # Obtém o resultado da consulta
    resultado = cursor.fetchone()
    conexao.close()
    return resultado

# Função para cadastrar um novo usuário
def cadastrar_usuario(nome, usuario, senha, tipo="vendedor"):
    conexao = conectar_banco_completo()
    cursor = conexao.cursor()
    
    # Consulta SQL para inserção de novo usuário
    query = "INSERT INTO usuarios (nome, usuario, senha, tipo) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (nome, usuario, senha, tipo))
    conexao.commit()
    conexao.close()
