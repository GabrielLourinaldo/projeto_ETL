import pandas as pd
import os
import sqlite3 # Biblioteca nativa do Python para banco de dados local
import extract
import transform

def load_to_csv(df: pd.DataFrame, file_name: str = 'Fifa_Processado.csv'):
    """
    Salva o DataFrame limpo em um arquivo CSV na pasta data/processed/
    """
    try:
        # 1. Definindo o caminho de destino
        caminho_atual = os.path.dirname(os.path.abspath(__file__))
        pasta_destino = os.path.join(caminho_atual, '..', 'data', 'processed')
        
        # 2. Garantindo que a pasta processed exista (Boa prática)
        os.makedirs(pasta_destino, exist_ok=True)
        
        # 3. Montando o caminho completo do novo arquivo
        caminho_arquivo = os.path.join(pasta_destino, file_name)
        
        # 4. O método mágico do Pandas para salvar em CSV
        # index=False evita que o Pandas crie uma coluna inútil com os números das linhas (0, 1, 2...)
        df.to_csv(caminho_arquivo, index=False)
        print(f"[CSV] Dados salvos com sucesso em: {caminho_arquivo}")
        return True
        
    except Exception as e:
        print(f"[CSV] ERRO ao salvar o arquivo: {e}")
        return False

def load_to_database(df: pd.DataFrame, db_name: str = 'moura_dados.db', table_name: str = 'jogadores'):
    """
    Salva o DataFrame limpo em um Banco de Dados SQLite na pasta data/processed/
    """
    try:
        # 1. Definindo o caminho do banco de dados
        caminho_atual = os.path.dirname(os.path.abspath(__file__))
        pasta_destino = os.path.join(caminho_atual, '..', 'data', 'processed')
        caminho_banco = os.path.join(pasta_destino, db_name)
        
        # 2. Criando a conexão com o banco de dados (Se não existir, o SQLite cria na hora)
        conexao = sqlite3.connect(caminho_banco)
        
        # 3. O método mágico do Pandas para salvar direto no SQL!
        # if_exists='replace' significa: se a tabela já existir, apague e crie de novo com os dados novos.
        # if_exists='append' (adicionaria as linhas sem apagar as velhas)
        df.to_sql(name=table_name, con=conexao, if_exists='replace', index=False)
        
        print(f"[SQL] Dados salvos com sucesso na tabela '{table_name}' do banco '{db_name}'")
        return True
        
    except Exception as e:
        print(f"[SQL] ERRO ao salvar no banco de dados: {e}")
        return False
    finally:
        # Boa prática: SEMPRE feche a conexão com o banco de dados, independentemente de erro ou sucesso
        if 'conexao' in locals():
            conexao.close()

if __name__ == "__main__":
    # Vamos orquestrar tudo para testar!
    print("Iniciando teste do Módulo LOAD...\n")
    
    # --- Passo 1: Extrair (Usando o que já fizemos) ---
    caminho_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_origem = os.path.join(caminho_atual, '..', 'data', 'raw', 'Fifa.csv')
    dados_sujos = extract.extract_fifa_data(caminho_origem)
    
    if dados_sujos is not None:
        # --- Passo 2: Transformar ---
        dados_limpos = transform.clean_fifa_data(dados_sujos)
        
        # --- Passo 3: Carregar (Load) ---
        print("\n--- Iniciando o Load (Carga) ---")
        load_to_csv(dados_limpos)
        load_to_database(dados_limpos)