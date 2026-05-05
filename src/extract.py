import pandas as pd
import os

def extract_fifa_data(file_path: str) -> pd.DataFrame: # >> Outro Type Hint. Isso indica que a função vai retornar (devolver) um objeto do tipo DataFrame do Pandas.
    """
    Lê o arquivo CSV bruto e retorna um DataFrame do Pandas.
    """
    print(f"Iniciando a extração do arquivo: {file_path}")
    
    try:
        # pd.read_csv é a mágica do Pandas que transforma o arquivo em uma tabela na memória
        df = pd.read_csv(file_path)
        print("Extração concluída com sucesso!")
        print(f"O dataset tem {df.shape[0]} linhas e {df.shape[1]} colunas.")
        return df
    
    except FileNotFoundError:
        print(f"ERRO: O arquivo não foi encontrado no caminho: {file_path}")
        print("Verifique se o nome do arquivo está correto na pasta data/raw/")
        return None
    except Exception as e:
        print(f"ERRO INESPERADO durante a leitura: {e}")
        return None

# Este bloco protege o código. Ele só executa se rodarmos este arquivo diretamente.
if __name__ == "__main__":
    
    # 1. Mapeando o caminho correto do arquivo
    # Como o script está dentro da pasta 'src', precisamos voltar uma pasta ('..') 
    # para depois entrar em 'data/raw'
    caminho_atual = os.path.dirname(os.path.abspath(__file__))
    print(caminho_atual)
    caminho_arquivo = os.path.join(caminho_atual, '..', 'data', 'raw', 'Fifa.csv')
    print("---------------")
    print(caminho_arquivo)
    
    # 2. Executando a função de extração
    dados_brutos = extract_fifa_data(caminho_arquivo)
    
    # 3. Se a leitura funcionou, exibimos as 5 primeiras linhas para conferir
    if dados_brutos is not None:
        print("\n--- Espiando os dados ---")
        print(dados_brutos.head())