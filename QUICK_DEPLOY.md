# 🚀 Déploiement rapide - Guide express

## Option la plus simple : Render.com (5 minutes)

### 1️⃣ Préparer le code

```bash
# Initialiser Git (si pas déjà fait)
git init
git add .
git commit -m "Initial commit"

# Créer un repo sur GitHub et pousser
git remote add origin https://github.com/VOTRE_USERNAME/newsletter-generator.git
git branch -M main
git push -u origin main
```

### 2️⃣ Déployer sur Render

1. Aller sur [render.com](https://render.com) et créer un compte
2. Cliquer "New +" → "Web Service"
3. Connecter GitHub et sélectionner votre repo
4. Remplir:
   - **Name:** `ux-curation-newsletter`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`

5. Ajouter les variables d'environnement:
   ```
   SECRET_KEY = votre-cle-secrete-longue-et-aleatoire
   FLASK_DEBUG = False
   ENABLE_AUTH = True
   AUTH_USERNAME = admin
   AUTH_PASSWORD = VotreMotDePasseSecurise123!
   ```

6. Cliquer "Create Web Service"

### 3️⃣ C'est fini ! 🎉

Votre app sera disponible sur: `https://ux-curation-newsletter.onrender.com`

---

## 🔐 Se connecter

Quand vos collègues accèdent à l'URL:
1. Une popup demande nom d'utilisateur et mot de passe
2. Entrer les identifiants définis dans `AUTH_USERNAME` et `AUTH_PASSWORD`
3. Ils peuvent maintenant uploader leurs fichiers Excel et générer des newsletters

---

## 🔄 Mettre à jour l'application

```bash
# Faire vos modifications
git add .
git commit -m "Description des changements"
git push origin main
```

Render déploiera automatiquement les changements en 2-3 minutes.

---

## 💡 Astuce pro

Pour désactiver l'authentification (accès libre):
```
ENABLE_AUTH = False
```

---

## ❓ Besoin d'aide ?

Consultez le guide complet: [DEPLOYMENT.md](DEPLOYMENT.md)
