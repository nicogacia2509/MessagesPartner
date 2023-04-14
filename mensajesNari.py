"""
I developed this project to help my girlfriend by sending motivational messages every hour. You can use it for your partner as well :)

"""


import random
import time
import requests
import json

# SendGrid API key
sendgrid_api_key = 'privatesnedgridapikey'

# List of motivacional messages 
mensajes_motivacionales = [
    'No te rindas, todo esfuerzo tiene su recompensa.',
    'El éxito no es la clave de la felicidad. La felicidad es la clave del éxito.',
    'Sólo se vive una vez, pero si lo haces bien, una vez es suficiente.',
    'No tengas miedo de renunciar a lo bueno para perseguir lo grandioso.',
    'La felicidad no es algo hecho. Viene de tus propias acciones.',
    'Si puedes soñarlo, puedes lograrlo.',
    'No esperes oportunidades, créalas.',
    'No te preocupes por los fracasos, preocúpate por las oportunidades que pierdes al no intentarlo.',
    'El éxito es la suma de pequeños esfuerzos repetidos día tras día.',
    'Nunca es tarde para ser lo que podrías haber sido.'
]

# Function to randomnly send messages using Sendgrid API through email
def enviar_mensaje():
    mensaje = random.choice(mensajes_motivacionales)
    destino = 'receiverEmail'
    asunto = 'Mensaje motivacional del día'
    cuerpo = f'Hola,\n\n{mensaje}\n\nSaludos,\npara recordarte que tu puedes'
    
    data = {
      "personalizations": [
        {
          "to": [
            {
              "email": destino
            }
          ],
          "subject": asunto
        }
      ],
      "from": {
        "email": "Sender email"
      },
      "content": [
        {
          "type": "text/plain",
          "value": cuerpo
        }
      ]
    }
    
    headers = {
      'Authorization': f'Bearer {sendgrid_api_key}',
      'Content-Type': 'application/json'
    }

    response = requests.post('https://api.sendgrid.com/v3/mail/send', data=json.dumps(data), headers=headers)
    print(response.status_code)

# Send message every hour 
for i in range(10):
    enviar_mensaje()
    time.sleep(3600) 