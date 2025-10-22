from flask import Blueprint, jsonify, render_template
import socket
from .data import get_random_pokenea

main = Blueprint('main', __name__)


@main.route("/")
def home():
    return "OK - Usa /pokenea-json o /pokenea-imagen"

@main.route("/pokenea-json")
def pokenea_json():
    pokenea = get_random_pokenea()
    container_id = socket.gethostname()
    response = {
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "container_id": container_id
    }
    return jsonify(response)

@main.route("/pokenea-imagen")
def pokenea_imagen():
    pokenea = get_random_pokenea()
    container_id = socket.gethostname()
    return render_template("pokenea.html", pokenea=pokenea, container_id=container_id)
