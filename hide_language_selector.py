#!/usr/bin/env python3
"""
Script pour cacher le sélecteur de langue sur toutes les pages FR.
Remplace <div class="nav-language"> par <div class="nav-language" style="display: none !important;">
"""

import os
import re

# Liste des fichiers HTML FR à modifier (racine du site)
files_to_modify = [
    'index.html',
    'histoire.html',
    'decor.html',
    'visite.html',
    'querelle.html',
    'objets-palissy.html',
    'galerie-complete.html',
    'galerie-images.html',
    'index-full.html',
]

def hide_language_selector(file_path):
    """Cache le sélecteur de langue en ajoutant un style display:none"""
    
    if not os.path.exists(file_path):
        print(f"Fichier non trouvé: {file_path}")
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Pattern: <div class="nav-language"> (peut avoir d'autres attributs avant ou après)
    # On capture tout le div d'ouverture
    pattern = r'(<div class="nav-language")([^\u003e]*)(>)'
    
    def replacer(match):
        div_start = match.group(1)
        existing_attrs = match.group(2)
        end_bracket = match.group(3)
        
        # Vérifier s'il y a déjà un style
        if 'style=' in existing_attrs:
            # S'il y a déjà un style, vérifier si notre display:none est déjà là
            if 'display: none !important' in existing_attrs:
                return match.group(0)  # Déjà caché, ne rien faire
            else:
                # Ajouter display:none au style existant
                return re.sub(
                    r'style="([^"]*)"',
                    r'style="display: none !important; \1"',
                    match.group(0)
                )
        else:
            # Pas de style, on ajoute le style display:none
            return f'{div_start}{existing_attrs} style="display: none !important;"{end_bracket}'
    
    content = re.sub(pattern, replacer, content)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Modifié: {file_path}")
        return True
    else:
        print(f"- Aucun changement: {file_path}")
        return False

def main():
    base_dir = '.'
    modified_count = 0
    
    print("Masquage des sélecteurs de langue sur les pages FR...")
    print("=" * 60)
    
    for filename in files_to_modify:
        file_path = os.path.join(base_dir, filename)
        if hide_language_selector(file_path):
            modified_count += 1
    
    print("=" * 60)
    print(f"Total: {modified_count} fichiers modifiés")
    print("\nLes sélecteurs de langue sont maintenant cachés sur toutes les pages FR.")
    print("Pour les réactiver, retirer le style='display: none !important;' des divs .nav-language")

if __name__ == '__main__':
    main()
