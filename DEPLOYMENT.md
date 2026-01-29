# 🚀 Guide de déploiement - UX Curation Newsletter Generator

Ce guide vous explique comment déployer votre générateur de newsletter sur différentes plateformes cloud pour le rendre accessible à votre équipe.

---

## 📋 Prérequis

Avant de commencer, assurez-vous d'avoir:
- Un compte GitHub (pour toutes les plateformes sauf PythonAnywhere)
- Votre projet versionné avec Git
- Les fichiers de configuration créés (déjà fait ✅)

---

## 🔧 Initialiser Git (si pas déjà fait)

```bash
# Initialiser le dépôt Git
git init

# Ajouter tous les fichiers
git add .

# Créer le premier commit
git commit -m "Initial commit: UX Curation Newsletter Generator"

# Créer un dépôt sur GitHub et le lier
git remote add origin https://github.com/VOTRE_USERNAME/newsletter-generator.git
git branch -M main
git push -u origin main
```

---

## Option 1: Render.com (⭐ Recommandé - Gratuit)

### Avantages
- ✅ Gratuit pour toujours (tier gratuit)
- ✅ Déploiement automatique depuis GitHub
- ✅ SSL automatique (HTTPS)
- ✅ Simple et rapide

### Étapes de déploiement

1. **Créer un compte sur [Render.com](https://render.com)**

2. **Créer un nouveau Web Service**
   - Cliquer sur "New +" → "Web Service"
   - Connecter votre compte GitHub
   - Sélectionner le repository `newsletter-generator`

3. **Configurer le service**
   - **Name:** `ux-curation-newsletter` (ou ce que vous voulez)
   - **Region:** Choisir la région la plus proche
   - **Branch:** `main`
   - **Runtime:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`

4. **Variables d'environnement**
   Aller dans "Environment" et ajouter:
   ```
   SECRET_KEY=votre-cle-secrete-aleatoire-tres-longue
   FLASK_DEBUG=False
   ENABLE_AUTH=True
   AUTH_USERNAME=admin
   AUTH_PASSWORD=votre-mot-de-passe-securise
   ```

5. **Déployer**
   - Cliquer sur "Create Web Service"
   - Attendre 5-10 minutes
   - Votre app sera disponible sur: `https://ux-curation-newsletter.onrender.com`

### ⚠️ Note importante
Le tier gratuit de Render met l'application en veille après 15 minutes d'inactivité. Le premier accès après une période d'inactivité peut prendre 30-60 secondes.

---

## Option 2: Railway.app (Moderne - Gratuit)

### Avantages
- ✅ Interface très moderne
- ✅ $5 de crédit gratuit/mois
- ✅ Déploiement ultra-rapide
- ✅ Pas de mise en veille

### Étapes de déploiement

1. **Créer un compte sur [Railway.app](https://railway.app)**

2. **Déployer depuis GitHub**
   - Cliquer sur "New Project"
   - Sélectionner "Deploy from GitHub repo"
   - Connecter GitHub et sélectionner votre repo

3. **Variables d'environnement**
   - Aller dans l'onglet "Variables"
   - Ajouter:
   ```
   SECRET_KEY=votre-cle-secrete
   FLASK_DEBUG=False
   ENABLE_AUTH=True
   AUTH_USERNAME=admin
   AUTH_PASSWORD=votre-mot-de-passe
   ```

4. **Générer un domaine**
   - Aller dans "Settings"
   - Cliquer sur "Generate Domain"
   - Votre app sera disponible sur: `https://votre-app.up.railway.app`

---

## Option 3: PythonAnywhere (Très simple - Gratuit)

### Avantages
- ✅ Spécialisé Python/Flask
- ✅ Très simple, pas besoin de Git
- ✅ Gratuit avec limitations

### Étapes de déploiement

1. **Créer un compte sur [PythonAnywhere.com](https://www.pythonanywhere.com)**

2. **Upload des fichiers**
   - Aller dans "Files"
   - Créer un dossier `newsletter-generator`
   - Uploader tous vos fichiers

3. **Installer les dépendances**
   - Aller dans "Consoles" → "Bash"
   - Exécuter:
   ```bash
   cd newsletter-generator
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Configurer l'application Web**
   - Aller dans "Web"
   - "Add a new web app" → "Manual configuration" → "Python 3.10"
   - Dans "Code" section:
     - Source code: `/home/VOTRE_USERNAME/newsletter-generator`
     - Working directory: `/home/VOTRE_USERNAME/newsletter-generator`
     - WSGI configuration file: Cliquer et remplacer par:
     ```python
     import sys
     path = '/home/VOTRE_USERNAME/newsletter-generator'
     if path not in sys.path:
         sys.path.append(path)

     from app import app as application
     ```
   - Dans "Virtualenv" section:
     - Entrer: `/home/VOTRE_USERNAME/newsletter-generator/venv`

5. **Reload**
   - Cliquer sur "Reload" en haut
   - Votre app sera disponible sur: `https://VOTRE_USERNAME.pythonanywhere.com`

---

## Option 4: Heroku (Payant - ~$7/mois)

### Avantages
- ✅ Très stable et fiable
- ✅ Excellente documentation
- ✅ Pas de mise en veille

### Étapes de déploiement

1. **Installer Heroku CLI**
   ```bash
   # macOS
   brew tap heroku/brew && brew install heroku

   # Ou télécharger depuis heroku.com
   ```

2. **Se connecter**
   ```bash
   heroku login
   ```

3. **Créer l'application**
   ```bash
   heroku create ux-curation-newsletter
   ```

4. **Configurer les variables d'environnement**
   ```bash
   heroku config:set SECRET_KEY=votre-cle-secrete
   heroku config:set FLASK_DEBUG=False
   heroku config:set ENABLE_AUTH=True
   heroku config:set AUTH_USERNAME=admin
   heroku config:set AUTH_PASSWORD=votre-mot-de-passe
   ```

5. **Déployer**
   ```bash
   git push heroku main
   ```

6. **Ouvrir l'application**
   ```bash
   heroku open
   ```

---

## 🔐 Sécurité et authentification

### Activer l'authentification

L'authentification HTTP Basic est déjà configurée. Pour l'activer:

1. **Définir les variables d'environnement**
   ```
   ENABLE_AUTH=True
   AUTH_USERNAME=votre-nom-utilisateur
   AUTH_PASSWORD=votre-mot-de-passe-securise
   ```

2. **Redémarrer l'application**

Vos utilisateurs devront entrer un nom d'utilisateur et mot de passe pour accéder à l'application.

### Désactiver l'authentification

```
ENABLE_AUTH=False
```

### Conseils de sécurité

- ✅ Utilisez un mot de passe fort (minimum 12 caractères)
- ✅ Changez régulièrement les mots de passe
- ✅ Utilisez des variables d'environnement, jamais de mots de passe dans le code
- ✅ Activez HTTPS (automatique sur Render, Railway, Heroku)

---

## 📦 Gestion du stockage des fichiers

### ⚠️ Important

Les fichiers uploadés (Excel) et générés (HTML) sont stockés sur le serveur. Sur les plateformes cloud gratuites:

- Les fichiers peuvent être **supprimés lors du redémarrage** du serveur
- L'espace de stockage est **limité**

### Solutions recommandées

#### Option A: Stockage temporaire (actuel)
Parfait si vous générez et téléchargez immédiatement les newsletters.

#### Option B: Stockage cloud (pour production)
Pour une solution plus robuste, intégrer:
- **AWS S3** (stockage de fichiers)
- **Google Cloud Storage**
- **Cloudinary** (pour les images)

---

## 🔄 Mises à jour de l'application

### Avec Git (Render, Railway, Heroku)

```bash
# Faire vos modifications
git add .
git commit -m "Description des changements"
git push origin main
```

Le déploiement se fera automatiquement sur Render et Railway. Pour Heroku:
```bash
git push heroku main
```

### PythonAnywhere

1. Uploader les fichiers modifiés via l'interface Web
2. Cliquer sur "Reload" dans l'onglet "Web"

---

## 📊 Monitoring et logs

### Render
- Onglet "Logs" pour voir les logs en temps réel

### Railway
- Onglet "Deployments" → "View Logs"

### Heroku
```bash
heroku logs --tail
```

### PythonAnywhere
- Aller dans "Web" → "Log files"

---

## 🆘 Dépannage

### L'application ne démarre pas

1. Vérifier les logs
2. Vérifier que toutes les dépendances sont dans `requirements.txt`
3. Vérifier les variables d'environnement

### Erreur "Application Error"

- Vérifier que `gunicorn` est installé
- Vérifier le `Procfile`
- Vérifier les logs

### Les fichiers ne sont pas sauvegardés

- Normal sur tier gratuit, les fichiers sont temporaires
- Solution: Télécharger immédiatement ou utiliser un stockage cloud

---

## 💰 Comparaison des coûts

| Plateforme | Gratuit | Payant | Notes |
|------------|---------|--------|-------|
| **Render** | ✅ Oui | $7/mois | Mise en veille après 15min |
| **Railway** | ✅ $5 crédit/mois | $5-20/mois | Pas de mise en veille |
| **PythonAnywhere** | ✅ Limité | $5/mois | Limitations CPU/stockage |
| **Heroku** | ❌ Non | $7-25/mois | Très stable |

---

## ✅ Checklist de déploiement

- [ ] Code versionné sur GitHub
- [ ] Variables d'environnement configurées
- [ ] Authentification activée (si nécessaire)
- [ ] Application testée localement
- [ ] Déployée sur la plateforme choisie
- [ ] URL partagée avec l'équipe
- [ ] Documentation créée pour l'équipe

---

## 🎓 Ressources supplémentaires

- [Documentation Render](https://render.com/docs)
- [Documentation Railway](https://docs.railway.app)
- [Documentation PythonAnywhere](https://help.pythonanywhere.com)
- [Documentation Heroku](https://devcenter.heroku.com)

---

**Bon déploiement ! 🚀**

Si vous avez des questions, consultez la documentation de la plateforme choisie ou ouvrez une issue sur GitHub.
