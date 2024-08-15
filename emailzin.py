import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from flask import Flask, jsonify, request

def enviar_email(mail, nome, image_path):  
    msg = MIMEMultipart('related')
    msg['Subject'] = "Temos uma oferta por tempo limitado."
    msg['From'] = 'Cultura Inglesa <comercialculturainglesacg@gmail.com>'
    msg['To'] = mail
    password = 'cjin nkol lbfo ybgp'

    # Corpo do e-mail em HTML com referência à imagem embutida
    if image_path == "crianca":
        corpo_email = f"""
           <html>
           <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #000000;">
               <div>
                   <p>O melhor presente que você pode dar a sua criança é a oportunidade de aprender inglês desde cedo.</p>
                   <p>Pensando nisso, a <strong>Cultura Inglesa</strong> preparou um <u><strong>kit de oportunidades</strong></u> para vocês:</p>
                   
                   <h3 style="color: #c00000;"><u>INVESTIMENTO 1º ESTÁGIO</u></h3>
                   
                   <ul style="list-style-type: none; padding-left: 0; color: #000000;">
                       <li><strong> >> Taxa de matrícula:</strong> GRÁTIS.</li>
                       <li><strong> >> 🚀 6 parcelas de <span style="color: #c00000;">R$ 269,90</span> (semestralidade)</strong></li>
                       <li><strong> >> 📚 6 parcelas de <span style="color: #c00000;">R$ 90,98</span> (material didático)</strong></li>
                   </ul>
                   
                   <p>Pagamento total do 1º estágio em espécie ou facilitado em até 6 vezes nos cartões de crédito sem juros.</p>
                   
                   <p>Garanta agora o futuro brilhante de sua criança!</p>
                   
                   <p style="font-size: 1.2em;"><strong>Faça a matrícula já! 🌟🚀</strong></p>
                   
                   <p style="font-size: 1.2em;"><strong>Oferta válida somente até sábado ou enquanto durar as vagas. Exclusivo na unidade Campina Grande-PB.</strong></p>
               </div>
           </body>
           </html>
            """
        else:
         corpo_email = """
                     <html>
             <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #000000;">
                 <div>
                     <p>O <strong style="color: #c00000">CULTURA EXPRESS</strong> é um curso de inglês desenhado de forma a aproveitar o melhor das várias abordagens do ensino de línguas para jovens e adultos, e tem como objetivo que você aprenda de forma rápida e prazerosa.</p>
                     <p>Ele leva em consideração a forma de pensar do aluno e também as etapas necessárias na aula, para que você fale com confiança sobre as diversas situações do dia a dia.</p>
                     <p>Toda aula, há um trabalho de intensa prática oral e há um momento também em que os alunos param para ver se estão realmente aprendendo. Depois disso, eles interagem entre si, simulando situações da vida real, de uma forma bastante personalizada e divertida.</p>
                     <p>Pensando nisso, a <strong>Cultura Inglesa</strong> preparou um <u><strong>kit de oportunidades</strong></u> para vocês:</p>
                     
                     <h3 style="color: #c00000;"><u>INVESTIMENTO 1º ESTÁGIO</u></h3>
                     
                     <ul style="list-style-type: none; padding-left: 0; color: #000000;">
                         <li><strong> >> Taxa de matrícula:</strong> GRÁTIS.</li>
                         <li><strong> >> 🚀 6 parcelas de <span style="color: #c00000;">R$ 269,90</span> (semestralidade)</strong></li>
                         <li><strong> >> 📚 6 parcelas de <span style="color: #c00000;">R$ 90,98</span> (material didático)</strong></li>
                     </ul>
                     
                     <p>Pagamento total do 1º estágio em espécie ou facilitado em até 6 vezes nos cartões de crédito sem juros.</p>
                     
                     <p>Garanta agora o futuro brilhante de sua criança!</p>
                     
                     <p style="font-size: 1.2em;"><strong>Faça a matrícula já! 🌟🚀</strong></p>
                     
                     <p style="font-size: 1.2em; color: red;"><strong><u>Oferta válida somente até sábado ou enquanto durar as vagas. Exclusivo na unidade Campina Grande-PB.</u></strong></p>
                 </div>
             </body>
             </html>
             """

    msg.attach(MIMEText(corpo_email, 'html'))

    # Adiciona a imagem embutida, se houver
    # if image_path:
    #     with open(image_path, 'rb') as img:
    #         mime = MIMEBase('image', 'jpeg', filename='turbo.jpeg')
    #         mime.add_header('Content-Disposition', 'inline', filename='turbo.jpeg')
    #         mime.add_header('Content-ID', '<image1>')
    #         mime.add_header('X-Attachment-Id', 'image1')
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
