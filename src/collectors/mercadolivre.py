import requests
from bs4 import BeautifulSoup
import sqlite3
import os
import datetime

# 1. Configuração do caminho do Banco de Dados (Mesma lógica do setup)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB_PATH = os.path.join(BASE_DIR, 'data', 'vero.db')

# 2. Cabeçalhos (Para enganar o site e parecer um navegador Chrome comum)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def salvar_no_banco(produto, preco, url):
    """Conecta no banco e salva o preço encontrado"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO precos (produto, preco, loja, url)
        VALUES (?, ?, ?, ?)
    ''', (produto, preco, "Mercado Livre", url))

    conn.commit()
    conn.close()
    print(f"💾 SALVO NO DB: {produto[:30]}... | R$ {preco}")

def buscar_preco(url):
    print(f"🕵️‍♂️ Acessando: {url}")

    try:
        response = requests.get(url, headers=HEADERS)

        # Se o site bloquear (Erro 403 ou 503), avisa
        if response.status_code != 200:
            print(f"❌ Erro {response.status_code}: O site bloqueou o acesso.")
            return

        soup = BeautifulSoup(response.content, 'html.parser')

        # --- SELETORES (Aqui é onde a mágica acontece) ---
        # Tenta pegar o Título (H1)
        titulo_element = soup.find('h1', class_='ui-pdp-title')
        if not titulo_element:
            print("⚠️ Erro: Não achei o título. O HTML do site pode ter mudado.")
            return
        titulo = titulo_element.text.strip()

        # Tenta pegar o Preço
        # O ML usa essa classe 'andes-money-amount__fraction' para os números grandes do preço
        preco_element = soup.find('span', class_='andes-money-amount__fraction')
        if not preco_element:
            print("⚠️ Erro: Não achei o preço.")
            return

        # Limpeza do preço (Ex: converte "1.500" texto para 1500.0 float)
        preco_texto = preco_element.text.replace('.', '').replace(',', '.')
        preco_float = float(preco_texto)

        print(f"✅ SUCESSO: R$ {preco_float} - {titulo}")

        # Salva no final
        salvar_no_banco(titulo, preco_float, url)

    except Exception as e:
        print(f"💥 Erro inesperado: {e}")

if __name__ == "__main__":
    # URL DE TESTE (Um produto qualquer do ML)
    # Você pode trocar por qualquer link do Mercado Livre depois
    url_teste = "https://www.mercadolivre.com.br/cadeira-de-escritorio-secretaria-giratoria-altura-ajustavel-cor-preto/p/MLB26008367?pdp_filters=item_id%3AMLB4001353994&from=gshop&matt_tool=29425971&matt_internal_campaign_id=&matt_word=&matt_source=google&matt_campaign_id=22090354064&matt_ad_group_id=173090531436&matt_match_type=&matt_network=g&matt_device=c&matt_creative=727882727271&matt_keyword=&matt_ad_position=&matt_ad_type=pla&matt_merchant_id=735125422&matt_product_id=MLB26008367-product&matt_product_partition_id=2388009794866&matt_target_id=pla-2388009794866&cq_src=google_ads&cq_cmp=22090354064&cq_net=g&cq_plt=gp&cq_med=pla&gad_campaignid=22090354064#shipping"

    buscar_preco(url_teste)
