from flask import Flask, render_template, request, jsonify
import json
import requests
import python_sql_licenses as ps

app = Flask(__name__)


# with open("data/dico_sites.json", "r", encoding="utf-8") as fichier_json:
#    dico_sites = json.load(fichier_json)


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
    if request.method == 'POST':                        # Si la méthode est POST
        site = request.get_json()                       # On récupère les données au format JSON fournit dans la requête
        test = ps.post("site", site)              # On effectue une requête POST grâce à notre module ps
        return f"Succès de l'opération : {test}"        # On retourne le résultat de l'opération, qui est un booléen
    elif request.method == 'GET':                       # Si la méthode est GET
        result = ps.get(["site"])                       # On effectue une requête GET grâce à notre module ps
        return jsonify(result)                          # On retourne les données demandées


@app.route('/site/<id>', methods=['GET', 'PATCH', 'DELETE'])
def findSiteById(id):
    if request.method == 'GET':  # si la méthode est GET
        return "Succès de la méthode GET !"
    elif request.method == 'PATCH':  # si la méthode est PATCH
        return "Succès de la méthode PATCH !"
    elif request.method == 'DELETE':  # si la méthode est DELETE
        return "Succès de la méthode PATCH !"


# Endpoints des objets Provider


@app.route('/provider', methods=['GET', 'POST'])
def provider():
    if request.method == 'POST':                        # Si la méthode est POST
        provider = request.get_json()                   # On récupère les données au format JSON fournit dans la requête
        test = ps.post("provider", provider)      # On effectue une requête POST grâce à notre module ps
        return f"Succès de l'opération : {test}"        # On retourne le résultat de l'opération, qui est un booléen
    elif request.method == 'GET':                       # Si la méthode est GET
        result = ps.get(["provider"])                   # On effectue une requête GET grâce à notre module ps
        return jsonify(result)                          # On retourne les données demandées


@app.route('/provider/<id>', methods=['GET', 'PATCH', 'DELETE'])
def findProviderById(id):
    if request.method == 'GET':  # si la méthode est GET
        return "Succès de la méthode GET !"
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
    if request.method == 'POST':                        # Si la méthode est POST
        product = request.get_json()                    # On récupère les données au format JSON fournit dans la requête
        test = ps.post("product", product)        # On effectue une requête POST grâce à notre module ps
        return f"Succès de l'opération : {test}"        # On retourne le résultat de l'opération, qui est un booléen
    elif request.method == 'GET':                       # Si la méthode est GET
        result = ps.get(["product"])                    # On effectue une requête GET grâce à notre module ps
        return jsonify(result)                          # On retourne les données demandées


@app.route('/product/<id>', methods=['GET', 'PATCH', 'DELETE'])
def findProductById(id):
    if request.method == 'GET':  # si la méthode est GET
        return "Succès de la méthode GET !"
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
        return "Succès de la méthode GET !"
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
