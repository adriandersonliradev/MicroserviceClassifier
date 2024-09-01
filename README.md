# MicroserviceClassifier


Este projeto é um microserviço para classificação automática de documentos usando aprendizado de máquina. O serviço permite o upload de arquivos PDF, extrai o texto usando OCR (se necessário), e classifica o documento em um tipo documental usando um modelo de aprendizado de máquina pré-treinado.

## Pré-requisitos

Certifique-se de ter o Python instalado no seu sistema (versão 3.6 ou superior). Para verificar se o Python está instalado e qual a versão, você pode executar o seguinte comando no terminal:

python --version

## Configuração do Ambiente
Clone o repositório do projeto:
git clone <URL_REPOSITORIO>

cd microservice_classifier

## Crie e ative um ambiente virtual:

### No Windows:

python -m venv venv
.\venv\Scripts\activate

No macOS/Linux:

python3 -m venv venv

source venv/bin/activate

## Instale todas as dependências do requirements.txt:

pip install -r requirements.txt

## Instalação do Tesseract OCR
Este projeto utiliza o Tesseract OCR para extrair texto de PDFs. Você precisa instalar o Tesseract no seu sistema operacional:

Windows: Baixe o instalador do site oficial do Tesseract e siga as instruções de instalação.

macOS: Instale o Tesseract via Homebrew:

brew install tesseract

# Executando o Projeto
Após a instalação das dependências e do Tesseract, você pode iniciar o servidor Flask:

### python -m controller.ClassifierController

O servidor irá iniciar em http://127.0.0.1:5000. Você pode usar o Postman ou qualquer outra ferramenta para fazer requisições à API.

## Como Usar a API

Endpoint /classificar
Método: POST
Descrição: Classifica o tipo documental de um arquivo PDF enviado.
Corpo da Requisição
A requisição deve ser do tipo multipart/form-data e incluir um arquivo PDF. A chave para o arquivo deve ser file.

# Exemplo de Requisição
Abra o Postman ou outra ferramenta de sua escolha.
Selecione o método POST.
Insira a URL: http://127.0.0.1:5000/classificar.
Vá para a aba Body.
Selecione form-data.
Adicione uma chave chamada file e defina o tipo como File.
Selecione o arquivo PDF que deseja classificar.
Clique em Send.
Exemplo de Resposta
A resposta será em formato JSON e conterá o tipo documental previsto ou uma mensagem de erro se algo deu errado.

## Exemplo de resposta bem-sucedida:

{
  "tipo_documental": "contrato"
}

Neste exemplo, "contrato" é o tipo documental previsto pelo modelo.

## Exemplo de resposta com erro:

json
Copiar código
{
  "error": "Nenhum arquivo enviado"
}
Este erro indica que o arquivo não foi incluído na requisição.

## Explicações de Respostas Possíveis
Resposta de Sucesso: 200

Campo: tipo_documental
Descrição: Indica o tipo documental previsto pelo modelo após processar o texto extraído do PDF. Por exemplo, pode retornar valores como "contrato", "fatura", "relatório", etc.
Respostas de Erro:

400 Bad Request: Retorna um JSON com uma chave "error" descrevendo o problema, como "Nenhum arquivo enviado" ou "Nenhum arquivo selecionado".
500 Internal Server Error: Retorna um JSON com uma chave "error" contendo a descrição do erro inesperado que ocorreu durante o processamento.

