import boto3
import os, random

BUCKET_NAME = "pokeneas-valeyjuank"
s3 = boto3.client("s3", region_name="us-east-1")
S3_BUCKET = os.getenv("S3_BUCKET", "pokeneas-valeyjuank")
S3_REGION = os.getenv("AWS_DEFAULT_REGION", "us-east-1")
S3_PREFIX = os.getenv("S3_PREFIX", "")

POKENEAS = [
    {
        "id": 1,
        "nombre": "Leoncini",
        "altura": 1.6,
        "habilidad": "Amigo de lo ajeno",
        "imagen": "Leoncini.png",
        "frase_filosofica": "Las cosas no son del dueño, son de quien las necesita."
    },
    {
        "id": 2,
        "nombre": "Grillachu",
        "altura": 1.5,
        "habilidad": "Farra infinita",
        "imagen": "Grillachu.png",
        "frase_filosofica": "Sonríe, que la vida es un soplo."
    },
    {
        "id": 3,
        "nombre": "Mozita",
        "altura": 1.4,
        "habilidad": "Dañar hogares",
        "imagen": "Mozita.png",
        "frase_filosofica": "Cada quien cuida lo que le interesa y descuida lo que le estorba."
    },
    {
        "id": 4,
        "nombre": "Barbie",
        "altura": 0.6,
        "habilidad": "Recuperación rápida",
        "imagen": "Barbie.png",
        "frase_filosofica": "Tú puedes ser lo que quieras ser."
    },
    {
        "id": 5,
        "nombre": "Bancolombio",
        "altura": 1.0,
        "habilidad": "Cabello inmóvil",
        "imagen": "Bancolombio.png",
        "frase_filosofica": "¿Quieres ser tu propio jefe?"
    },
    {
        "id": 6,
        "nombre": "Dineroviejo",
        "altura": 1.2,
        "habilidad": "Evadir impuestos",
        "imagen": "Dineroviejo.png",
        "frase_filosofica": "El que es pobre, es pobre porque quiere."
    },
    {
        "id": 7,
        "nombre": "Alternito",
        "altura": 0.9,
        "habilidad": "Diseñar interactivamente",
        "imagen": "Alternito.png",
        "frase_filosofica": "Hay personas que se odian, porque un día se quisieron."
    },
    {
        "id": 8,
        "nombre": "Undergolio",
        "altura": 1.8,
        "habilidad": "Ser original",
        "imagen": "Undergolio.png",
        "frase_filosofica": "Si no es oversized, ahí no es."
    }
]



def public_url(filename: str) -> str:
    return f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{S3_PREFIX}{key}"


def get_random_pokenea():
    pok = random.choice(POKENEAS).copy()
    img_key = pok.get("imagen")

    if not img_key:
        img_key = f'{pok["nombre"]}.png'

    pok["imagen"] = public_url(img_key)
    return pok