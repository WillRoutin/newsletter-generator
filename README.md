# 📧 UX Curation - Générateur de Newsletter

Un outil puissant et élégant pour transformer vos fichiers Excel en newsletters HTML professionnelles, prêtes à être intégrées dans Mailchimp ou d'autres outils d'emailing.

## ✨ Fonctionnalités

- **Upload de fichiers Excel** (.xls, .xlsx) via une interface web moderne
- **Génération automatique de HTML/CSS** compatible avec les clients email
- **Design responsive** qui s'adapte aux mobiles et tablettes
- **Support de multiples types de ressources**:
  - Introduction
  - Ressource en vedette
  - Ressources standards
  - Vidéothèque
  - Événements
- **Statistiques détaillées** sur les ressources
- **Aperçu en direct** de la newsletter générée
- **Téléchargement direct** du fichier HTML

## 🚀 Installation

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de packages Python)

### Étapes d'installation

1. **Cloner ou télécharger le projet**
   ```bash
   cd newsletter-generator
   ```

2. **Créer un environnement virtuel**
   ```bash
   python3 -m venv venv
   ```

3. **Activer l'environnement virtuel**
   - Sur macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - Sur Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

## 📋 Structure du fichier Excel

Votre fichier Excel doit contenir les colonnes suivantes:

| Colonne | Description | Obligatoire |
|---------|-------------|-------------|
| Type de ressource | Type: introduction, ressource en vedette, ressources, vidéothèque, événements | ✅ Oui |
| Image | URL de l'image (sauf pour introduction et événements) | ⚠️ Selon le type |
| Titre de la ressource | Titre de la ressource (sauf pour introduction) | ⚠️ Selon le type |
| Description de la ressource | Description détaillée | ⚠️ Selon le type |
| Lien | URL de la ressource | ⚠️ Selon le type |
| Date | Date de l'événement (uniquement pour événements) | ⚠️ Pour événements |
| Horaire | Horaire (uniquement pour événements) | ⚠️ Pour événements |
| Localité | En ligne ou ville (uniquement pour événements) | ⚠️ Pour événements |
| Prix | Gratuit ou montant (uniquement pour événements) | ⚠️ Pour événements |
| Langue | Français/Anglais (uniquement pour événements) | ⚠️ Pour événements |

### Particularités par type de ressource

#### Introduction
- **Colonnes utilisées**: Type, Description
- **Description**: Texte d'introduction de la newsletter

#### Ressource en vedette
- **Colonnes utilisées**: Type, Image, Titre, Description, Lien
- **Description**: La ressource principale mise en avant

#### Ressources / Vidéothèque
- **Colonnes utilisées**: Type, Image, Titre, Description, Lien
- **Description**: Ressources ou vidéos standards

