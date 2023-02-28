import openai

#Carregue sua chave de API de uma variável de ambiente ou serviço de gerenciamento secreto
openai.api_key = "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" #YOUR_API_KEY
model_engine="text-davinci-003"
prompt= "Fazer uma API de consumo de CEP"

response= openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=2048,
    n=3,
    stop=['---'],
    temperature=0.9,
)

for result in response.choices:
    print(result.text)

