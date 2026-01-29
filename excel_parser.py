"""
Module pour lire et parser les fichiers Excel contenant les ressources newsletter
"""
import pandas as pd
from typing import List, Dict, Any


class NewsletterExcelParser:
    """
    Parse un fichier Excel contenant des ressources pour newsletter.

    Structure attendue des colonnes :
    - Type de ressource : introduction, ressource en vedette, ressources, vidéothèque, événements
    - Image (lien)
    - Titre de la ressource
    - Description de la ressource
    - Lien

    Colonnes supplémentaires pour les événements :
    - Date
    - Horaire
    - Localité
    - Prix
    - Langue
    """

    # Types de ressources supportés
    RESOURCE_TYPES = [
        'introduction',
        'ressource en vedette',
        'ressources',
        'vidéothèque',
        'événements'
    ]

    def __init__(self, excel_file_path: str):
        """
        Initialise le parser avec le chemin du fichier Excel.

        Args:
            excel_file_path: Chemin vers le fichier Excel (.xls ou .xlsx)
        """
        self.excel_file_path = excel_file_path
        self.data = None

    def parse(self) -> List[Dict[str, Any]]:
        """
        Parse le fichier Excel et retourne une liste de ressources structurées.

        Returns:
            Liste de dictionnaires contenant les données de chaque ressource
        """
        # Lire le fichier Excel
        try:
            self.data = pd.read_excel(self.excel_file_path)
        except Exception as e:
            raise ValueError(f"Erreur lors de la lecture du fichier Excel : {str(e)}")

        # Normaliser les noms de colonnes (enlever espaces, minuscules)
        self.data.columns = self.data.columns.str.strip().str.lower()

        # Convertir en liste de dictionnaires
        resources = []
        for index, row in self.data.iterrows():
            resource = self._parse_row(row, index)
            if resource:  # Ignorer les lignes vides
                resources.append(resource)

        return resources

    def _parse_row(self, row: pd.Series, index: int) -> Dict[str, Any]:
        """
        Parse une ligne du fichier Excel.

        Args:
            row: Une ligne du DataFrame pandas
            index: Numéro de la ligne

        Returns:
            Dictionnaire contenant les données de la ressource
        """
        # Récupérer le type de ressource
        resource_type = self._get_value(row, 'type de ressource')

        # Si pas de type, ignorer la ligne
        if not resource_type:
            return None

        # Normaliser le type de ressource
        resource_type = resource_type.strip().lower()

        # Structure de base
        resource = {
            'type': resource_type,
            'row_number': index + 2  # +2 car Excel commence à 1 et on a une ligne d'en-tête
        }

        # Parser selon le type de ressource
        if resource_type == 'introduction':
            resource.update(self._parse_introduction(row))
        elif resource_type == 'événements':
            resource.update(self._parse_event(row))
        else:
            # ressource en vedette, ressources, vidéothèque
            resource.update(self._parse_standard_resource(row))

        return resource

    def _parse_introduction(self, row: pd.Series) -> Dict[str, Any]:
        """Parse une ressource de type 'introduction'."""
        return {
            'description': self._get_value(row, 'description de la ressource', default='')
        }

    def _parse_event(self, row: pd.Series) -> Dict[str, Any]:
        """Parse une ressource de type 'événements'."""
        return {
            'titre': self._get_value(row, 'titre de la ressource', default=''),
            'lien': self._get_value(row, 'lien', default=''),
            'date': self._get_value(row, 'date', default=''),
            'horaire': self._get_value(row, 'horaire', default=''),
            'localite': self._get_value(row, 'localité', default=''),
            'prix': self._get_value(row, 'prix', default='Gratuit'),
            'langue': self._get_value(row, 'langue', default='Français')
        }

    def _parse_standard_resource(self, row: pd.Series) -> Dict[str, Any]:
        """Parse une ressource standard (vedette, ressources, vidéothèque)."""
        return {
            'image': self._get_value(row, 'image', default=''),
            'titre': self._get_value(row, 'titre de la ressource', default=''),
            'description': self._get_value(row, 'description de la ressource', default=''),
            'lien': self._get_value(row, 'lien', default='')
        }

    def _get_value(self, row: pd.Series, column_name: str, default: str = '') -> str:
        """
        Récupère une valeur d'une colonne en gérant les erreurs et les valeurs nulles.

        Args:
            row: La ligne du DataFrame
            column_name: Nom de la colonne à récupérer
            default: Valeur par défaut si la colonne n'existe pas ou est vide

        Returns:
            La valeur de la colonne ou la valeur par défaut
        """
        try:
            value = row.get(column_name)
            # Gérer les valeurs NaN/None
            if pd.isna(value):
                return default
            return str(value).strip()
        except KeyError:
            return default


def test_parser():
    """Fonction de test pour vérifier le parser."""
    # Cette fonction sera utilisée pour tester avec un fichier Excel d'exemple
    parser = NewsletterExcelParser('examples/exemple.xlsx')
    resources = parser.parse()

    print(f"Nombre de ressources trouvées : {len(resources)}")
    for resource in resources:
        print(f"\nType: {resource['type']}")
        print(f"Données: {resource}")


if __name__ == '__main__':
    test_parser()
