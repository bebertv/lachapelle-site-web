#!/usr/bin/env python3
"""
Script pour corriger les liens internes dans les pages traduites.
Les liens doivent pointer vers les bonnes versions traduites des pages.
"""

import os
import re
from pathlib import Path

# Mapping des pages - chaque langue doit pointer vers sa propre version
PAGE_FILES = {
    'fr': {
        'histoire': 'histoire.html',
        'decor': 'decor.html',
        'querelle': 'querelle.html',
        'visite': 'visite.html',
        'index': 'index.html'
    },
    'en': {
        'histoire': 'history.html',
        'decor': 'decor.html',
        'querelle': 'dispute.html',
        'visite': 'visit.html',
        'index': 'index.html'
    },
    'nl': {
        'histoire': 'history.html',
        'decor': 'decor.html',
        'querelle': 'dispute.html',
        'visite': 'visit.html',
        'index': 'index.html'
    },
    'de': {
        'histoire': 'history.html',
        'decor': 'decor.html',
        'querelle': 'dispute.html',
        'visite': 'visit.html',
        'index': 'index.html'
    }
}

def get_lang_from_path(filepath):
    """Détecte la langue à partir du chemin."""
    if 'en/' in filepath or filepath.endswith('en/'):
        return 'en'
    if 'nl/' in filepath or filepath.endswith('nl/'):
        return 'nl'
    if 'de/' in filepath or filepath.endswith('de/'):
        return 'de'
    return 'fr'

def fix_links_in_file(filepath, lang):
    """Corrige les liens dans un fichier."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Pour les pages non-FR, corriger les liens vers les pages FR vers les versions traduites
    if lang != 'fr':
        # Corriger les liens "En savoir plus" et autres liens dans le contenu
        for page_key in ['histoire', 'decor', 'querelle', 'visite']:
            fr_file = PAGE_FILES['fr'][page_key]
            target_file = PAGE_FILES[lang][page_key]
            
            # Remplacer href="fr.html" par href="target.html"
            pattern = f'href="{fr_file}"'
            replacement = f'href="{target_file}"'
            content = content.replace(pattern, replacement)
        
        # Corriger les liens de dropdown Visiter vers visite.html, visite.html#horaires, visite.html#contact
        # Devraient pointer vers visit.html
        content = content.replace('href="visite.html"', 'href="visit.html"')
        content = content.replace('href="visite.html#horaires"', 'href="visit.html#horaires"')
        content = content.replace('href="visite.html#contact"', 'href="visit.html#contact"')
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    base_dir = Path('/home/openclawadmin/projets/lachapelle-site-web')
    
    # Liste des fichiers à traiter (excluant index.html de la racine et index.html des langues)
    files_to_process = [
        # EN
        'en/history.html',
        'en/decor.html',
        'en/dispute.html',
        'en/visit.html',
        # NL
        'nl/history.html',
        'nl/decor.html',
        'nl/dispute.html',
        'nl/visit.html',
        # DE
        'de/history.html',
        'de/decor.html',
        'de/dispute.html',
        'de/visit.html',
    ]
    
    modified = 0
    for rel_path in files_to_process:
        filepath = base_dir / rel_path
        if filepath.exists():
            lang = get_lang_from_path(str(filepath))
            if fix_links_in_file(str(filepath), lang):
                print(f"✓ Corrigé: {rel_path}")
                modified += 1
            else:
                print(f"- Pas de changement: {rel_path}")
        else:
            print(f"✗ Fichier manquant: {rel_path}")
    
    print(f"\n{modified} fichiers modifiés")

if __name__ == '__main__':
    main()
