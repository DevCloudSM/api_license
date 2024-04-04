
### Fichier `python_sql.py`

Ce module permet d'interagir avec une base de données PostgreSQL. Il inclut des fonctions pour effectuer des opérations pour (Créer, Lire, Mettre à jour, Supprimer), ainsi que pour la gestion de la base de données et des tables.

- **get_id(database: str = '') -> dict[str, str]:** Génère les identifiants de connexion à la base de données.
- **log(message: str) -> bool:** Enregistre un message dans un fichier log.
- **format_sql(data: Union[str, int, list[str], list[int], bool]) -> str:** Formate les données pour les requêtes SQL.
- **get(database: str, tables: list[str], variable: str = "", operation: str = "=", valeur: str = "") -> list[tuple]:** Récupère des données depuis la base de données.
- **post(database: str, table: str, data: dict[str, any]) -> bool:** Ajoute une nouvelle entrée dans une table.
- **patch(database: str, table: str, object_id : int, data: dict[str, any]) -> bool:** Met à jour une entrée existante dans une table.
- **delete(database: str, table: str, id: int) -> bool:** Supprime une entrée dans une table.
- **create_database(name: str = 'database_1') -> bool:** Crée une nouvelle base de données.
- **create_table(database: str, table_name: str) -> bool:** Crée une nouvelle table.
- **add_column(database: str, table: str, column_name: str, type: type | str) -> bool:** Ajoute une colonne à une table.

### Fichier `api_license.py`

Ce module définit une API Flask pour la gestion des licences. Il interagit avec la base de données via le module `python_sql.py` pour fournir des endpoints relatifs à la gestion des licences, des sites, des fournisseurs (providers), et des produits.

- **Endpoints pour les opérations sur les objets Site, Provider, Product, et License:**
  - **GET, POST, PATCH, DELETE** méthodes sont disponibles pour interagir avec les données de ces objets dans la base de données. Chaque type d'objet (Site, Provider, Product, License) a des routes spécifiques pour la création, la lecture, la mise à jour, et la suppression.
  - **Recherche par nom ou d'autres attributs spécifiques** est également disponible pour certains objets, permettant une récupération facile basée sur des critères autres que l'ID.

- **Exemple de route:**
  - `@api_license.route('/site', methods=['GET', 'POST'])` définit les opérations de base pour l'objet Site, permettant de récupérer la liste des sites ou d'en ajouter un nouveau.

