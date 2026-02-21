import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, jsonify, request

def enviar_email(mail, nome, tipo_proposta):
    msg = MIMEMultipart('alternative')
    
    # 1. Configurações Básicas do E-mail
    msg['From'] = 'Cultura Inglesa <comercialculturainglesacg@gmail.com>'
    msg['To'] = mail
    password = 'cjin nkol lbfo ybgp'  # senha de aplicativo do Gmail
    
    # 2. Lógica para escolher o Texto
    tipo = tipo_proposta.lower()
    
    if tipo == "crianca" or tipo == "adulto":
        # Texto padrão de investimento
        msg['Subject'] = "Sua Proposta de Investimento 🎁"
        
        corpo_email_html = f"""
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                h3 {{ color: #003366; }}
                .destaque {{ font-weight: bold; color: #cc0000; }}
            </style>
        </head>
        <body>
            <p>Olá, {nome}!</p>
            <p>Segue abaixo a sua proposta:</p>
            
            <h3>Investimento 1º estágio – Contrato Semestral</h3>
            
            <p><strong>Semestralidade</strong><br>
            6 parcelas iguais de R$ 459,84 (Boleto bancário)</p>
            
            <p><strong>Material didático</strong><br>
            6 parcelas iguais de R$ 106,66 nos cartões de crédito</p>
            
            <p class="destaque">Válido somente para a unidade Campina Grande-PB</p>
            
            <p>Qualquer dúvida, estamos à disposição!</p>
        </body>
        </html>
        """
        
    else:
        # Se mandar algo diferente de crianca ou adulto
        msg['Subject'] = "Informações sobre os cursos"
        corpo_email_html = f"<p>Olá, {nome}! Em breve entraremos em contato com mais informações.</p>"

    # 3. Anexa o texto HTML ao e-mail
    msg.attach(MIMEText(corpo_email_html, 'html'))

    # 4. Envio
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(msg['From'].split('<')[1][:-1], password)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()
    print('Email enviado com sucesso!')

# --- Configuração do Servidor Flask ---

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor de E-mail da Cultura Inglesa Online!"

@app.route('/sentmail', methods=['POST'])
def sentmail():
    data = request.json
    email = data.get('email')
    nome = data.get('nome')
    tipo_proposta = data.get('image_path', 'default') 
    
    try:
        enviar_email(mail=email, nome=nome, tipo_proposta=tipo_proposta)
        return jsonify({"status": "sucesso", "mensagem": "E-mail enviado!"}), 200
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
        return jsonify({"status": "erro", "mensagem": "Falha no envio."}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
