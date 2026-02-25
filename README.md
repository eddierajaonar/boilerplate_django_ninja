# Django Ninja Boilerplate

[![Django](https://img.shields.io/badge/Django-5.x-green.svg)](https://www.djangoproject.com/)
[![Django Ninja](https://img.shields.io/badge/Django%20Ninja-latest-blue.svg)](https://django-ninja.rest-framework.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Un boilerplate Django moderne et prêt à l'emploi utilisant Django Ninja pour créer des API REST rapides et type-safe. Ce projet inclut une authentification JWT, un CRUD complet pour les produits, et un support Docker pour un déploiement simplifié.

## 🚀 Fonctionnalités

- ✅ **Django Ninja** - Framework API rapide avec validation automatique des schémas
- 🔐 **Authentification JWT** - Système d'authentification sécurisé avec tokens JWT
- 📦 **CRUD complet** - Exemple d'API pour la gestion de produits
- 🐳 **Docker Ready** - Configuration Docker et Docker Compose incluse
- 🗄️ **PostgreSQL** - Support PostgreSQL en production via Docker
- 🔄 **CORS configuré** - Headers CORS configurés pour les applications frontend
- 📝 **Documentation automatique** - Documentation interactive Swagger/OpenAPI
- 🎯 **Type-safe** - Validation de schémas avec Pydantic
- 🌐 **Variables d'environnement** - Configuration via fichier .env

## 📋 Prérequis

- Python 3.10 ou supérieur
- pip (gestionnaire de paquets Python)
- PostgreSQL (optionnel, SQLite par défaut)
- Docker & Docker Compose (pour le déploiement avec Docker)

## 🛠️ Technologies utilisées

| Technologie | Description |
|-------------|-------------|
| Django | Framework web Python de haut niveau |
| Django Ninja | Framework API REST moderne et rapide |
| PostgreSQL | Base de données relationnelle |
| python-jose | Implémentation JWT pour l'authentification |
| passlib | Bibliothèque de hachage de mots de passe |
| python-dotenv | Gestion des variables d'environnement |
| django-cors-headers | Gestion des en-têtes CORS |

## 📦 Installation

### Option 1 : Installation locale

1. **Cloner le repository**
   ```bash
   git clone <repository-url>
   cd BOILERPLATE_DJANGO_NINJA
   ```

2. **Créer et activer l'environnement virtuel**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   # .venv\Scripts\activate   # Windows
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer les variables d'environnement**
   ```bash
   cp .env.example .env
   # Éditer le fichier .env avec vos valeurs
   ```

5. **Appliquer les migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Créer un superutilisateur**
   ```bash
   python manage.py createsuperuser
   ```

7. **Lancer le serveur de développement**
   ```bash
   python manage.py runserver
   ```

Le serveur sera accessible sur `http://localhost:8000`

### Option 2 : Déploiement avec Docker

1. **Cloner le repository**
   ```bash
   git clone <repository-url>
   cd BOILERPLATE_DJANGO_NINJA
   ```

2. **Configurer les variables d'environnement**
   ```bash
   cp .env.example .env
   # Éditer le fichier .env avec vos valeurs PostgreSQL
   ```

3. **Construire et démarrer les conteneurs**
   ```bash
   docker compose up --build
   ```

4. **Créer un superutilisateur (dans un nouveau terminal)**
   ```bash
   docker exec -it django_backend python manage.py createsuperuser
   ```

Le serveur sera accessible sur `http://localhost:8000`

## 📚 Documentation API

Une fois le serveur lancé, accédez à la documentation interactive Swagger :

**URL :** `http://localhost:8000/api/docs`

La documentation interactive vous permet de :
- Visualiser tous les endpoints disponibles
- Tester les requêtes directement depuis l'interface
- Voir les schémas de requête/réponse
- Consulter les codes de statut HTTP

## 🔌 Endpoints API

### Authentification

| Méthode | Endpoint | Description | Auth requise |
|---------|----------|-------------|--------------|
| POST | `/api/register` | Créer un nouveau compte utilisateur | ❌ |
| POST | `/api/login` | Se connecter et obtenir un token JWT | ❌ |
| POST | `/api/refresh` | Rafraîchir le token JWT | ✅ |

#### Exemple de requête d'inscription
```json
POST /api/register
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "SecurePassword123"
}
```

#### Exemple de requête de connexion
```json
POST /api/login
{
  "username": "john_doe",
  "password": "SecurePassword123"
}
```

#### Réponse de connexion
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### Produits (CRUD)

| Méthode | Endpoint | Description | Auth requise |
|---------|----------|-------------|--------------|
| GET | `/api/products` | Récupérer la liste de tous les produits | ✅ |
| POST | `/api/products` | Créer un nouveau produit | ✅ |
| PUT | `/api/products/{id}` | Mettre à jour un produit existant | ✅ |
| DELETE | `/api/products/{id}` | Supprimer un produit | ✅ |

#### Exemple de requête de création de produit
```json
POST /api/products
Authorization: Bearer <your_token>

{
  "name": "Laptop Dell XPS 15",
  "description": "Ordinateur portable haut de gamme",
  "price": 1499.99,
  "stock": 10
}
```

## ⚙️ Configuration

### Variables d'environnement

Créez un fichier `.env` à la racine du projet (voir `.env.example`) :

```env
# Django Configuration
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=True

# JWT Configuration
JWT_SECRET=your-jwt-secret-here

# Database Configuration
DATABASE_URL=sqlite:///db.sqlite3

# PostgreSQL (pour Docker)
POSTGRES_DB=your_database_name
POSTGRES_USER=your_database_user
POSTGRES_PASSWORD=your_database_password
```

### Structure du projet

```
BOILERPLATE_DJANGO_NINJA/
├── core/                   # Configuration Django principale
│   ├── settings.py        # Paramètres Django
│   ├── urls.py            # Routes principales
│   └── wsgi.py            # Configuration WSGI
├── myapp/                 # Application principale
│   ├── api.py             # Endpoints API
│   ├── auth.py            # Logique d'authentification
│   ├── models.py          # Modèles de base de données
│   ├── schema.py          # Schémas Pydantic
│   └── migrations/        # Migrations de base de données
├── templates/             # Templates HTML (si nécessaire)
├── .env.example           # Exemple de configuration
├── docker-compose.yml     # Configuration Docker Compose
├── Dockerfile             # Configuration Docker
├── entrypoint.sh          # Script de démarrage Docker
├── manage.py              # CLI Django
├── requirements.txt       # Dépendances Python
└── README.md              # Ce fichier
```

## 🔐 Sécurité

### Bonnes pratiques implémentées

- ✅ Mots de passe hachés avec `passlib`
- ✅ Tokens JWT avec expiration
- ✅ Variables sensibles dans `.env` (non versionné)
- ✅ CORS configuré pour limiter les origines autorisées
- ✅ Validation des entrées avec Pydantic

### Recommandations pour la production

1. **Désactiver le mode DEBUG**
   ```env
   DEBUG=False
   ```

2. **Utiliser une clé secrète forte**
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

3. **Configurer ALLOWED_HOSTS**
   ```python
   ALLOWED_HOSTS = ['votre-domaine.com']
   ```

4. **Utiliser HTTPS en production**

5. **Configurer une base de données PostgreSQL**

## 🧪 Tests

Pour exécuter les tests :

```bash
python manage.py test
```

Avec Docker :

```bash
docker exec -it django_backend python manage.py test
```

## 📝 Commandes utiles

### Migrations de base de données

```bash
# Créer de nouvelles migrations
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Voir l'état des migrations
python manage.py showmigrations
```

### Gestion des utilisateurs

```bash
# Créer un superutilisateur
python manage.py createsuperuser

# Changer le mot de passe d'un utilisateur
python manage.py changepassword <username>
```

### Django Shell

```bash
# Ouvrir le shell Django
python manage.py shell

# Avec Docker
docker exec -it django_backend python manage.py shell
```

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Commiter vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Pousser vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 📧 Support

Pour toute question ou problème, n'hésitez pas à :
- Ouvrir une issue sur GitHub
- Consulter la documentation Django Ninja : https://django-ninja.rest-framework.com/
- Consulter la documentation Django : https://docs.djangoproject.com/

## 🌟 Remerciements

- [Django](https://www.djangoproject.com/) - Le framework web pour perfectionnistes avec des deadlines
- [Django Ninja](https://django-ninja.rest-framework.com/) - API web rapide pour Django
- [FastAPI](https://fastapi.tiangolo.com/) - Inspiration pour l'approche type-safe

---

Développé avec ❤️ en utilisant Django et Django Ninja
