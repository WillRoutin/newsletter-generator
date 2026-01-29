"""
Module pour générer le HTML de la newsletter à partir des ressources parsées
"""
from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime
from typing import List, Dict, Any
import os


class NewsletterHTMLGenerator:
    """
    Génère le HTML d'une newsletter à partir de ressources structurées.

    Utilise Jinja2 pour le templating et produit un HTML compatible avec
    les clients email (Mailchimp, etc.)
    """

    def __init__(self, template_dir: str = 'templates'):
        """
        Initialise le générateur avec le répertoire des templates.

        Args:
            template_dir: Chemin vers le dossier contenant les templates
        """
        self.template_dir = template_dir

        # Configuration de Jinja2
        self.env = Environment(
            loader=FileSystemLoader(template_dir),
            autoescape=select_autoescape(['html', 'xml'])
        )

        # Charger le template principal
        self.template = self.env.get_template('newsletter.html')

    def generate(
        self,
        resources: List[Dict[str, Any]],
        newsletter_date: str = None,
        output_path: str = None
    ) -> str:
        """
        Génère le HTML de la newsletter.

        Args:
            resources: Liste des ressources parsées depuis Excel
            newsletter_date: Date de la newsletter (format texte)
            output_path: Chemin où sauvegarder le HTML (optionnel)

        Returns:
            Le code HTML généré
        """
        # Si pas de date fournie, utiliser la date du jour
        if newsletter_date is None:
            newsletter_date = datetime.now().strftime("%B %Y")

        # Organiser les ressources par type pour un meilleur ordre
        ordered_resources = self._order_resources(resources)

        # Rendre le template avec les données
        html_content = self.template.render(
            resources=ordered_resources,
            date=newsletter_date,
            generation_date=datetime.now().strftime("%d/%m/%Y à %H:%M")
        )

        # Sauvegarder si un chemin est fourni
        if output_path:
            self._save_html(html_content, output_path)
            print(f"✓ Newsletter générée : {output_path}")

        return html_content

    def _order_resources(self, resources: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Ordonne les ressources selon l'ordre logique de la newsletter.

        Ordre: introduction → ressource en vedette → ressources → vidéothèque → événements

        Args:
            resources: Liste des ressources non ordonnées

        Returns:
            Liste des ressources ordonnées
        """
        type_order = {
            'introduction': 0,
            'ressource en vedette': 1,
            'ressources': 2,
            'vidéothèque': 3,
            'événements': 4
        }

        def get_order(resource):
            resource_type = resource.get('type', '').lower()
            return type_order.get(resource_type, 999)

        return sorted(resources, key=get_order)

    def _save_html(self, html_content: str, output_path: str) -> None:
        """
        Sauvegarde le contenu HTML dans un fichier.

        Args:
            html_content: Le contenu HTML à sauvegarder
            output_path: Chemin du fichier de sortie
        """
        # Créer le dossier de sortie si nécessaire
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Écrire le fichier
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

    def generate_stats(self, resources: List[Dict[str, Any]]) -> Dict[str, int]:
        """
        Génère des statistiques sur les ressources.

        Args:
            resources: Liste des ressources

        Returns:
            Dictionnaire avec le nombre de ressources par type
        """
        stats = {
            'total': len(resources),
            'introduction': 0,
            'ressource_en_vedette': 0,
            'ressources': 0,
            'videotheque': 0,
            'evenements': 0
        }

        for resource in resources:
            resource_type = resource.get('type', '').lower()
            if resource_type == 'introduction':
                stats['introduction'] += 1
            elif resource_type == 'ressource en vedette':
                stats['ressource_en_vedette'] += 1
            elif resource_type == 'ressources':
                stats['ressources'] += 1
            elif resource_type == 'vidéothèque':
                stats['videotheque'] += 1
            elif resource_type == 'événements':
                stats['evenements'] += 1

        return stats


def test_generator():
    """
    Fonction de test pour vérifier le générateur HTML.
    """
    from excel_parser import NewsletterExcelParser

    # Parser le fichier Excel d'exemple
    parser = NewsletterExcelParser('examples/exemple.xlsx')
    resources = parser.parse()

    # Générer la newsletter
    generator = NewsletterHTMLGenerator()
    html = generator.generate(
        resources=resources,
        newsletter_date="Janvier 2025",
        output_path="output/newsletter_test.html"
    )

    # Afficher les stats
    stats = generator.generate_stats(resources)
    print(f"\n📊 Statistiques de la newsletter:")
    print(f"  Total de ressources: {stats['total']}")
    print(f"  - Introduction: {stats['introduction']}")
    print(f"  - Ressource en vedette: {stats['ressource_en_vedette']}")
    print(f"  - Ressources: {stats['ressources']}")
    print(f"  - Vidéothèque: {stats['videotheque']}")
    print(f"  - Événements: {stats['evenements']}")

    print(f"\n✅ Test réussi ! Ouvrez le fichier output/newsletter_test.html dans votre navigateur.")


if __name__ == '__main__':
    test_generator()
