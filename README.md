# 🛡️ Vero: Price Monitor & AI Advisor

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

*Do latim "Verus" (Verdadeiro).*
**Monitoramento de preços com inteligência real.**

[Reportar Bug](https://github.com/guilhermemf0/vero/issues) · [Solicitar Feature](https://github.com/guilhermemf0/vero/issues)

</div>

---

## 📖 Sobre o Projeto

O **Vero** nasceu de uma frustração comum: a manipulação de preços em grandes e-commerces (especialmente em épocas de Black Friday).

Diferente de rastreadores comuns que apenas mostram o gráfico de preços, o Vero atua como um **Consultor de Compras Pessoal**. Ele combina Web Scraping, Estatística e LLMs (Large Language Models) para responder a uma única pergunta: *"Este desconto é real ou é metade do dobro?"*

### ✨ Principais Funcionalidades (Planejadas)

* 🕵️ **Coleta Autônoma:** Monitoramento de preços 24/7 em grandes varejistas.
* 📊 **Análise Estatística:** Cálculo de média móvel e desvio padrão para identificar anomalias.
* 🧠 **IA Advisor:** Um "Boletim de Compra" gerado por IA que explica, em linguagem natural, se é hora de comprar.
* 🔔 **Alertas Inteligentes:** Notificações via Discord/Telegram apenas para ofertas reais (filtradas pela IA).
* 📈 **Dashboard Interativo:** Visualização de dados via Streamlit.

---

## 🛠️ Tech Stack

O projeto utiliza uma arquitetura moderna focada em dados:

| Área | Tecnologias |
| :--- | :--- |
| **Linguagem Base** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) |
| **Coleta de Dados** | `Requests` `BeautifulSoup4` `Selenium` |
| **Dados & Analytics** | `Pandas` `NumPy` `SQLite` |
| **Inteligência Artificial** | `OpenAI API (GPT)` `LangChain` |
| **Interface & Web** | `Streamlit` |
| **DevOps & Automação** | `Git` `n8n` |

---

## 🚀 Como Executar Localmente

### Pré-requisitos
* Python 3.10 ou superior
* Git

### Passo a Passo

1. **Clone o repositório**
   ```bash
   git clone [https://github.com/guilhermemf0/vero.git](https://github.com/guilhermemf0/vero.git)
   cd vero
