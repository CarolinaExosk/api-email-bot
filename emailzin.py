import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from flask import Flask, jsonify, request

def enviar_email(mail, nome, image_path):
    msg = MIMEMultipart('related')
    # Define the subject based on the image_path
    if image_path.lower() == "crianca1" or image_path.lower() == "crianca2":
        msg['Subject'] = "O maior presente🎁 que você pode dar ao seu filho."
        
    elif "promo" in image_path.lower():
        msg['Subject'] = "Oferta relâmpago!⚡️"
        
    else:
        msg['Subject'] = "O maior presente🎁 que você pode se dar."
    msg['From'] = 'Cultura Inglesa <comercialculturainglesacg@gmail.com>'
    msg['To'] = mail
    password = 'cjin nkol lbfo ybgp'

    # Corpo do e-mail em HTML com apenas a imagem
    if image_path.lower() == "crianca1" or image_path.lower() == "crianca2" or image_path.lower() == "adulto":
        corpo_email = """
        <html>
        <body>
            <img src="cid:image1" alt="Imagem" style="width:100%; max-width:600px;">
        </body>
        </html>
        """
        msg.attach(MIMEText(corpo_email, 'html'))

        # Map for image paths based on 'image_path' argument
        image_files = {
            "crianca1": "crianca1.jpeg",
            "crianca2": "crianca2.jpeg",
            "adulto": "adulto.jpeg"
            
        }

        # Attach the image inline if 'image_path' exists in the dictionary
        if image_path in image_files:
            with open(image_files[image_path], 'rb') as img:
                mime = MIMEBase('image', 'jpeg', filename=image_files[image_path])
                mime.add_header('Content-Disposition', 'inline', filename=image_files[image_path])
                mime.add_header('Content-ID', '<image1>')
                mime.add_header('X-Attachment-Id', 'image1')
                mime.set_payload(img.read())
                encoders.encode_base64(mime)
                msg.attach(mime)
    else:
        if image_path.lower()=="promo49":
            corpo_email="""
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
                            color: #ff0000; /* Adjust color if needed */
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
            corpo_email="""
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
                            color: #ff0000; /* Adjust color if needed */
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
            
        elif image_path=="promo14plus":
            corpo_email="""
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
                            color: #000000; /* Adjust color if needed */
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
        msg.attach(MIMEText(corpo_email, 'html'))
            
    # Sending email
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
