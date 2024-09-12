import fitz  # PyMuPDF
import re
import pytesseract
from model.ClassifierModel import vectorizer, logistic_model
from PIL import Image

import os

system = os.name
if system == 'posix':
    url = r'/opt/homebrew/bin/tesseract'
else:
    url = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

pytesseract.pytesseract.tesseract_cmd = url

def extrair_texto_pdf(caminho_pdf):
    texto = ""
    with fitz.open(caminho_pdf) as doc:
        for pagina in doc:
            # Extrair texto digital
            texto_pagina = pagina.get_text()
            
            # Verificar se o texto digital é insuficiente ou inexistente
            if not texto_pagina.strip():
                # Converter a página em uma imagem
                imagem = pagina.get_pixmap()
                imagem_pil = Image.frombytes("RGB", [imagem.width, imagem.height], imagem.samples)
                
                # Aplicar OCR para extrair texto da imagem
                texto_pagina = pytesseract.image_to_string(imagem_pil)

            texto += texto_pagina
    
    return texto


def limpar_texto(texto):
    # Remover stop words e caracteres especiais
    texto = re.sub(r'\b\w{1,2}\b', '', texto)  # Remove palavras com 1 ou 2 caracteres
    texto = re.sub(r'[^\w\s]', '', texto)  # Remove caracteres especiais
    texto = texto.lower()  # Converter para minúsculas
    return texto

def classificar_documento(texto):
    texto_limpo = limpar_texto(texto)
    X_novo = vectorizer.transform([texto_limpo])
    tipo_documental_previsto = logistic_model.predict(X_novo)
    return tipo_documental_previsto[0]
