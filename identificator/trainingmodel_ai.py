import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Erro: A variável de ambiente GEMINI_API_KEY não foi definida.")
    exit()

genai.configure(api_key=api_key)


path_df_default = "Desktop/Planilhas-Identiticator-Error/default_spreadsheet.xlsx"
path_df_analise = "Desktop/Planilhas-Identificator-Error/Analise da Concorrencia (Encartes).xlsx"

try:
    print("Fazendo upload dos arquivos para a API...")

    file_default = genai.upload_file(path=path_df_default, display_name="Default Spreadsheet")
    file_analise = genai.upload_file(path=path_df_analise, display_name="Spreadsheet for Analysis")

    print(f"Upload completo: {file_default.name}, {file_analise.name}")


    model = genai.GenerativeModel(model_name="gemini-flash-latest")

    prompt_parts = [
        file_default,
        file_analise,
        "Analise as duas planilhas enviadas ('Default Spreadsheet' e 'Spreadsheet for Analysis').",
        "Verifique se a 'Spreadsheet for Analysis' é compatível com a 'Default Spreadsheet' nos seguintes campos: supermercado, data, Data Inicio, Data Fim, Categoria dos Produtos, Campanha, Produto, Preço, App, Cidade e Estado.",
        "\nSiga estas regras para a 'Spreadsheet for Analysis':",
        "1. Não pode ter espaçamento desnecessário antes ou depois dos dados nas células.",
        "2. Não pode conter linhas ou colunas inteiras vazias desnecessariamente.",
        "3. Verifique se há dados duplicados em linhas inteiras.",
        "4. Verifique se os dados em colunas (como 'Cidade' ou 'Estado') são consistentes com os valores esperados (definidos pela planilha default).",
        "\nInstruções:",
        "Percorra cada linha e coluna e verifique se os dados são compatíveis com a 'Default Spreadsheet'.",
        "Se tudo estiver OK, responda: 'A planilha está formatada corretamente e é compatível.'",
        "Se houver erros, identifique-os claramente, liste os problemas encontrados (ex: 'Erro na Linha 5, Coluna C: Data 'XX' fora do formato') e sugira a solução."
    ]

    print("Enviando prompt para a API Gemini...")
    response = model.generate_content(prompt_parts)
    
    print("\n--- Resposta da API ---")
    print(response.text)
    print("-----------------------\n")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
    print("Verifique se os caminhos dos arquivos estão corretos e se a API Key é válida.")