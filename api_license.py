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

# !!!! A refaire car idk how to faire tree avec les liens entre les ids
@app.route("/licence/", methods=['GET'])
def menu(): 
    site_id = request.args.get("site") if request.args.get("site") else 0
    cles_site = ['id','name']
    cles_provider = ['id','name']
    cles_product = ['id','name','nb_licenses','nb_used_licenses','provider_id','site_id']
    cles_licence = ['key', 'date_start', 'date_expiration', 'is_used', 'user_id', 'product_id']
    sites = ps.get('licence',['site'])
    sites = [{key:value for key,value in zip(cles_site, groupe)} for groupe in sites]
    contenu_site = ps.get('licence',['group'], 'parent_id',group_id)
    contenu_site = [{key:value for key,value in zip(cles_site, cont)} for cont in contenu_site]
    contenu_provider = ps.get('licence',['subnet'], 'group_id',group_id)
    contenu_provider = [{key:value for key,value in zip(cles_provider, cont)} for cont in contenu_provider]
    contenu_product = ps.get('licence',['subnet'], 'group_id',group_id)
    contenu_product = [{key:value for key,value in zip(cles_product, cont)} for cont in contenu_product]
    contenu_licence = ps.get('licence',['subnet'], 'group_id',group_id)
    contenu_licence = [{key:value for key,value in zip(cles_licence, cont)} for cont in contenu_licence]
    return render_template('licence.html', tree=groupes, groupes=contenu_groupe, subnets=contenu_subnet)


# --------------------------- Edit Object -----------------------------

@app.route('/edit/site', methods = ['GET'])
def edit_site():
    cles_site = ['id','name']
    id = request.args.get("id")
    site = ps.get('licence',['site'], 'id', id)
    site = {key:value for key,value in zip(cles_site, site[0])} 
    sites = ps.get('licence',['site'])
    sites = [{key:value for key,value in zip(cles_site, site)} for site in sites]
    return render_template('edit_site.html', site=site, sites=sites)

@app.route('/edit/provider', methods = ['GET'])
def edit_site():
    cles_provider = ['id','name']
    id = request.args.get("id")
    provider = ps.get('licence',['provider'], 'id', id)
    provider = {key:value for key,value in zip(cles_provider, provider[0])} 
    providers = ps.get('licence',['provider'])
    providers = [{key:value for key,value in zip(cles_provider, provider)} for provider in providers]
    return render_template('edit_site.html', provider=provider, providers=providers)

@app.route('/edit/product', methods = ['GET'])
def edit_product():
    cles_site = ['id','name']
    cles_product = ['id','name','nb_licenses','nb_used_licenses','provider_id','site_id']
    id = request.args.get("id")
    product = ps.get('licence',['product'], 'id', id)
    product = {key:value for key,value in zip(cles_product, product[0])} 
    sites = ps.get('licence',['site'])
    sites = [{key:value for key,value in zip(cles_site, site)} for site in sites]
    return render_template('edit_product.html', product=product, sites=sites)

@app.route('/edit/licence', methods = ['GET'])
def edit_licence():
    cles_site = ['id','name']
    cles_licence = ['id','name','nb_licenses','nb_used_licenses','provider_id','site_id']
    id = request.args.get("id")
    licence = ps.get('licence',['licence'], 'id', id)
    licence = {key:value for key,value in zip(cles_licence, licence[0])} 
    sites = ps.get('licence',['site'])
    sites = [{key:value for key,value in zip(cles_site, site)} for site in sites]
    return render_template('edit_licence.html', licence=licence, sites=sites)


# --------------------------- New Object -----------------------------

@app.route('/new/site/', methods = ['GET'])
def new_site():
    cles_site = ['id','name']
    sites = ps.get('licence',['site'])
    sites = [{key:value for key,value in zip(cles_site, site)} for groupe in sites]
    return render_template('new_site.html', sites=sites)

@app.route('/new/provider/', methods = ['GET'])
def new_provider():
    cles_provider = ['id','name']
    providers = ps.get('licence',['provider'])
    providers = [{key:value for key,value in zip(cles_provider, provider)} for provider in providers]
    return render_template('new_provider.html', providers=providers)

@app.route('/new/product/', methods = ['GET'])
def new_product():
    cles_product = ['id','name','nb_licenses','nb_used_licenses','provider_id','site_id']
    products = ps.get('licence',['product'])
    products = [{key:value for key,value in zip(cles_product, product)} for product in products]
    return render_template('new_product.html', products=products)

@app.route('/new/provider/', methods = ['GET'])
def new_licence():
    cles_licence = ['key', 'date_start', 'date_expiration', 'is_used', 'user_id', 'product_id']
    licences = ps.get('licence',['site'])
    licences = [{key:value for key,value in zip(cles_licence, licence)} for licence in licences]
    return render_template('new_provider.html', licences=licences)


# --------------------------- Edit Database Object -----------------------------

@app.route('/action_form/site/<int:id>', methods = ['POST'])
def action_form_site(id:int):
    if id == 0:
        id = request.form.get('id')
    arguments = {'id': id,
                 'name': request.form.get('name')}
    ps.delete('licence','site',id)
    ps.put('licence','site', arguments)
    return redirect('/licence')

@app.route('/action_form/provider/<int:id>', methods=['POST'])
def action_form_provider(id: int):
    if id == 0:
        id = request.form.get('id')
    arguments = {
        'id': id,
        'name': request.form.get('name')
    }
    ps.delete('licence','provider',id)
    ps.put('licence','provider', arguments)
    return redirect('/licence')

@app.route('/action_form/product/<int:id>', methods=['POST'])
def action_form_product(id: int):
    if id == 0:
        id = request.form.get('id')
    arguments = {
        'id': id,
        'name': request.form.get('name'),
        'nb_licenses': request.form.get('nb_licenses'),
        'nb_used_licenses': request.form.get('nb_used_licenses'),
        'provider_id': request.form.get('provider_id'),
        'site_id': request.form.get('site_id')
    }
    ps.delete('licence','product',id)
    ps.put('licence','product', arguments)
    return redirect('/licence')

@app.route('/action_form/license/<int:id>', methods=['POST'])
def action_form_license(id: int):
    if id == 0:
        id = request.form.get('id')
    arguments = {
        'id': id,
        'key': request.form.get('key'),
        'date_start': request.form.get('date_start'),
        'date_expiration': request.form.get('date_expiration'),
        'is_used': request.form.get('is_used'),
        'user_id': request.form.get('user_id'),
        'product_id': request.form.get('product_id')
    }
    ps.delete('licence','licence',id)
    ps.put('licence','licence', arguments)
    return redirect('/licence')


# --------------------------- Delete Object -----------------------------

@app.route('/delete/site')
def delete_site():
    id = request.args.get('id')
    ps.delete('licence', 'site', id)
    return redirect('/licence')

@app.route('/delete/provider')
def delete_provider():
    id = request.args.get('id')
    ps.delete('licence', 'provider', id)
    return redirect('/licence')

@app.route('/delete/product')
def delete_product():
    id = request.args.get('id')
    ps.delete('licence', 'product', id)
    return redirect('/licence')

@app.route('/delete/license')
def delete_license():
    id = request.args.get('id')
    ps.delete('licence', 'license', id)
    return redirect('/licence')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009)
