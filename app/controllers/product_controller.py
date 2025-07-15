# app/controllers/product_controller.py

from utils.db import conectar

def cadastrar_produto(nome, quantidade, minimo):
    conn = conectar()
    cursor = conn.cursor()
    try:
        query = "INSERT INTO products (nome, quantidade, quantidade_minima) VALUES (%s, %s, %s)"
        cursor.execute(query, (nome, quantidade, minimo))
        conn.commit()
        sucesso = True
    except Exception as e:
        print(f"Erro ao cadastrar produto: {e}")
        sucesso = False
    finally:
        cursor.close()
        conn.close()
    return sucesso


def listar_produtos():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM products")
    produtos = cursor.fetchall()

    cursor.close()
    conn.close()
    return produtos


def atualizar_produto(produto_id, nome, quantidade, quantidade_minima):
    from utils.db import conectar
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        try:
            cursor.execute(
                "UPDATE products SET nome=%s, quantidade=%s, quantidade_minima=%s WHERE id=%s",
                (nome, quantidade, quantidade_minima, produto_id)
            )
            conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao atualizar produto: {e}")
            return False
        finally:
            cursor.close()
            conexao.close()
    return False

def deletar_produto(produto_id):
    conn = conectar()
    cursor = conn.cursor()
    try:
        query = "DELETE FROM products WHERE id = %s"
        cursor.execute(query, (produto_id,))
        conn.commit()
        sucesso = True
    except Exception as e:
        print(f"Erro ao deletar produto: {e}")
        sucesso = False
    finally:
        cursor.close()
        conn.close()
    return sucesso
