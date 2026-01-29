"""
Script pour créer un fichier Excel d'exemple avec toutes les ressources
"""
import pandas as pd

# Données d'exemple pour la newsletter
data = {
    'Type de ressource': [
        'introduction',
        'ressource en vedette',
        'ressources',
        'ressources',
        'vidéothèque',
        'événements',
        'événements'
    ],
    'Image': [
        '',  # introduction n'a pas d'image
        'https://example.com/image-vedette.jpg',
        'https://example.com/image1.jpg',
        'https://example.com/image2.jpg',
        'https://example.com/video-thumbnail.jpg',
        '',  # événements n'ont pas d'image
        ''
    ],
    'Titre de la ressource': [
        '',  # introduction n'a pas de titre
        'IA et Design : Les nouvelles tendances 2025',
        'Guide complet du design system',
        'Les meilleures pratiques UX en 2025',
        'Conférence : L\'avenir du web design',
        'Workshop Design Thinking',
        'Meetup UX Paris'
    ],
    'Description de la ressource': [
        'Bienvenue dans cette édition de notre newsletter ! Ce mois-ci, nous explorons les tendances du design et du développement web. Découvrez nos sélections de ressources, événements et vidéos incontournables.',
        'Un article complet qui explore comment l\'intelligence artificielle transforme les pratiques du design moderne. Découvrez les outils, les méthodologies et les cas d\'usage concrets.',
        'Apprenez à créer un design system robuste et scalable pour vos projets. Ce guide couvre tous les aspects essentiels.',
        'Découvrez les dernières pratiques en expérience utilisateur pour créer des interfaces intuitives et performantes.',
        'Une vidéo fascinante sur les évolutions du web design avec des exemples concrets et des démonstrations.',
        '',  # événements n'ont pas de description
        ''
    ],
    'Lien': [
        '',  # introduction n'a pas de lien
        'https://example.com/article-ia-design',
        'https://example.com/guide-design-system',
        'https://example.com/ux-best-practices',
        'https://youtube.com/watch?v=example',
        'https://example.com/workshop-design-thinking',
        'https://example.com/meetup-ux-paris'
    ],
    'Date': [
        '',
        '',
        '',
        '',
        '',
        '15 février 2025',
        '22 février 2025'
    ],
    'Horaire': [
        '',
        '',
        '',
        '',
        '',
        '14h00 - 17h00',
        '19h00 - 21h00'
    ],
    'Localité': [
        '',
        '',
        '',
        '',
        '',
        'En ligne',
        'Paris, France'
    ],
    'Prix': [
        '',
        '',
        '',
        '',
        '',
        'Gratuit',
        '25€'
    ],
    'Langue': [
        '',
        '',
        '',
        '',
        '',
        'Français',
        'Français'
    ]
}

# Créer le DataFrame
df = pd.DataFrame(data)

# Sauvegarder en Excel
output_path = 'examples/exemple.xlsx'
df.to_excel(output_path, index=False, engine='openpyxl')

print(f"✓ Fichier Excel d'exemple créé : {output_path}")
print(f"  Nombre de ressources : {len(df)}")
print(f"\nStructure du fichier :")
print(f"  - {(df['Type de ressource'] == 'introduction').sum()} introduction")
print(f"  - {(df['Type de ressource'] == 'ressource en vedette').sum()} ressource en vedette")
print(f"  - {(df['Type de ressource'] == 'ressources').sum()} ressources")
print(f"  - {(df['Type de ressource'] == 'vidéothèque').sum()} vidéothèque")
print(f"  - {(df['Type de ressource'] == 'événements').sum()} événements")
