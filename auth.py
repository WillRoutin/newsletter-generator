"""
Module d'authentification simple pour l'application
"""
from functools import wraps
from flask import request, Response
import os


def check_auth(username, password):
    """
    Vérifie les identifiants de connexion.

    Args:
        username: Nom d'utilisateur fourni
        password: Mot de passe fourni

    Returns:
        True si les identifiants sont corrects, False sinon
    """
    correct_username = os.environ.get('AUTH_USERNAME', 'admin')
    correct_password = os.environ.get('AUTH_PASSWORD', 'changez-moi')

    return username == correct_username and password == correct_password


def authenticate():
    """
    Envoie une réponse 401 demandant une authentification.
    """
    return Response(
        'Authentification requise.\n'
        'Veuillez vous connecter avec vos identifiants.',
        401,
        {'WWW-Authenticate': 'Basic realm="UX Curation - Accès restreint"'}
    )


def requires_auth(f):
    """
    Décorateur pour protéger les routes avec une authentification HTTP Basic.

    Usage:
        @app.route('/protected')
        @requires_auth
        def protected_route():
            return 'Contenu protégé'
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        # Si l'authentification est désactivée, laisser passer
        if os.environ.get('ENABLE_AUTH', 'False') != 'True':
            return f(*args, **kwargs)

        # Vérifier les identifiants
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()

        return f(*args, **kwargs)

    return decorated
