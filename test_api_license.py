from typing import Tuple, Any

import requests
import json
from requests.structures import CaseInsensitiveDict

# Adresse et port du serveur hébergeant l'API à interroger
adresse = "localhost"
port = 5009


def test_requete(method: str = 'GET', path: str = '/', data: dict[str, str] = {}) -> str | tuple[str, Any]:
    headers = CaseInsensitiveDict()
    headers['Content-Type'] = 'application/json'
    if method.upper() == "GET":
        test = requests.get(f'http://{adresse}:{port}{path}')
    elif method.upper() == "DELETE":
        test = requests.delete(f'http://{adresse}:{port}{path}')
    elif method.upper() == "POST":
        test = requests.post(f'http://{adresse}:{port}{path}', headers=headers, data=json.dumps(data))
    elif method.upper() == "PATCH":
        test = requests.patch(f'http://{adresse}:{port}{path}', headers=headers, data=json.dumps(data))
    else:
        return f"Method {method.upper()} not allowed or not implemented\nRetry with one of the following methods:\n\tGET\n\tPOST\n\tPATCH\n\tDELETE"
    return f'Code {test.status_code}', json.loads(test.text)


# ----- Tests Site -----
print("\n----- Tests Site -----")

# GET /site
try:
    print(test_requete("GET", "/site"))
except Exception as e:
    print(e)

# POST /site

# GET /site/{siteId}
try:
    sites = test_requete("GET", "/site/1")[1]
    vannes = sites[0]
    test = vannes == [1, 'Vannes']
except Exception as e:
    print(e)
    test = False
print(f'GET /site/{{siteId}} : {test}')

# PATCH /site/{siteId}

# DELETE /site/{siteId}

# GET /site/findByName?name=...
try:
    groupes = test_requete("GET", "/site/findByName?name=Vannes")[1]
    vannes = groupes[0]
    test = vannes == [1, 'Vannes']
except:
    test = False
print(f'GET /group : {test}')


# ----- Tests Provider -----
print("\n----- Tests Provider -----")

# GET /provider
try:
    print(test_requete("GET", "/provider"))
except Exception as e:
    print(e)

# POST /provider

# GET /provider/{providerId}
try:
    providers = test_requete("GET", "/provider/1")[1]
    microsoft = providers[0]
    test = microsoft == [1, 'Microsoft']
except Exception as e:
    print(e)
    test = False
print(f'GET /provider/{{providerId}} : {test}')

# PATCH /provider/{providerId}

# DELETE /provider/{providerId}

# GET /provider/findByName?name=...


# ----- Tests Product -----
print("\n----- Tests Product -----")

# GET /product
try:
    print(test_requete("GET", "/product"))
except Exception as e:
    print(e)

# POST /product

# GET /product/{productId}
try:
    products = test_requete("GET", "/product/1")[1]
    win10 = products[0]
    test = win10 == [1, 'Windows 10']
except Exception as e:
    print(e)
    test = False
print(f'GET /site/{{productId}} : {test}')

# PATCH /product/{productId}

# DELETE /product/{productId}

# GET /product/findByName?name=...


# ----- Tests License -----
print("\n----- Tests License -----")

# GET /license
try:
    print(test_requete("GET", "/license"))
except Exception as e:
    print(e)

# POST /license

# GET /license/{licenseId}
try:
    licenses = test_requete("GET", "/license/1")[1]
    license1 = licenses[0]
    # À modifier après création des données dans la base
    #test = license1 == [1, 'Windows 10']
except Exception as e:
    print(e)
    test = False
print(f'GET /license/{{licenseId}} : {test}')

# PATCH /license/{licenseId}

# DELETE /license/{licenseId}

# GET /license/findByKey?key=...

# GET /license/findByIsUsed?boolean=...

# GET /license/findByIdUser?idUser=...
