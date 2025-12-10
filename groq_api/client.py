from groq import Groq
from groq_api.config import Config


def get_car_ai_bio(model, brand):
    client = Groq(api_key=Config.GROQ_API_KEY)
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Você é um grande vendedor de carros Hot Wheels para o mercado brasileiro. Sua ÚNICA tarefa é gerar o texto de venda solicitado pelo usuário, SEM NENHUMA introdução, explicação, raciocínio ou título (como 'Bio').",
            },
            {
                "role": "user",
                "content": f"Escreva uma bio curta, focada em venda, para o carro hot wheels {brand} {model}, com no máximo 250 caracteres. Destaque as principais características e detalhes interessantes.",
            }
        ],
        model="groq/compound",
        max_tokens=1000
    )
    return response.choices[0].message.content
