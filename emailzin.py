import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, jsonify, request

def enviar_email(mail, nome, tipo_proposta):
    # texto e HTML
    msg = MIMEMultipart('alternative')
    
    # 1. Configurações Básicas do E-mail
    msg['From'] = 'Cultura Inglesa <comercialculturainglesacg@gmail.com>'
    msg['To'] = mail
    password = 'cjin nkol lbfo ybgp'  # senha de aplicativo do Gmail
    
    # 2. Lógica para escolher o Texto
    tipo = tipo_proposta.lower()
    
    if tipo == "crianca" or tipo == "adulto":
        msg['Subject'] = "Sua Proposta de Investimento Cultura Inglesa 🎁"
        
        # Versão em texto simples atualizada com a nova proposta
        corpo_email_texto = f"""Olá, {nome}!
        
Segue abaixo a sua proposta:
Investimento 1º estágio – Contrato Semestral

Semestralidade com 30% OFF
6 parcelas iguais de R$ 389,90 (Boleto bancário)

Material didático com bônus de R$ 250,00
Por apenas R$ 589,90 no pix ou facilitado nos cartões de crédito em até 6 vezes sem juros.

Válido somente para a unidade Campina Grande-PB

Qualquer dúvida, estamos à disposição!"""

        # Pode visualizar a proposta por este link: 
        # https://api-email-bot-seven.vercel.app/mailing-06.png

        corpo_email_html = f"""
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>
        <body style="font-family: Arial, sans-serif; color: #333333; line-height: 1.6; margin: 0; padding: 20px;">
        
            <p>Olá, {nome}!</p>
            
            <p>Segue abaixo a sua proposta:</p>
            
            <h3 style="color: #003366;">Investimento 1º estágio – Contrato Semestral</h3>
            
            <p><strong>Semestralidade com 30% OFF</strong><br>
            6 parcelas iguais de R$ 389,90 (Boleto bancário)</p>
            
            <p><strong>Material didático com bônus de R$ 250,00</strong><br>
            Por apenas R$ 589,90 no pix ou facilitado nos cartões de crédito em até 6 vezes sem juros.</p>
            
            <p style="font-weight: bold; color: #cc0000;">Válido somente para a unidade Campina Grande-PB</p>
            
            <p>Qualquer dúvida, estamos à disposição!</p>
        
        </body>
        </html>
        """
        
    else:
        msg['Subject'] = "Informações sobre os cursos"
        corpo_email_texto = f"Olá, {nome}! Em breve entraremos em contato com mais informações."
        corpo_email_html = f"<p>Olá, {nome}! Em breve entraremos em contato com mais informações.</p>"

    # 3. Anexa as duas versões ao e-mail
    msg.attach(MIMEText(corpo_email_texto, 'plain'))
    msg.attach(MIMEText(corpo_email_html, 'html'))

    # 4. Envio
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        remetente_limpo = msg['From'].split('<')[1][:-1]
        s.login(remetente_limpo, password)
        s.sendmail(remetente_limpo, msg['To'], msg.as_string())
        s.quit()
        print('Email enviado com sucesso!')
    except Exception as e:
        print(f"Erro no SMTP: {e}")
        raise e

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
