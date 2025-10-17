import os
import google.generativeai as genai
from google.generativeai import GenerativeModel
from dotenv import load_dotenv


env = load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

try:
    model = genai.GenerativeModel(model_name="gemini-flash-latest")
    prompt = {
        "Right Above, these files have extension of .pdf, .img, imeg, .png. With these files idenfity if there is same, if is yes, drop off and tell me which these is same and give me option of download with .zip extesion of all files that is not the same, if is not, continue to do process without cut any files."
    }
    
    print("Sending prompt to the Gemini API")
    response = model.generate_content(prompt)
    
    print(response.text)
except:
    print("Is not executable")

