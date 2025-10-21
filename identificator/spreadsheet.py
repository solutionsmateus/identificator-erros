import pandas as pd
import numpy as py
from openpyxl import Workbook
import zipfile
import os
import glob

df = pd.read_excel = ["Desktop/Planilhas-Identiticator-Error/spreadsheet_example.xlsx"]
artifact_folder = os.environ.get("ARTIFACT_FOLDER", "./ocr-vm") 

#Default configuration of all Columns and Rows.
supermarkets = {
    "Assai Atacadista",
    "Atacadão",
    "Cometa Supermercados",
    "Frangolândia",
    "Atakarejo",
    "GBarbosa",
    "Novo Atacarejo"
}

campanhas = df['Rows'] = ['A2' * 'J2'] * ['A10500' * 'J100500']

column_supermarket = df['Column1'] = ['A1']
column_data = df['Column2'] = ['B1']
column_datainicio = df['Column3'] = ['C1']
column_datafim = df['Column4'] = ['D1']
column_campanha = df['Colum5'] = ['E1']
column_categoriaproduto = df['Column6'] = ['F1']
column_produto = df['Column7'] = ['G1']
column_preço = df['Column8'] = ['H1']
column_app = df['Column9'] = ['I1']
column_cidade = df['Column10'] = ['I1']
column_estado = df['Column11'] = ['K1']

#Unzip all folders of Downloaded Artifacts

def unzip_folders():
    search_pattern = os.path.join(artifact_folder, "**", "*.*")
    file_paths = [f for f in glob.glob(search_pattern, recursive=True) if os.path.isfile(f)]
    zip_path = glob.glob(file_paths, recursive=True)
    
    for zip_path in file_paths:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            extract_directory = os.path.join(os.path.dirname (zip_path))
            zip_ref.extractall(file_paths)
            print(f"Encontrando as pastas {zip_path}, to {extract_directory}")

#Check if the Columns is on Defalut Configuration           
def syscheck():
    for i in df:
        with open('spreadsheet_example.xlsx', 'r'):
            if column_supermarket != column_supermarket:
                print("Column supermarket is different of Deffault")
            if column_data != column_data:
                print("Column Data is different of Defalut")
            if column_datainicio != column_datainicio:
                print("Column Data Inicio is different of Default")
            if column_datafim != column_datafim:
                print("Column Data Fim is different of Default")
            if column_campanha != column_campanha:
                print("Column Campanha is different of Default")
            if column_categoriaproduto != column_categoriaproduto:
                print("Column Categoria-Produto is different of Default")
            if column_produto != column_produto:
                print("Column Produto is different of Default")
            if column_preço != column_preço:
                print("Column Preço is different of Default")
            if column_app != column_app:
                print("Columm App is different of Defalut")
            if column_cidade != column_cidade:
                print("Column Cidade is different of Default")   
            if column_estado != column_estado:
                print("Column Estado is different of Default") 
    else:
        print("All columns are Error, Please Review your Spreadsheet Again")
            

#Duplicates and erros in spreadsheet
def duplicate():    
    column_data = df["Empresa", "Data Inicio", "Data Fim", "Campanha", "Categoria do Produto", "Produto", "Preço", "App", "Cidade", "Estado"]
    
    if ['column1' * "column2", "column3", "column4", "column5", "column6", "column7", "column8", "column9", "column10"].isnull():
        print("Colums is not defined")
        df.append(column_data)
    
    if column_data == 0:
        print("Criando a organização para colunas.")
        df.append[["New Column"]] = ["Empresa"] * ["Data Inicio"] * ["Data Fim"] * ["Campanha"] * ["Categoria do Produto"] * ["Preço"] * ["App"] * ["Cidade"] * ["Estado"]
        
    if column_data == df[pd.read_table]:
        print("Cleaning all table")
        df.clear()
        df.append(column_data)
    
    if column_data == column_data:
        print("Colunas na planilha estão corretas.")    

try:
    duplicate()
    syscheck()
    unzip_folders()
except:
    print("Not possible to process all functions")