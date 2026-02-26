import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, jsonify, request

def enviar_email(mail, nome, tipo_proposta):
    msg = MIMEMultipart('alternative')
    
    # 1. Config email
    msg['From'] = 'Cultura Inglesa <comercialculturainglesacg@gmail.com>'
    msg['To'] = mail
    password = 'cjin nkol lbfo ybgp'  # senha de aplicativo do Gmail
    
    # 2. Lógica para escolher o Texto
    tipo = tipo_proposta.lower()
    
    if tipo == "crianca" or tipo == "adulto":
        msg['Subject'] = "Sua Proposta de Investimento Cultura Inglesa 🎁"
        
        # HTML atualizado com a imagem hospedada no Vercel
        corpo_email_html = f"""
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>
        <body style="font-family: Arial, sans-serif; color: #333333; line-height: 1.6; margin: 0; padding: 20px;">
        
            <p>Olá, {nome}!</p>
            
            <p>Segue abaixo a sua proposta de investimento:</p>
            
            <div style="text-align: center; margin: 30px 0;">
                <img src="https://api-email-bot-seven.vercel.app/mailing-06.png" alt="Proposta de Investimento Cultura Inglesa" style="max-width: 100%; height: auto; display: block; margin: 0 auto; border-radius: 8px;">
            </div>
            
            <p>Qualquer dúvida, estamos à disposição!</p>
        
        </body>
        </html>
        """
        
    else:
        msg['Subject'] = "Informações sobre os cursos"
        corpo_email_html = f"<p>Olá, {nome}! Em breve entraremos em contato com mais informações.</p>"

    # 3. Anexa o texto HTML ao e-mail
    msg.attach(MIMEText(corpo_email_html, 'html'))

    # 4. Envio
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        # Extraindo o email limpo do remetente para o login
        remetente_limpo = msg['From'].split('<')[1][:-1]
        s.login(remetente_limpo, password)
        s.sendmail(remetente_limpo, msg['To'], msg.as_string())
        s.quit()
        print('Email enviado com sucesso!')
    except Exception as e:
        print(f"Erro no SMTP: {e}")
        raise e # Repassa o erro para o Flask capturar

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
