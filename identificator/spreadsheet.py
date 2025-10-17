import pandas as pd
import numpy as py
from openpyxl import Workbook

df = pd.read_excel = ["Desktop/Planilhas-Identiticator-Error/spreadsheet_example.xlsx"]

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
column_datainicio = df['Column2'] = ['B1']
column_datafim = df['Column3'] = ['C1']
column_campanha = df['Colum4'] = ['D1']
column_categoriaproduto = df['Column5'] = ['E1']
column_produto = df['Column6'] = ['F1']
column_preço = df['Column7'] = ['G1']
column_app = df['Column8'] = ['H1']
column_cidade = df['Column9'] = ['I1']
column_estado = df['Column10'] = ['J1']

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

duplicate()  

#Cleaning Data with the same data on spreadsheet
def cleaning_data():
    #Check if the column Supermarket is defined and have any value
    column_supermarket = []
    for i, supermarket in enumerate(column_supermarket):
        if supermarket == 0:
            print("Supermarket is not find")
            df.append([i])
    
    #Check if the columns data is defined by Default Configuration
    

cleaning_data()