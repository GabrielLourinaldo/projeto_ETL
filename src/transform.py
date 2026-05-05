import pandas as pd
import extract

def clean_fifa_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Recebe o DataFrame sujo, aplica regras de negócio e retorna o DataFrame limpo.
    """
    print("\n--- Iniciando a Transformação dos Dados ---")
    
    # 1. Boa Prática: Fazer uma cópia do DataFrame original para não corromper o dado em memória
    df_clean = df.copy()
    
    # 2. Limpeza de Nulos: 
    # Em sistemas de RH/Vendas, um cadastro sem 'Team' ou 'Value Per M$' geralmente é lixo.
    # O dropna() exclui qualquer linha que tenha pelo menos uma coluna em branco (NaN).
    linhas_antes = df_clean.shape[0]
    df_clean = df_clean.dropna(subset=['Team', 'Value Per M$'])
    

    # 3. Regra de Negócio (Criando uma nova coluna condicional):
    # Vamos classificar o jogador. Se for maior ou igual a 30 anos, é 'Veterano', senão é 'Jovem'.
    # Isso treina a criação de flags e categorias, essencial para dashboards no Power BI.
    df_clean['Categoria_Idade'] = df_clean['Age'].apply(lambda idade: 'Veterano' if idade >= 30 else 'Jovem')
    
    # 4. Filtro Matemático (Limpando lixo numérico):
    # Não faz sentido um jogador custar 0 ou menos. Vamos manter apenas quem tem valor válido.
    # A sintaxe df[condição] funciona exatamente como a cláusula WHERE do banco de dados.
    df_clean = df_clean[df_clean['Value Per M$'] > 0.0]
    linhas_depois = df_clean.shape[0]
    print(f"Limpeza de Nulos: {linhas_antes - linhas_depois} linhas com dados vazios foram removidas.")
    print(f"Transformação concluída! O dataset agora tem {df_clean.shape[0]} linhas perfeitas.")
    return df_clean

if __name__ == "__main__":
    import os
    
    # Vamos reaproveitar o caminho e a função do extract.py
    caminho_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(caminho_atual, '..', 'data', 'raw', 'Fifa.csv')
    
    # 1. Extração (O 'E' do ETL)
    dados_sujos = extract.extract_fifa_data(caminho_arquivo)
    
    if dados_sujos is not None:
        # 2. Transformação (O 'T' do ETL)
        dados_limpos = clean_fifa_data(dados_sujos)
        
        # 3. Conferindo o resultado: Vamos exibir algumas colunas específicas para ver nossa nova coluna
        print("\n--- Resultado Final (Amostra) ---")
        colunas_para_exibir = ['Name', 'Age', 'Categoria_Idade', 'Team', 'Value Per M$']
        print(dados_limpos[colunas_para_exibir].head(7))