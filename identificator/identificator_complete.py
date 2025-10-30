import pandas as pd
import numpy as np
import zipfile
import os
import glob
from typing import List, Set

# Configurações de Validação

FILE_PATH = "Desktop/Planilhas-Identiticator-Error/spreadsheet_example.xlsx"
ARTIFACT_FOLDER = os.environ.get("ARTIFACT_FOLDER", "./ocr-vm") 

EXPECTED_COLUMNS = [
    "Empresa", "Data", "Data Inicio", "Data Fim", "Campanha", 
    "Categoria do Produto", "Produto", "Preço", "App", "Cidade", "Estado"
]

VALID_SUPERMARKETS = {
    "Assai Atacadista", "Atacadão", "Cometa Supermercados", "Frangolândia", 
    "Atakarejo", "GBarbosa", "Novo Atacarejo", "Assaí Atacadista", 
    "Novo-Atacarejo", "Frangolandia", "Cometa-Supermercados", "Gbarbosa"
}

VALID_CIDADES = {
    "Recife", "São Luís", "Fortaleza", "Vitória da Conquista", "Belém", 
    "João Pessoa", "Teresina", "Aracaju", "Macéio"
}

VALID_ESTADOS = {
    "PERNAMBUCO", "MARANHÃO", "CEARÁ", "BAHIA", "PARÁ", 
    "PARAÍBA", "PIAUÍ", "SERGIPE", "ALAGOAS"
}


def unzip_folders(folder_path: str):

    print(f"Procurando arquivos .zip em: {folder_path}")
    
    search_pattern = os.path.join(folder_path, "**", "*.zip")
    
    zip_files = glob.glob(search_pattern, recursive=True)
    
    if not zip_files:
        print("Nenhum arquivo .zip encontrado.")
        return

    for zip_path in zip_files:
        try:
            extract_directory = os.path.dirname(zip_path)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_directory)
                print(f"Descompactado: {zip_path} em {extract_directory}")
        except zipfile.BadZipFile:
            print(f"Erro: O arquivo {zip_path} não é um .zip válido ou está corrompido.")
        except Exception as e:
            print(f"Erro ao descompactar {zip_path}: {e}")

def validate_spreadsheet(df: pd.DataFrame) -> bool:

    print("\n--- Iniciando Validação da Planilha ---")
    is_valid = True

    print("Verificando colunas...")
    missing_cols = [col for col in EXPECTED_COLUMNS if col not in df.columns]
    if missing_cols:
        print(f"ERRO: Colunas obrigatórias faltando: {missing_cols}")
        is_valid = False
    else:
        print("OK: Todas as colunas esperadas estão presentes.")

    print("Verificando células vazias (NaN)...")
    nan_counts = df.isnull().sum()
    cols_with_nan = nan_counts[nan_counts > 0]
    if not cols_with_nan.empty:
        print(f"AVISO: Encontradas células vazias nas seguintes colunas:\n{cols_with_nan}")
    else:
        print("OK: Nenhuma célula vazia encontrada.")

    print("Verificando linhas duplicadas...")
    duplicate_rows = df.duplicated().sum()
    if duplicate_rows > 0:
        print(f"ERRO: Encontradas {duplicate_rows} linhas duplicadas.")
        is_valid = False
    else:
        print("OK: Nenhuma linha duplicada.")

    print("Validando valores nas colunas...")
    
    if "Empresa" in df.columns:
        invalid_supermarkets = df[~df['Empresa'].isin(VALID_SUPERMARKETS)]['Empresa'].unique()
        if len(invalid_supermarkets) > 0:
            print(f"ERRO: Encontrados nomes de 'Empresa' inválidos: {list(invalid_supermarkets)}")
            is_valid = False
        else:
            print("OK: Coluna 'Empresa' validada.")

    if "Cidade" in df.columns:
        invalid_cidades = df[~df['Cidade'].isin(VALID_CIDADES)]['Cidade'].unique()
        if len(invalid_cidades) > 0:
            print(f"ERRO: Encontrados nomes de 'Cidade' inválidos: {list(invalid_cidades)}")
            is_valid = False
        else:
            print("OK: Coluna 'Cidade' validada.")
            
    print("Validando formatos de data...")
    if "Data Inicio" in df.columns:
        try:
            pd.to_datetime(df['Data Inicio'], format='%d/%m/%Y', errors='raise')
            print("OK: Formato 'Data Inicio' validado.")
        except ValueError as e:
            print(f"ERRO: Coluna 'Data Inicio' contém formatos de data inválidos. {e}")
            is_valid = False

    print("---------------------------------------\n")
    return is_valid



def main():
    try:
        print(f"Lendo arquivo: {FILE_PATH}")
        df = pd.read_excel(FILE_PATH)
        
        df.dropna(how='all', axis=0, inplace=True) # Linhas
        df.dropna(how='all', axis=1, inplace=True) # Colunas

        print(f"Arquivo lido. Encontradas {len(df)} linhas e {len(df.columns)} colunas.")

    except FileNotFoundError:
        print(f"ERRO: Arquivo não encontrado no caminho: {FILE_PATH}")
        return
    except Exception as e:
        print(f"ERRO ao ler o arquivo Excel: {e}")
        return

    if validate_spreadsheet(df):
        print("Resultado: SUCESSO! A planilha passou em todas as validações.")
    else:
        print("Resultado: FALHA! A planilha contém erros.")

if __name__ == "__main__":
    main()

