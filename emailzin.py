import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from flask import Flask, jsonify, request

def enviar_email(mail, nome, image_path):  
    msg = MIMEMultipart('related')
    msg['Subject'] = "Assunto"
    msg['From'] = 'gugaben903@gmail.com'
    msg['To'] = mail
    password = 'syyw nsxw fztu ywhe' 

    # Corpo do e-mail em HTML com referência à imagem embutida
    corpo_email = f"""
    <html>
    <body>
        <p>Olá {nome}</p>
        <p>Seu email é {mail}</p>
        <p>Veja a imagem abaixo:</p>
        <img src="cid:image1">
    </body>
    </html>
    """

    msg.attach(MIMEText(corpo_email, 'html'))

    # Adiciona a imagem embutida
    if image_path:
        with open(image_path, 'rb') as img:
            mime = MIMEBase('image', 'png', filename='image.png')
            mime.add_header('Content-Disposition', 'inline', filename='image.png')
            mime.add_header('Content-ID', '<image1>')
            mime.add_header('X-Attachment-Id', 'image1')
            mime.set_payload(img.read())
            encoders.encode_base64(mime)
            msg.attach(mime)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
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
