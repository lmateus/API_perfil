from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from products import profile_data
from profile_gdal_t import pruebaPerfil
from Perfil import Perfil

@app.route('/ping')
def ping():
    return jsonify({"message":"pong"})

@app.route('/products')
def getProducts():
    return jsonify(profile_data)

@app.route('/products',methods=['POST'])
def addProduct():

    profile = Perfil(request.json["Punto_inicial"],request.json["Punto_final"])
    profile.datos_perfil()
    return jsonify(profile.profile_json)

if __name__ == '__main__':
    app.run(debug=True, port=4000)