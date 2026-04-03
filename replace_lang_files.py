#!/usr/bin/env python3
"""
Script pour copier la page 'en construction' vers tous les fichiers HTML 
dans les dossiers /en/, /de/, /nl/ au cas où l'utilisateur accède directement
à une page spécifique (pas seulement index.html).
"""

import os
import shutil

# Dossiers de langues à traiter
lang_folders = ['en', 'de', 'nl']

# Le fichier template
construction_template = 'under-construction.html'

def replace_html_files():
    if not os.path.exists(construction_template):
        print(f"Erreur: {construction_template} n'existe pas")
        return False
    
    for folder in lang_folders:
        folder_path = folder
        if not os.path.isdir(folder_path):
            print(f"Dossier non trouvé: {folder_path}")
            continue
        
        for filename in os.listdir(folder_path):
            if filename.endswith('.html'):
                file_path = os.path.join(folder_path, filename)
                try:
                    shutil.copy(construction_template, file_path)
                    print(f"✓ Remplacé: {folder}/{filename}")
                except Exception as e:
                    print(f"✗ Erreur {folder}/{filename}: {e}")
    
    return True

if __name__ == '__main__':
    print("Remplacement des fichiers HTML dans les dossiers de langues par 'en construction'...")
    print("=" * 70)
    replace_html_files()
    print("=" * 70)
    print("\nTous les fichiers HTML dans /en/, /de/, /nl/ pointent maintenant vers 'en construction'.")
    print("Redirection automatique vers la version FR en 3 secondes.")
