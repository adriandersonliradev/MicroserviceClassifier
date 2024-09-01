from flask import Flask, request, jsonify
from service.ClassifierService import extrair_texto_pdf, limpar_texto, classificar_documento
app = Flask(__name__)


@app.route('/classificar', methods=['POST'])
def classificar():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400
    
    arquivo = request.files['file']
    if arquivo.filename == '':
        return jsonify({'error': 'Nenhum arquivo selecionado'}), 400

    try:
        caminho_pdf = './temp.pdf'
        arquivo.save(caminho_pdf)
        texto = extrair_texto_pdf(caminho_pdf)
        texto = limpar_texto(texto)
        tipo_documental = classificar_documento(texto)
        return jsonify({'tipo_documental': tipo_documental}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
