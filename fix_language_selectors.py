#!/usr/bin/env python3
"""
Script pour corriger les sélecteurs de langue dans tous les fichiers HTML du site.
Chaque sélecteur doit pointer vers la page correspondante dans les 4 langues.
"""

import os
import re
from pathlib import Path

# Mapping des pages entre les langues
# Clé = concept de page, Valeurs = nom de fichier dans chaque langue
PAGE_MAPPING = {
    'index':     {'fr': 'index.html',    'en': 'index.html',    'nl': 'index.html',    'de': 'index.html'},
    'histoire':  {'fr': 'histoire.html', 'en': 'history.html',  'nl': 'history.html',  'de': 'history.html'},
    'decor':     {'fr': 'decor.html',    'en': 'decor.html',    'nl': 'decor.html',    'de': 'decor.html'},
    'querelle':  {'fr': 'querelle.html', 'en': 'dispute.html',  'nl': 'dispute.html',  'de': 'dispute.html'},
    'visite':    {'fr': 'visite.html',   'en': 'visit.html',    'nl': 'visit.html',    'de': 'visit.html'},
}

# Ordre des langues dans le sélecteur
LANGS = ['fr', 'en', 'nl', 'de']

def detect_page_key(filepath):
    """Détecte la clé de page à partir du chemin et du nom de fichier."""
    filename = os.path.basename(filepath)
    dirname = os.path.dirname(filepath)
    
    # Normalize: si dans un sous-dossier de langue
    lang = None
    for l in ['en', 'nl', 'de']:
        if dirname.endswith(f'/{l}') or f'/{l}/' in dirname or dirname == l:
            lang = l
            break
    
    if lang is None:
        lang = 'fr'  # Racine = français
    
    # Trouver la clé de page correspondante
    for key, mapping in PAGE_MAPPING.items():
        if mapping.get(lang) == filename:
            return key, lang
    
    return None, None

def generate_selector_options(current_key, current_lang):
    """Génère les options du sélecteur de langue pour la page courante."""
    options = []
    
    for lang in LANGS:
        target_file = PAGE_MAPPING[current_key][lang]
        
        if current_lang == 'fr':
            # On est à la racine
            if lang == 'fr':
                path = f"./{target_file}"
            else:
                path = f"./{lang}/{target_file}"
        else:
            # On est dans un sous-dossier (en/, nl/, de/)
            if lang == 'fr':
                path = f"../{target_file}"
            elif lang == current_lang:
                path = f"./{target_file}"
            else:
                path = f"../{lang}/{target_file}"
        
        lang_names = {
            'fr': ('Français', '🇫🇷'),
            'en': ('English', '🇬🇧'),
            'nl': ('Nederlands', '🇳🇱'),
            'de': ('Deutsch', '🇩🇪')
        }
        
        name, flag = lang_names[lang]
        selected = ' selected' if lang == current_lang else ''
        options.append(f'<option value="{path}"{selected}>{name}</option>')
    
    return '\n                '.join(options)

def fix_file(filepath):
    """Corrige le sélecteur de langue dans un fichier."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Erreur lecture {filepath}: {e}")
        return False
    
    # Détecter la clé de page
    key, lang = detect_page_key(filepath)
    if key is None:
        print(f"Page inconnue: {filepath}")
        return False
    
    # Générer les nouvelles options
    new_options = generate_selector_options(key, lang)
    
    # Pattern pour remplacer le sélecteur
    # Cherche tout le bloc select et ses options
    pattern = r'(<select[^>]*onchange="window\.location\.href=this\.value"[^>]*>)(.*?)(</select>)'
    
    def replacer(match):
        return match.group(1) + '\n                ' + new_options + '\n            ' + match.group(3)
    
    new_content = re.sub(pattern, replacer, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✓ Corrigé: {filepath} ({key} en {lang})")
        return True
    else:
        print(f"- Pas de changement: {filepath}")
        return False

def main():
    base_dir = Path('/home/openclawadmin/projets/lachapelle-site-web')
    
    # Liste des fichiers à traiter (ceux qui sont réellement utilisés)
    files_to_process = [
        # FR (racine)
        'index.html',
        'histoire.html',
        'decor.html',
        'querelle.html',
        'visite.html',
        # EN
        'en/index.html',
        'en/history.html',
        'en/decor.html',
        'en/dispute.html',
        'en/visit.html',
        # NL
        'nl/index.html',
        'nl/history.html',
        'nl/decor.html',
        'nl/dispute.html',
        'nl/visit.html',
        # DE
        'de/index.html',
        'de/history.html',
        'de/decor.html',
        'de/dispute.html',
        'de/visit.html',
    ]
    
    modified = 0
    for rel_path in files_to_process:
        filepath = base_dir / rel_path
        if filepath.exists():
            if fix_file(str(filepath)):
                modified += 1
        else:
            print(f"✗ Fichier manquant: {rel_path}")
    
    print(f"\n{modified} fichiers modifiés")

if __name__ == '__main__':
    main()