#### Événements
- **Colonnes utilisées**: Type, Titre, Lien, Date, Horaire, Localité, Prix, Langue
- **Description**: Événements à venir (pas d'image ni de description)

## 🎯 Utilisation

### Méthode 1: Interface Web (Recommandé)

1. **Lancer l'application Flask**
   ```bash
   source venv/bin/activate  # Activer l'environnement virtuel
   python app.py
   ```

2. **Ouvrir votre navigateur**
   - Accéder à: http://localhost:5000

3. **Utiliser l'interface**
   - Entrer la date de la newsletter (optionnel)
   - Glisser-déposer ou cliquer pour sélectionner votre fichier Excel
   - Cliquer sur "Générer la newsletter"
   - Télécharger ou prévisualiser le résultat

### Méthode 2: Ligne de commande

```python
from excel_parser import NewsletterExcelParser
from html_generator import NewsletterHTMLGenerator

# Parser le fichier Excel
parser = NewsletterExcelParser('chemin/vers/votre/fichier.xlsx')
resources = parser.parse()

# Générer la newsletter HTML
generator = NewsletterHTMLGenerator()
html = generator.generate(
    resources=resources,
    newsletter_date="Janvier 2025",
    output_path="output/ma_newsletter.html"
)

print("Newsletter générée avec succès!")
```

## 📁 Structure du projet

```
newsletter-generator/
│
├── app.py                      # Application Flask
├── excel_parser.py             # Parser de fichiers Excel
├── html_generator.py           # Générateur HTML/CSS
├── requirements.txt            # Dépendances Python
├── create_example_excel.py     # Script pour créer un fichier d'exemple
│
├── templates/                  # Templates Jinja2
│   ├── newsletter.html         # Template de newsletter
│   └── index.html              # Interface web
│
├── static/                     # Fichiers statiques
│   └── email-styles.css        # Styles CSS (référence)
│
├── examples/                   # Fichiers d'exemple
│   └── exemple.xlsx            # Fichier Excel d'exemple
│
├── output/                     # Newsletters générées
│
└── uploads/                    # Fichiers Excel uploadés
```

## 🎨 Personnalisation

### Modifier le design

Le fichier [templates/newsletter.html](templates/newsletter.html) contient le template principal. Vous pouvez:

- Modifier les couleurs dans la section `<style>`
- Changer la typographie
- Ajuster les espacements
- Modifier le dégradé du header
- Personnaliser les sections

### Couleurs principales

```css
--primary-color: #2563eb;        /* Bleu principal */
--secondary-color: #1e293b;      /* Gris foncé */
--text-color: #334155;           /* Texte standard */
--border-color: #e2e8f0;         /* Bordures */
--bg-light: #f8fafc;             /* Fond clair */
```

## 🧪 Tester avec l'exemple

Un fichier Excel d'exemple est fourni pour tester l'outil:

```bash
# Générer l'exemple
python create_example_excel.py

# Tester le générateur
python html_generator.py
```

Le fichier généré sera disponible dans `output/newsletter_test.html`

## 📤 Intégration avec Mailchimp

1. Générer votre newsletter HTML
2. Ouvrir le fichier HTML généré
3. Copier tout le code HTML (Ctrl+A, Ctrl+C)
4. Dans Mailchimp:
   - Créer une nouvelle campagne
   - Choisir "Code your own" ou "Paste in code"
   - Coller votre code HTML
   - Tester l'envoi

## 🛠️ Dépannage

### Erreur: "Module not found: pandas"
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Erreur: "Port 5000 already in use"
Modifier le port dans [app.py](app.py):
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Changer 5000 en 5001
```

### Les images ne s'affichent pas
Vérifier que les URLs des images dans votre fichier Excel sont:
- Complètes (commencent par http:// ou https://)
- Accessibles publiquement
- Pas bloquées par un pare-feu

## 📝 Bonnes pratiques

1. **Images**: Utilisez des URLs d'images hébergées (Imgur, Cloudinary, etc.)
2. **Taille**: Gardez vos images sous 500KB pour un chargement rapide
3. **Texte**: Limitez les descriptions à 2-3 phrases pour plus d'impact
4. **Test**: Toujours tester dans plusieurs clients email avant l'envoi
5. **Backup**: Sauvegardez vos fichiers Excel sources

## 🤝 Contribution

N'hésitez pas à proposer des améliorations:
1. Fork le projet
2. Créer une branche (`git checkout -b feature/amelioration`)
3. Commit vos changements (`git commit -am 'Ajout de fonctionnalité'`)
4. Push vers la branche (`git push origin feature/amelioration`)
5. Créer une Pull Request

## 🌐 Déploiement sur le web

Pour rendre l'application accessible à votre équipe, consultez les guides de déploiement:

- **[Guide de déploiement rapide](QUICK_DEPLOY.md)** - Déployer en 5 minutes sur Render.com
- **[Guide de déploiement complet](DEPLOYMENT.md)** - Toutes les options (Render, Railway, PythonAnywhere, Heroku)

### Déploiement express (Render.com)

```bash
# 1. Initialiser Git
git init && git add . && git commit -m "Initial commit"

# 2. Pousser sur GitHub
git remote add origin https://github.com/VOTRE_USERNAME/newsletter-generator.git
git push -u origin main

# 3. Aller sur render.com → New Web Service → Connecter le repo
# 4. Configurer les variables d'environnement
# 5. Déployer !
```

Votre équipe pourra accéder à l'application via une URL comme:
`https://ux-curation-newsletter.onrender.com`

## 📄 Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, le modifier et le distribuer.

## 🙏 Support

Pour toute question ou problème:
- Ouvrir une issue sur GitHub
- Consulter la documentation
- Vérifier les fichiers d'exemple

---

**Créé avec ❤️ pour les créateurs de contenu UX**

Bon emailing! 🚀
