# utils/db.py

import mysql.connector
from mysql.connector import Error
import config

def conectar():
    try:
        conexao = mysql.connector.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME,
            port=config.DB_PORT
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def criar_tabelas():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            username VARCHAR(50) NOT NULL UNIQUE,
            senha VARCHAR(255) NOT NULL,
            perfil ENUM('admin', 'comum') NOT NULL
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            quantidade INT NOT NULL,
            quantidade_minima INT NOT NULL
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS movements (
            id INT AUTO_INCREMENT PRIMARY KEY,
            produto_id INT NOT NULL,
            tipo ENUM('entrada', 'saida') NOT NULL,
            quantidade INT NOT NULL,
            data_movimento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (produto_id) REFERENCES products(id)
        );
        """)

        conexao.commit()
        cursor.close()
        conexao.close()
