import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from flask import Flask, jsonify, request

def enviar_email(mail, nome, image_path):  
    msg = MIMEMultipart('related')
    msg['Subject'] = "Uma oferta especial para você investir no seu inglês."
    msg['From'] = 'Cultura Inglesa <comercialculturainglesacg@gmail.com>'
    msg['To'] = mail
    password = 'cjin nkol lbfo ybgp'

    # Corpo do e-mail em HTML com referência à imagem embutida
    if image_path == "crianca":
        corpo_email = f"""
        <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #000000;">
            <div>
                <p>A <strong style="color: #c30e0e;">CULTURA INGLESA</strong> é referência no ensino de qualidade desde 1934. Há 90 anos com cursos próprios, desenvolvidos pelo nosso departamento acadêmico da Faculdade Cultura Inglesa, com conteúdos constantemente atualizados, aulas dinâmicas e interativas, que transformam a sala de aula em um espaço de intercâmbio cultural.</p>
                
                <p>Pensando nisso, a <strong >Cultura Inglesa</strong> preparou um <u><strong style="color: #000000;"><u>kit de oportunidades</u></strong></u> para você:</p>
        
                <ul style="list-style-type: none; padding-left: 0; color: #000000;">
                    <li><strong style="color:#ff1f1f;">>> Taxa de matrícula:</strong> GRÁTIS.</li>
                    <li><strong style="color:#ff1f1f;">>> 30% de desconto na semestralidade:</strong> 6 parcelas de R$ 279,90 nos cartões de crédito sem juros.</li>
                    <li><strong style="color:#ff1f1f;">>> 250,00 reais de bônus no material didático:</strong> R$ 519,00 à vista.</li>
                </ul>
        
                <p><strong style="color: #c30e0e;">Diferenciais que você só encontra aqui:</strong></p>
                <ul style="list-style-type: none; padding-left: 0; color: #000000;">
                    <li> >> <strong> Professores altamente qualificados</strong>e especialistas em aulas para jovens e adultos;</li>
                    <li> >> <strong> Material didático internacional</strong> das melhores editoras do mundo;</li>
                    <li> >> <strong> Infraestrutura</strong> com <strong> tecnologia de ponta</strong> (Quadros interativos, inteligência artificial e muito mais);</li>
                    <li> >> <strong> Dupla certificação:</strong>  Diploma brasileiro gratuito (Cultura Inglesa) ao final do curso e Certificação Internacional (Cambridge English Exams) opcional mediante pagamento de taxa de inscrição.</li>
                </ul>
        
                <p style="font-size: 1.2em;"><strong style="color: #c30e0e;">Oferta válida somente até sábado ou enquanto durarem as vagas. Exclusivo na unidade Campina Grande-PB.</strong></p>
            </div>
        </body>
        </html>
        """

    else:
        corpo_email = f"""
        <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #000000;">
            <div>
                <p>A <strong style="color: #c30e0e;">CULTURA INGLESA</strong> é referência no ensino de qualidade desde 1934. Há 90 anos com cursos próprios, desenvolvidos pelo nosso departamento acadêmico da Faculdade Cultura Inglesa, com conteúdos constantemente atualizados, aulas dinâmicas e interativas, que transformam a sala de aula em um espaço de intercâmbio cultural.</p>
                
                <p>Pensando nisso, a <strong style="color: #c30e0e;">Cultura Inglesa</strong> preparou um <u><strong style="color: #000000;"><u>kit de oportunidades</u></strong></u> para você:</p>
        
                <ul style="list-style-type: none; padding-left: 0; color: #000000;">
                    <li><strong style="color:#ff1f1f;">>> Taxa de matrícula:</strong> GRÁTIS.</li>
                    <li><strong style="color:#ff1f1f;">>> 30% de desconto na semestralidade:</strong> 6 parcelas de R$ 279,90 nos cartões de crédito sem juros.</li>
                    <li><strong style="color:#ff1f1f;">>> 250,00 reais de bônus no material didático:</strong> R$ 519,00 à vista.</li>
                </ul>
        
                <p><strong style="color: #c30e0e;">Diferenciais que você só encontra aqui:</strong></p>
                <ul style="list-style-type: none; padding-left: 0; color: #000000;">
                    <li> >> Professores altamente qualificados e especialistas em aulas para jovens e adultos;</li>
                    <li> >> Material didático internacional das melhores editoras do mundo;</li>
                    <li> >> Infraestrutura com tecnologia de ponta (Quadros interativos, inteligência artificial e muito mais);</li>
                    <li> >> Dupla certificação: Diploma brasileiro gratuito (Cultura Inglesa) ao final do curso e Certificação Internacional (Cambridge English Exams) opcional mediante pagamento de taxa de inscrição.</li>
                </ul>
        
                <p style="font-size: 1.2em;"><strong style="color: #c30e0e;">Oferta válida somente até sábado ou enquanto durarem as vagas. Exclusivo na unidade Campina Grande-PB.</strong></p>
            </div>
        </body>
        </html>
        """

    msg.attach(MIMEText(corpo_email, 'html'))

    # Adiciona a imagem embutida, se houver
    # if image_path:
    #     with open(image_path, 'rb') as img:
    #         # mime = MIMEBase('image', 'jpeg', filename='turbo.jpeg')
    #         # mime.add_header('Content-Disposition', 'inline', filename='turbo.jpeg')
    #         # mime.add_header('Content-ID', '<image1>')
    #         # mime.add_header('X-Attachment-Id', 'image1')
    #         mime.set_payload(img.read())
    #         encoders.encode_base64(mime)
    #         msg.attach(mime)

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
