#!/usr/bin/env python3
"""
Script pour corriger TOUS les liens internes dans les pages traduites.
"""

import os
import re
from pathlib import Path

# Les traductions des noms de fichiers entre langues
LINK_MAPPING = {
    # FR -> traductions
    'histoire.html': {'en': 'history.html', 'nl': 'history.html', 'de': 'history.html'},
    'decor.html': {'en': 'decor.html', 'nl': 'decor.html', 'de': 'decor.html'},
    'querelle.html': {'en': 'dispute.html', 'nl': 'dispute.html', 'de': 'dispute.html'},
    'visite.html': {'en': 'visit.html', 'nl': 'visit.html', 'de': 'visit.html'},
}

def get_lang(filepath):
    """Détecte la langue."""
    if 'en/' in filepath:
        return 'en'
    if 'nl/' in filepath:
        return 'nl'
    if 'de/' in filepath:
        return 'de'
    return 'fr'

def fix_file(filepath):
    """Corrige les liens dans un fichier."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    lang = get_lang(filepath)
    
    if lang == 'fr':
        return False
    
    # Remplacer les liens vers les pages FR vers les versions traduites
    for fr_file, translations in LINK_MAPPING.items():
        target = translations[lang]
        # Pattern: href="histoire.html" -> remplace par le bon fichier
        content = content.replace(f'href="{fr_file}"', f'href="{target}"')
        content = content.replace(f'href="{fr_file}#', f'href="{target}#')
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    base_dir = Path('/home/openclawadmin/projets/lachapelle-site-web')
    
    # Tous les fichiers dans en/, nl/, de/
    files = []
    for lang in ['en', 'nl', 'de']:
        lang_dir = base_dir / lang
        for f in lang_dir.glob('*.html'):
            files.append(f)
    
    modified = 0
    for filepath in files:
        if fix_file(str(filepath)):
            print(f"✓ Corrigé liens: {filepath.relative_to(base_dir)}")
            modified += 1
    
    print(f"\n{modified} fichiers modifiés")

if __name__ == '__main__':
    main()
