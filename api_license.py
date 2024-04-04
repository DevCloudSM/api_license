from flask import Flask, render_template, request, jsonify, Response
import json
import requests
import python_sql as ps

app = Flask(__name__)

nom_db = 'licenses'


@app.route('/', endpoint='page_accueil')
def index():
    """
    Render the index HTML page.

    :return: The index HTML page.
    :rtype: str
    """
    return render_template("index_licenses.j2")


# Endpoints des objets Site


@app.route('/site', methods=['GET', 'POST'])
def site():
    if request.method == 'POST':
        test = ps.post(f'{nom_db}', 'site', {'name': request.get_json()})
        return f"Succès de l'opération : {test}"
    elif request.method == 'GET':
        result = ps.get(f'{nom_db}', ['site'])
        return jsonify(result)


@app.route('/site/<id>', methods=['GET', 'PATCH', 'DELETE'])
def findSiteById(id: str) -> Response | str:
    if request.method == 'GET':  # si la méthode est GET
        result = ps.get(f'{nom_db}', ["site"], "id", id)  # On effectue une requête GET grâce à notre module ps
        return jsonify(result)  # On retourne les données demandées
    elif request.method == 'PATCH':  # si la méthode est PATCH
        return "Succès de la méthode PATCH !"
    elif request.method == 'DELETE':  # si la méthode est DELETE
        return "Succès de la méthode PATCH !"


# Endpoints des objets Provider


@app.route('/provider', methods=['GET', 'POST'])
def provider():
    if request.method == 'POST':
        test = ps.post(f'{nom_db}', 'provider', {'name': request.get_json()})
        return f"Succès de l'opération : {test}"
    elif request.method == 'GET':
        result = ps.get(f'{nom_db}', ['provider'])
        return jsonify(result)


@app.route('/provider/<id>', methods=['GET', 'PATCH', 'DELETE'])
def findProviderById(id):
    if request.method == 'GET':  # si la méthode est GET
        result = ps.get(f'{nom_db}', ["provider"], "id", id)  # On effectue une requête GET grâce à notre module ps
        return jsonify(result)  # On retourne les données demandées
    elif request.method == 'PATCH':  # si la méthode est PATCH
        return "Succès de la méthode PATCH !"
    elif request.method == 'DELETE':  # si la méthode est DELETE
        return "Succès de la méthode PATCH !"


@app.route('/provider/findByName', methods=['GET'])
def findProviderByName():
    return "Succès de la méthode GET !"


# Endpoints des objets Product


@app.route('/product', methods=['GET', 'POST'])
def product():
    if request.method == 'POST':
        product_fields = request.get_json()
        test = ps.post(f'{nom_db}', 'provider', {f"{product_fields.keys()}": val for val in product_fields.values()})
        return f"Succès de l'opération : {test}"
    elif request.method == 'GET':
        result = ps.get(f'{nom_db}', ['product'])
        return jsonify(result)


@app.route('/product/<id>', methods=['GET', 'PATCH', 'DELETE'])
def findProductById(id):
    if request.method == 'GET':  # si la méthode est GET
        result = ps.get(f'{nom_db}', ["product"], "id", id)  # On effectue une requête GET grâce à notre module ps
        return jsonify(result)  # On retourne les données demandées
    elif request.method == 'PATCH':  # si la méthode est PATCH
        return "Succès de la méthode PATCH !"
    elif request.method == 'DELETE':  # si la méthode est DELETE
        return "Succès de la méthode PATCH !"


@app.route('/product/findByName', methods=['GET'])
def findProductByName():
    return "Succès de la méthode GET !"


# Endpoints des objets Licenses


@app.route('/license', methods=['GET', 'POST'])
def license():
    if request.method == 'POST':                        # Si la méthode est POST
        license = request.get_json()                    # On récupère les données au format JSON fournit dans la requête
        test = ps.post("license", license)        # On effectue une requête POST grâce à notre module ps
        return f"Succès de l'opération : {test}"        # On retourne le résultat de l'opération, qui est un booléen
    elif request.method == 'GET':                       # Si la méthode est GET
        result = ps.get(["license"])                    # On effectue une requête GET grâce à notre module ps
        return jsonify(result)                          # On retourne les données demandées


@app.route('/license/<id>', methods=['GET', 'PATCH', 'DELETE'])
def findLicenseById(id):
    if request.method == 'GET':  # si la méthode est GET
        result = ps.get(f'{nom_db}', ["license"], "id", id)  # On effectue une requête GET grâce à notre module ps
        return jsonify(result)  # On retourne les données demandées
    elif request.method == 'PATCH':  # si la méthode est PATCH
        return "Succès de la méthode PATCH !"
    elif request.method == 'DELETE':  # si la méthode est DELETE
        return "Succès de la méthode PATCH !"


@app.route('/license/findByKey', methods=['GET'])
def findLicenseByKey():
    return "Succès de la méthode GET !"


@app.route('/license/findByIsUsed', methods=['GET'])
def findLicenseByIsUsed():
    return "Succès de la méthode GET !"


@app.route('/license/findByIdUser', methods=['GET'])
def findLicenseByIdUser():
    return "Succès de la méthode GET !"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009)
