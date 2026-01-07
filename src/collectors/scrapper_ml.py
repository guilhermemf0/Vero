import requests
from bs4 import BeautifulSoup
import sqlite3
import os
from datetime import datetime

# Configuração do Banco de Dados
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'vero.db')

# Headers são obrigatórios para fingir que somos um navegador e não um robô
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def salvar_no_banco(produto, preco, loja, url):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO precos (produto, preco, loja, url)
        VALUES (?, ?, ?, ?)
    ''', (produto, preco, loja, url))
    conn.commit()
    conn.close()
    print(f"💾 Guardado no DB: {produto} | R$ {preco}")

def buscar_preco_mercadolivre(url):
    print(f"🔍 A analisar: {url}")

    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print("❌ Erro ao aceder à página. O site pode ter bloqueado o bot.")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    try:
        # Tenta pegar o título
        # DICA: No Chrome, clica com botão direito no titulo -> Inspecionar para ver a classe
        titulo = soup.find('h1', class_='ui-pdp-title').text.strip()

        # Tenta pegar o preço (a classe muda, tens de inspecionar o site se der erro)
        # Esta classe 'andes-money-amount__fraction' é comum no ML, mas pode variar
        preco_texto = soup.find('span', class_='andes-money-amount__fraction').text.strip()

        # Tratamento do preço (remove pontos e converte para float)
        preco_formatado = float(preco_texto.replace('.', '').replace(',', '.'))

        print(f"✅ Encontrado: {titulo} -> R$ {preco_formatado}")

        # Salvar
        salvar_no_banco(titulo, preco_formatado, "Mercado Livre", url)

    except AttributeError:
        print("⚠️ Erro: Não foi possível encontrar o elemento HTML. A estrutura do site pode ter mudado.")
    except Exception as e:
        print(f"Erro genérico: {e}")

if __name__ == "__main__":
    # Teste com um produto (Troca este link por um produto real se quiseres)
    link_produto = "https://www.mercadolivre.com.br/placa-de-video-nvidia-msi-ventus-geforce-rtx-40-series-rtx-4060-geforce-rtx-4060-ventus-2x-white-8g-oc-8gb/p/MLB27986341"
    buscar_preco_mercadolivre(link_produto)
