"""
Application Flask pour générer des newsletters HTML depuis des fichiers Excel
"""
from flask import Flask, render_template, request, send_file, jsonify, redirect, url_for
from werkzeug.utils import secure_filename
import os
import zipfile
from io import BytesIO
from datetime import datetime
from excel_parser import NewsletterExcelParser
from html_generator import NewsletterHTMLGenerator
from auth import requires_auth

# Configuration de l'application
app = Flask(__name__)

# Variables d'environnement pour la production
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'output'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limite à 16MB

# Extensions de fichiers autorisées
ALLOWED_EXTENSIONS = {'xls', 'xlsx'}

# Créer les dossiers nécessaires
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)


def allowed_file(filename):
    """Vérifie si le fichier a une extension autorisée."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
@requires_auth
def index():
    """Page d'accueil avec le formulaire d'upload."""
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
@requires_auth
def upload_file():
    """
    Traite l'upload du fichier Excel et génère la newsletter.
    """
    try:
        # Vérifier qu'un fichier a été envoyé
        if 'excel_file' not in request.files:
            return jsonify({'error': 'Aucun fichier fourni'}), 400

        file = request.files['excel_file']

        # Vérifier que le fichier a un nom
        if file.filename == '':
            return jsonify({'error': 'Aucun fichier sélectionné'}), 400

        # Vérifier l'extension
        if not allowed_file(file.filename):
            return jsonify({'error': 'Format de fichier non autorisé. Utilisez .xls ou .xlsx'}), 400

        # Récupérer la date de la newsletter (optionnelle)
        newsletter_date = request.form.get('newsletter_date', '')
        if not newsletter_date:
            newsletter_date = datetime.now().strftime("%B %Y")

        # Sauvegarder le fichier uploadé
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{timestamp}_{filename}")
        file.save(upload_path)

        # Parser le fichier Excel
        parser = NewsletterExcelParser(upload_path)
        resources = parser.parse()

        if not resources:
            return jsonify({'error': 'Aucune ressource trouvée dans le fichier Excel'}), 400

        # Générer le HTML
        generator = NewsletterHTMLGenerator()
        output_filename = f"newsletter_{timestamp}.html"
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)

        html_content = generator.generate(
            resources=resources,
            newsletter_date=newsletter_date,
            output_path=output_path
        )

        # Générer les statistiques
        stats = generator.generate_stats(resources)

        # Retourner les informations
        return jsonify({
            'success': True,
            'message': 'Newsletter générée avec succès!',
            'output_file': output_filename,
            'stats': stats,
            'download_url': url_for('download_file', filename=output_filename)
        })

    except Exception as e:
        return jsonify({'error': f'Erreur lors de la génération: {str(e)}'}), 500


@app.route('/download/<filename>')
def download_file(filename):
    """
    Télécharge le fichier HTML généré dans un fichier ZIP.
    """
    try:
        file_path = os.path.join(app.config['OUTPUT_FOLDER'], filename)

        # Créer un fichier ZIP en mémoire
        memory_file = BytesIO()
        with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zf:
            # Ajouter le fichier HTML au ZIP avec un nom propre
            zf.write(file_path, arcname=filename)

        # Repositionner le curseur au début du fichier
        memory_file.seek(0)

        # Nom du fichier ZIP (remplacer .html par .zip)
        zip_filename = filename.replace('.html', '.zip')

        return send_file(
            memory_file,
            mimetype='application/zip',
            as_attachment=True,
            download_name=zip_filename
        )
    except FileNotFoundError:
        return jsonify({'error': 'Fichier introuvable'}), 404


@app.route('/preview/<filename>')
def preview_file(filename):
    """
    Affiche un aperçu du fichier HTML généré.
    """
    try:
        file_path = os.path.join(app.config['OUTPUT_FOLDER'], filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        return html_content
    except FileNotFoundError:
        return jsonify({'error': 'Fichier introuvable'}), 404


@app.route('/history')
def history():
    """
    Liste toutes les newsletters générées.
    """
    try:
        files = []
        for filename in os.listdir(app.config['OUTPUT_FOLDER']):
            if filename.endswith('.html'):
                file_path = os.path.join(app.config['OUTPUT_FOLDER'], filename)
                file_stat = os.stat(file_path)
                files.append({
                    'filename': filename,
                    'size': file_stat.st_size,
                    'created': datetime.fromtimestamp(file_stat.st_ctime).strftime("%d/%m/%Y %H:%M"),
                    'download_url': url_for('download_file', filename=filename),
                    'preview_url': url_for('preview_file', filename=filename)
                })

        # Trier par date de création (plus récent en premier)
        files.sort(key=lambda x: x['created'], reverse=True)

        return jsonify({'files': files})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.errorhandler(413)
def request_entity_too_large(error):
    """Gestion de l'erreur de fichier trop volumineux."""
    return jsonify({'error': 'Fichier trop volumineux (limite: 16MB)'}), 413


if __name__ == '__main__':
    # Configuration pour le développement local
    port = int(os.environ.get('PORT', 5001))
    debug = os.environ.get('FLASK_DEBUG', 'True') == 'True'

    print("\n" + "="*60)
    print("🚀 UX Curation - Générateur de Newsletter")
    print("="*60)
    print(f"\n📝 Accédez à l'application sur: http://localhost:{port}")
    print("💡 Pour arrêter le serveur: Ctrl+C\n")

    app.run(debug=debug, host='0.0.0.0', port=port)
