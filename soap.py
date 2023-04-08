from suds.client import Client

# pede ao usuário para informar o primeiro número
numero1 = int(input("Informe o primeiro número: "))

# pede ao usuário para informar o segundo número
numero2 = int(input("Informe o segundo número: "))

# cria um objeto cliente SOAP apontando para a URL do serviço
url = 'http://www.dneonline.com/calculator.asmx?WSDL'
client = Client(url)

# chama o método 'Add' do serviço passando dois números como parâmetros
result = client.service.Add(numero1, numero2)

# exibe o resultado da soma
print("O resultado da soma é:", result)

# descreve request
print("------Request-------")
print(client.last_sent().str())
print("--------------------")

# descreve response
print("------Response------")
print(client.last_received().str())
print("--------------------")
