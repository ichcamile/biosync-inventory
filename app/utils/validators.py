# utils/validators.py

def validar_numero(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

def campo_vazio(valor):
    return not valor.strip()
