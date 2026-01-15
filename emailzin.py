import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from flask import Flask, jsonify, request

def enviar_email(mail, nome, image_path):
    msg = MIMEMultipart('related')
    
    # Define o assunto baseado no image_path
    if image_path.lower() == "crianca":
        msg['Subject'] = "Um presente para toda a vida 🎁"
    elif image_path.lower() == "adulto":
        msg['Subject'] = "O maior presente🎁 que você pode se dar."
    elif "promo" in image_path.lower():
        msg['Subject'] = "Oferta relâmpago!⚡️"
    else:
        msg['Subject'] = "Um presente para toda a vida🎁"
        
    msg['From'] = 'Cultura Inglesa <comercialculturainglesacg@gmail.com>'
    msg['To'] = mail
    password = 'cjin nkol lbfo ybgp'  # substitua pela sua senha de aplicativo/conta

    # Se for "crianca" ou "adulto", enviará apenas a imagem correspondente
    if image_path.lower() == "crianca" or image_path.lower() == "adulto":
        corpo_email = """
        <html>
        <body>
            <img src="cid:image1" alt="Imagem" style="width:100%; max-width:600px;">
        </body>
        </html>
        """
        msg.attach(MIMEText(corpo_email, 'html'))

        # Escolhe o arquivo certo com base na string
        image_files = {
            "crianca": "crianca.png",
            "adulto": "adulto.png"
        }

        if image_path.lower() in image_files:
            with open(image_files[image_path.lower()], 'rb') as img:
                mime = MIMEBase('image', 'png', filename=image_files[image_path.lower()])
                mime.add_header('Content-Disposition', 'inline', filename=image_files[image_path.lower()])
                mime.add_header('Content-ID', '<image1>')
                mime.add_header('X-Attachment-Id', 'image1')
                mime.set_payload(img.read())
                encoders.encode_base64(mime)
                msg.attach(mime)
    
    # Se for "promo...", aqui segue o mesmo fluxo de ofertas em HTML:
    else:
        if image_path.lower()=="promo49":
            corpo_email = """
                <!DOCTYPE html>
                <html lang="pt-BR">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Promoção de Matrícula</title>
                    <style>
                        body {
                            font-family: Arial, sans-serif;
                            line-height: 1.6;
                        }
                        .highlight {
                            font-weight: bold;
                            color: #ff0000;
                        }
                        .emphasis {
                            font-style: italic;
                        }
                        .limited-offer {
                            font-weight: bold;
                            color: #000;
                            font-size: 1.2em;
                        }
                    </style>
                </head>
                <body>
                    <ul>
                        <li>☑️ Taxa de matrícula <span class="highlight emphasis">GRÁTIS</span>;</li>
                        <li>☑️ R$ <span class="highlight">790,00</span> de <span class="highlight emphasis">desconto</span> na <span class="highlight emphasis">semestralidade</span>;</li>
                        <li>☑️ R$ <span class="highlight">100,00</span> de <span class="highlight emphasis">desconto</span> no <span class="highlight emphasis">material didático</span>.</li>
                    </ul>
                    <p class="limited-offer">*SOMENTE ATÉ AMANHÃ!!!* 🏃🏃</p>
                </body>
                </html>
            """
        elif image_path.lower()=="promo1013":
            corpo_email = """
                <!DOCTYPE html>
                <html lang="pt-BR">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Promoção de Matrícula</title>
                    <style>
                        body {
                            font-family: Arial, sans-serif;
                            line-height: 1.6;
                        }
                        .highlight {
                            font-weight: bold;
                            color: #ff0000;
                        }
                        .emphasis {
                            font-style: italic;
                        }
                        .limited-offer {
                            font-weight: bold;
                            color: #000;
                            font-size: 1.2em;
                        }
                    </style>
                </head>
                <body>
                    <ul>
                        <li>☑️ Taxa de matrícula <span class="highlight emphasis">GRÁTIS</span>;</li>
                        <li>☑️ R$ <span class="highlight">820,00</span> de <span class="highlight emphasis">desconto</span> na <span class="highlight emphasis">semestralidade</span>;</li>
                        <li>☑️ R$ <span class="highlight">240,00</span> de <span class="highlight emphasis">desconto</span> no <span class="highlight emphasis">material didático</span>.</li>
                    </ul>
                    <p class="limited-offer">*SOMENTE ATÉ AMANHÃ!!!* 🏃🏃</p>
                </body>
                </html>
            """
        elif image_path.lower()=="promo14plus":
            corpo_email = """
                <!DOCTYPE html>
                <html lang="pt-BR">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Promoção de Matrícula</title>
                    <style>
                        body {
                            font-family: Arial, sans-serif;
                            line-height: 1.6;
                        }
                        .highlight {
                            font-weight: bold;
                            color: #000000;
                        }
                        .emphasis {
                            font-style: italic;
                        }
                        .limited-offer {
                            font-weight: bold;
                            color: #000;
                            font-size: 1.2em;
                        }
                    </style>
                </head>
                <body>
                    <ul>
                        <li>☑️ Taxa de matrícula <span class="highlight emphasis">GRÁTIS</span>;</li>
                        <li>☑️ R$ <span class="highlight">890,00</span> de <span class="highlight emphasis">desconto</span> na <span class="highlight emphasis">semestralidade</span>;</li>
                        <li>☑️ R$ <span class="highlight">220,00</span> de <span class="highlight emphasis">desconto</span> no <span class="highlight emphasis">material didático</span>.</li>
                    </ul>
                    <p class="limited-offer">*SOMENTE ATÉ AMANHÃ!!!* 🏃🏃</p>
                </body>
                </html>
            """
        else:
            # Caso não seja nenhum "promo", pode enviar uma mensagem genérica ou vazia
            corpo_email = "Não há conteúdo definido para este tipo de image_path."
        
        # Adiciona o corpo do email em HTML
        msg.attach(MIMEText(corpo_email, 'html'))
    
    # Envio do e-mail
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(msg['From'].split('<')[1][:-1], password)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()
    print('Email enviado')

app = Flask(__name__)

@app.route('/')
def home():
    return "Olá, Mundo!"

@app.route('/endpoint1', methods=['GET'])
def endpoint1():
    return jsonify({"mensagem": "Você bateu no endpoint1!"})

@app.route('/sentmail', methods=['POST'])
def sentmail():
    data = request.json
    email = data.get('email')
    nome = data.get('nome')
    image_path = data.get('image_path')  # Caminho da imagem fornecido na requisição
    enviar_email(mail=email, nome=nome, image_path=image_path)
    return jsonify({"mensagem": "Você bateu no endpoint2!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
