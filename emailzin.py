import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from flask import Flask, jsonify, request

def enviar_email(mail, nome, image_path):  
    msg = MIMEMultipart('related')
    msg['Subject'] = "Investimento com retorno garantido."
    msg['From'] = 'Cultura Inglesa <comercialculturainglesacg@gmail.com>'
    msg['To'] = mail
    password = 'cjin nkol lbfo ybgp'

    # Corpo do e-mail em HTML com referência à imagem embutida
    if image_path == "crianca":
        corpo_email = f"""
            <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #052664;">
                <div style="">
                    <p>O melhor presente que você pode dar a sua criança é a oportunidade de aprender inglês desde cedo.</p>
                    <p>Pensando nisso, a <strong>Cultura Inglesa</strong> preparou um <u><strong>kit de oportunidades</strong></u> para vocês:</p>
                    
                    <ul style="list-style-type: none; padding-left: 0;">
                        <li><strong style="font-size: 1.2em; color: red;">Taxa de matrícula:</strong> GRÁTIS.</li>
                        <li><strong style="font-size: 1.2em; color: red;">20% de desconto na semestralidade:</strong> 6 parcelas de R$ 269,90</li>
                        <li><strong style="font-size: 1.2em; color: red;">250,00 reais de bônus no material didático:</strong> 6 parcelas de R$ 90,98</li>
                    </ul>
                    
                    <h3 style="color: #c00000">Diferenciais que você só encontra aqui:</h3>
                    
                    <ul style="list-style-type: none; padding-left: 0;">
                        <li><strong> >> Professores altamente qualificados</strong> e especialistas em aulas para crianças;</li>
                        <li><strong> >> Materiais didáticos internacionais</strong> das melhores editoras do mundo;</li>
                        <li><strong> >></strong> Infraestrutura com <strong>tecnologia de ponta;</strong></li>
                        <li><strong> >> Gameficação</strong> para incentivar atitudes positivas;</li>
                        <li><strong> >> Quadros interativos</strong> com uso de internet, games, vídeos e muito mais;</li>
                        <li><strong> >> Dupla certificação:</strong> Diploma brasileiro e Certificação Inglesa (<a href="https://culturainglesacg.com.br/certificacoes/" style="color: blue; text-decoration: underline;">Cambridge English Exams</a>);</li>
                        <li><strong> >> Experiências</strong> gastronômicas e de <em>maker</em>.</li>
                    </ul>
                    
                    <p>Garanta agora o futuro brilhante de sua criança!</p>
                    
                    <p style="font-size: 1.2em; color: #c00000;"><strong>Faça a matrícula já! 🌟🚀</strong></p>
                    
                    <p>Oferta válida somente até sábado ou enquanto durar as vagas. Exclusivo na unidade Campina Grande-PB.</p>
                </div>
            </body>
            </html>
            """
    else:
        corpo_email = """<html>
                <body style="font-family: Arial, sans-serif; line-height: 1.6;">
                    <div>
                        <p>O <strong>CULTURA EXPRESS</strong> é um curso de inglês desenhado de forma a aproveitar o melhor das várias abordagens do ensino de línguas para jovens e adultos, e tem como objetivo que você aprenda de forma rápida e prazerosa.</p>
                        <p>Ele leva em consideração a forma de pensar do aluno e também as etapas necessárias na aula, para que você fale com confiança sobre as diversas situações do dia a dia.</p>
                        <p>Toda aula, há um trabalho de intensa prática oral e há um momento também em que os alunos param para ver se estão realmente aprendendo. Depois disso, eles interagem entre si, simulando situações da vida real, de uma forma bastante personalizada e divertida.</p>
                        <p>Pensando nisso, a <strong>Cultura Inglesa</strong> preparou um <u><strong>kit de oportunidades</strong></u> para vocês:</p>
                        
                        <ul style="list-style-type: none; padding-left: 0;">
                            <li><strong style="font-size: 1.2em; color: red;">Taxa de matrícula:</strong> GRÁTIS.</li>
                            <li><strong style="font-size: 1.2em; color: red;">20% de desconto na semestralidade:</strong> 6 parcelas de R$ 298,90</li>
                            <li><strong style="font-size: 1.2em; color: red;">250,00 reais de bônus no material didático:</strong> 6 parcelas de R$ 90,98</li>
                        </ul>
                        
                        <h3 style="color: #c00000">Diferenciais que você só encontra aqui:</h3>
                        
                        <ul style="list-style-type: none; padding-left: 0;">
                            <li><strong> >> Professores altamente qualificados</strong> e especialistas em aulas para jovens e adultos;</li>
                            <br>
                            <li><strong> >> Materiais didáticos internacionais</strong> das melhores editoras do mundo;</li>
                            <br>
                            <li> <strong>>></strong> Infraestrutura com <strong>tecnologia de ponta;</strong></li>
                            <br>
                            <li><strong> >> Gameficação</strong> para incentivar atitudes positivas;</li>
                            <br>
                            <li><strong> >> Quadros interativos</strong> com uso de internet, vídeos, podcasts e muito mais;</li>
                            <br>
                            <li><strong> >> Dupla certificação:</strong> Diploma brasileiro e Certificação Inglesa (<a href="https://culturainglesacg.com.br/certificacoes/" style="color: blue; text-decoration: underline;">Cambridge English Exams</a>);</li>
                        </ul>
                        
                        <p style="color: #c00000"><strong>Faça a matrícula já! 🌟🚀</strong></p>
                        
                        <p style="font-size: 1.2em; color: #c00000;"><u>Oferta válida somente até sábado ou enquanto durar as vagas. Exclusivo na unidade Campina Grande-PB.</u></p>
                    </div>
                </body>
                </html>"""

    # corpo_email = f"""
    # <html>
    # <body>
    #     <img src="cid:image1">
    # </body>
    # </html>
    # """

    msg.attach(MIMEText(corpo_email, 'html'))

    # Adiciona a imagem embutida
    

    s = smtplib.SMTP('smtp.gmail.com: 587')
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
