import requests

# URL do endpoint que envia o e-mail
url = "http://localhost:5001/sentmail"

# Dados da requisição
data = {
    "email": "gustavoataide.trabalho@gmail.com",
    "nome": "gustavito",
    "image_path": "imagem_crianca.png"  # Atualize o caminho para a imagem correta
}

# Enviando a requisição POST
response = requests.post(url, json=data)

# Exibindo a resposta do servidor
print(response.status_code)
print(response.json())
