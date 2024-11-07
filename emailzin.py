import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from flask import Flask, jsonify, request

def enviar_email(mail, nome, image_path):
    msg = MIMEMultipart('related')
    msg['Subject'] = "O maior presente🎁 que você pode se dar."
    msg['From'] = 'Cultura Inglesa <comercialculturainglesacg@gmail.com>'
    msg['To'] = mail
    password = 'cjin nkol lbfo ybgp'

    # Corpo do e-mail em HTML com referência à imagem embutida
    corpo_email = f"""
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #000000;">
        <div>
            <p>A <strong style="color: #c30e0e;">CULTURA INGLESA</strong> é referência no ensino de qualidade desde 1934...</p>
            <!-- Rest of the HTML content -->
            <p style="font-size: 1.2em;"><strong style="color: #c30e0e;">Oferta válida somente até sábado ou enquanto durarem as vagas. Exclusivo na unidade Campina Grande-PB.</strong></p>
        </div>
    </body>
    </html>
    """
    msg.attach(MIMEText(corpo_email, 'html'))

    # Map for image paths based on 'image_path' argument
    image_files = {
        "crianca": "crianca.jpeg",
        "adulto": "adulto.jpeg"
    }

    # Attach the image if 'image_path' exists in the dictionary
    if image_path in image_files:
        with open(image_files[image_path], 'rb') as img:
            mime = MIMEBase('image', 'jpeg', filename=image_files[image_path])
            mime.add_header('Content-Disposition', 'inline', filename=image_files[image_path])
            mime.add_header('Content-ID', '<image1>')
            mime.add_header('X-Attachment-Id', 'image1')
            mime.set_payload(img.read())
            encoders.encode_base64(mime)
            msg.attach(mime)

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
