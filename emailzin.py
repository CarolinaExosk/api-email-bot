import smtplib
import email.message
from flask import Flask, jsonify,request
def enviar_email(mail, nome):  
    
    corpo_email = f"""
    <p> ola {nome}</p>
    <p>seu email eh {mail}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'gugaben903@gmail.com'
    msg['To'] = f'{mail}'
    password = 'syyw nsxw fztu ywhe' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

app = Flask(__name__)

@app.route('/')
def home():
    return "Olá, Mundo!"

@app.route('/endpoint1', methods=['GET'])
def endpoint1():
    # Substitua com a sua lógica
    return jsonify({"mensagem": "Você bateu no endpoint1jsvd!"})


@app.route('/sentmail', methods=['POST'])
def sentmail():
    data = request.json
    email = data.get('email')
    nome = data.get('nome')
    enviar_email(mail=email,nome=nome)
    # Agora você pode usar as variáveis email e nome na sua lógica
    return jsonify({"mensagem": "Você bateu no endpoint2!"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5001)


    
    
