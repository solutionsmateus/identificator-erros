import os
import glob
from google import genai
import google.generativeai as genai
from google.generativeai import GenerativeModel
from dotenv import load_dotenv


env = load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

df_default = ["Desktop/Planilhas-Identiticator-Error/default_spreadsheet.xlsx"]
df = ["Desktop/Planilhas-Identificator-Error/Analise da Concorrencia (Encartes).xlsx"]


try:
    model = genai.GenerativeModel(model_name="gemini-flash-latest")

    arquivo_df = df
    arquivo_df_default = df_default

    prompt = { 
        (df), (df_default),
        "Analise as planilhas upadas e verifique se há compatibilidade nos campos: supermercado, data, Data Inicio, Data Fim, Categoria dos Produtos, Campanha, Produto, Preço, App, Cidade e Estado) e seguindo estas seguintes regras: 1 - Não pode ter espaçamento entre as colunas e linhas. 2 - Não pode conter nenhum dado em todas as colunas e linhas. 3 - Não pode conter dados iguais entre as colunas ou linhas. 4 - Não pode conter dados diferentes em diferentes colunas ou linhas. Percorra por cada linha e coluna e verifique os dados se dão compatibilidade com a Default SpreadSheet (Default Spreadsheet for Analysis). Se tudo tiver ok e ocorrer bem, disponibilize o download da planilha. Se não identifique o erro e faça um prompt para você mesmo indicando os erros e a solução."
    }
    
    print("Sending prompt to the Gemini API")
    response = model.generate_content(prompt)
    
    print(response.text)
except:
    print("Is not executable")