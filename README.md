# Pipeline ETL com Python

Este projeto implementa um pipeline ETL (Extract, Transform, Load) local utilizando Python e Pandas. O objetivo é ler dados brutos de um arquivo CSV, aplicar regras de higienização e de negócio, e carregar os dados processados em um banco de dados relacional.

## Tecnologias Utilizadas
- Python 3
- Pandas e NumPy
- SQLite e SQLAlchemy

## Estrutura do Pipeline
- src/extract.py: Responsável pela leitura e validação dos dados brutos.
- src/transform.py: Realiza a limpeza de nulos, aplicação de regras condicionais e filtros vetoriais.
- src/load.py: Exporta o dataset processado para um arquivo CSV e persiste os dados em um banco SQLite.

## Como Executar

1. Clone este repositório.
2. Crie e ative um ambiente virtual:
   python -m venv venv
3. Instale as dependências:
   pip install -r requirements.txt
4. Execute o arquivo principal para rodar o fluxo completo:
   python src/load.py