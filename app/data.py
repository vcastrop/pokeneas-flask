import random

POKENEAS = [
    {
        "id": 1,
        "nombre": "Leoncini",
        "altura": 1.6,
        "habilidad": "Amigo de lo ajeno",
        "imagen": "https://pokeneas-valenyjuank.s3.us-east-2.amazonaws.com/Leoncini.png",
        "frase_filosofica": "Las cosas no son del dueño, son de quien las necesita."
    },
    {
        "id": 2,
        "nombre": "Grillachu",
        "altura": 1.5,
        "habilidad": "Farra infinita",
        "imagen": "https://pokeneas-valenyjuank.s3.us-east-2.amazonaws.com/Grillachu.png",
        "frase_filosofica": "Sonríe, que la vida es un soplo."
    },
    {
        "id": 3,
        "nombre": "Mozita",
        "altura": 1.4,
        "habilidad": "Dañar hogares",
        "imagen": "https://pokeneas-valenyjuank.s3.us-east-2.amazonaws.com/Mozita.png",
        "frase_filosofica": "Cada quien cuida lo que le interesa y descuida lo que le estorba."
    },
    {
        "id": 4,
        "nombre": "Barbie",
        "altura": 0.6,
        "habilidad": "Recuperación rápida",
        "imagen": "https://pokeneas-valenyjuank.s3.us-east-2.amazonaws.com/Barbie.png",
        "frase_filosofica": "Tú puedes ser lo que quieras ser."
    },
    {
        "id": 5,
        "nombre": "Bancolombio",
        "altura": 1.0,
        "habilidad": "Cabello inmóvil",
        "imagen": "https://pokeneas-valenyjuank.s3.us-east-2.amazonaws.com/Bancolombio.png",
        "frase_filosofica": "¿Quieres ser tu propio jefe?"
    },
    {
        "id": 6,
        "nombre": "Dineroviejo",
        "altura": 1.2,
        "habilidad": "Evadir impuestos",
        "imagen": "https://pokeneas-valenyjuank.s3.us-east-2.amazonaws.com/Dineroviejo.png",
        "frase_filosofica": "El que es pobre, es pobre porque quiere."
    },
    {
        "id": 7,
        "nombre": "Alternito",
        "altura": 0.9,
        "habilidad": "Diseñar interactivamente",
        "imagen": "https://pokeneas-valenyjuank.s3.us-east-2.amazonaws.com/Alternito.png",
        "frase_filosofica": "Hay personas que se odian, porque un día se quisieron."
    },
    {
        "id": 8,
        "nombre": "Undergolio",
        "altura": 1.8,
        "habilidad": "Ser original",
        "imagen": "https://pokeneas-valenyjuank.s3.us-east-2.amazonaws.com/Undergolio.png",
        "frase_filosofica": "Si no es oversized, ahí no es."
    }
]

def get_random_pokenea():
    return random.choice(POKENEAS)
