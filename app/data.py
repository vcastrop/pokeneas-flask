import random

POKENEAS = [
    {
        "id": 1,
        "nombre": "Leoncini",
        "altura": 1.6,
        "habilidad": "Amigo de lo ajeno",
        "imagen": "https://via.placeholder.com/200",
        "frase_filosofica": "Las cosas no son del dueño, son de quien las necesita."
    },
    {
        "id": 2,
        "nombre": "Grillachu",
        "altura": 1.5,
        "habilidad": "Sople infinito",
        "imagen": "https://via.placeholder.com/200",
        "frase_filosofica": "Sonríe, que la vida es un soplo."
    },
    {
        "id": 3,
        "nombre": "Mozita",
        "altura": 1.4,
        "habilidad": "Dañar hogares",
        "imagen": "https://via.placeholder.com/200",
        "frase_filosofica": "Cada quien cuida lo que le interesa y descuida lo que le estorba."
    },
    {
        "id": 4,
        "nombre": "Barbie",
        "altura": 0.6,
        "habilidad": "Recuperación rápida",
        "imagen": "https://via.placeholder.com/200",
        "frase_filosofica": "Tú puedes ser lo que quieras ser."
    },
    {
        "id": 5,
        "nombre": "Bancolombio",
        "altura": 1.0,
        "habilidad": "Cabello inmóvil",
        "imagen": "https://via.placeholder.com/200",
        "frase_filosofica": "¿Quieres ser tu propio jefe?"
    },
    {
        "id": 6,
        "nombre": "Dineroviejo",
        "altura": 1.2,
        "habilidad": "Evadir impuestos",
        "imagen": "https://via.placeholder.com/200",
        "frase_filosofica": "El que es pobre, es pobre porque quiere."
    },
    {
        "id": 7,
        "nombre": "Alternos",
        "altura": 0.9,
        "habilidad": "Diseñar interactivamente",
        "imagen": "https://via.placeholder.com/200",
        "frase_filosofica": "Hay personas que se odian, porque un día se quisieron."
    },
    {
        "id": 8,
        "nombre": "Undergolio",
        "altura": 1.8,
        "habilidad": "Ser original",
        "imagen": "https://via.placeholder.com/200",
        "frase_filosofica": "Si no es oversized, ahí no es."
    },
    {
        "id": 9,
        "nombre": "Eafitense",
        "altura": 0.7,
        "habilidad": "Faltar a clase",
        "imagen": "https://via.placeholder.com/200",
        "frase_filosofica": "¿El parqueadero está lleno?"
    }
]

def get_random_pokenea():
    return random.choice(POKENEAS)
