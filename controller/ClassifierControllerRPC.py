import pika
import json
from service.ClassifierService import extrair_texto_pdf, limpar_texto, classificar_documento

# Conectando ao RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declarando as filas (de requisição e resposta)
channel.queue_declare(queue='documentRequestQueue', durable=True)
channel.queue_declare(queue='documentResponseQueue', durable=True)

# Função que processa a mensagem recebida da fila
def process_document(ch, method, properties, body):
    try:
        print('Recebendo documento...')
        caminho_pdf = './temp.pdf'
        
        # Salvando os bytes como arquivo temporário
        with open(caminho_pdf, 'wb') as f:
            f.write(body)

        # Extraindo e processando o texto
        texto = extrair_texto_pdf(caminho_pdf)
        texto = limpar_texto(texto)
        tipo_documental = classificar_documento(texto)
        print('Documento classificado:', tipo_documental)


        # Criando a resposta
        response = json.dumps({'tipo_documental': tipo_documental})
        print('Enviando resposta:', response)

        # Enviando a resposta de volta na fila de resposta
        channel.basic_publish(exchange='',
                              routing_key= properties.reply_to,
                              body=response, properties=pika.BasicProperties(correlation_id=properties.correlation_id))
        print('Resposta enviada com sucesso!')

        # confirmando o processamento da mensagem
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print('Mensagem processada com sucesso!')

    except Exception as e:
        error_message = json.dumps({'error': str(e)})
        channel.basic_publish(exchange='',
                              routing_key=properties.reply_to,
                              body=error_message, properties=pika.BasicProperties(correlation_id=properties.correlation_id))
        ch.basic_ack(delivery_tag=method.delivery_tag)

# Consumindo mensagens da fila de requisição
channel.basic_consume(queue='documentRequestQueue', on_message_callback=process_document)

print('Aguardando requisições de documentos...')
channel.start_consuming()
