import sqlite3
import pandas as pd # Vamos usar o pandas da Pessoa B só pra visualizar bonitinho
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB_PATH = os.path.join(BASE_DIR, 'data', 'vero.db')

def ler_banco():
    conn = sqlite3.connect(DB_PATH)

    print("\n📊 --- DADOS NO BANCO ---")

    # Lê tudo da tabela 'precos'
    try:
        df = pd.read_sql_query("SELECT * FROM precos", conn)

        if df.empty:
            print("O banco está vazio!")
        else:
            print(df)
            print(f"\nTotal de registros: {len(df)}")

    except Exception as e:
        print(f"Erro ao ler banco: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    ler_banco()
