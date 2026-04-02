#!/usr/bin/env python3
"""
Script de traduction automatique du contenu historique du site
Via LibreTranslate en local (localhost:5000)

Usage: python translate-content.py
"""

import requests
import re
from pathlib import Path

LOCAL_LIBRE_URL = "http://localhost:5000/translate"
TARGETS = ['en', 'nl', 'de', 'zh']  # Langues cibles

def translate_text(text, target_lang):
    """Traduit via l'instance LibreTranslate locale"""
    text = text.strip()
    if len(text) < 10 or text.startswith('http') or text.isdigit():
        return text  # Skip URLs, nombres, textes courts
    
    try:
        response = requests.post(LOCAL_LIBRE_URL, 
            headers={"Content-Type": "application/json"},
            json={"q": text, "source": "fr", "target": target_lang},
            timeout=30
        )
        if response.status_code == 200:
            return response.json().get('translatedText', text)
        else:
            print(f"  ⚠️ Erreur {response.status_code}: {response.text[:100]}")
    except Exception as e:
        print(f"  ⚠️ Exception: {e}")
    return text

def translate_paragraphs_in_html(html_content, target_lang):
    """Traduit les paragraphes de texte dans le HTML"""
    # Pattern pour trouver les balises <p> avec du texte FR
    pattern = r'<p>([^<]{20,500})</p>'
    
    def replace_paragraph(match):
        text = match.group(1)
        # Skip si déjà traduit (presence de mots anglais/néerlandais courants)
        skip_words = ['the', 'and', 'are', 'you', 'with', 'het', 'een', 'van', 'das', 'die', '的', '是']
        if any(word in text.lower().split() for word in skip_words):
            return match.group(0)
        
        translated = translate_text(text, target_lang)
        return f'<p>{translated}</p>'
    
    # Limite à 20 paragraphes pour éviter de surcharger
    count = 0
    result = html_content
    for match in re.finditer(pattern, html_content):
        if count >= 20:
            break
        original = match.group(0)
        replacement = replace_paragraph(match)
        if original != replacement:
            result = result.replace(original, replacement, 1)
            count += 1
            if count % 5 == 0:
                print(f"  → {count} paragraphes traduits...")
    
    return result, count

def translate_specific_sections():
    """Traduit les sections historiques clés du FR vers EN/NL/DE/ZH"""
    
    base_path = Path('/home/openclawadmin/projets/lachapelle-site-web')
    fr_path = base_path / 'index.html'
    
    with open(fr_path, 'r', encoding='utf-8') as f:
        html_fr = f.read()
    
    print("=" * 60)
    print("Traduction du contenu historique")
    print(f"Source: {fr_path}")
    print("=" * 60)
    
    for lang in TARGETS:
        print(f"\n🌍 Traduction vers {lang.upper()}...")
        target_file = base_path / lang / 'index.html'
        
        # Lire version actuelle
        with open(target_file, 'r', encoding='utf-8') as f:
            html_target = f.read()
        
        # Compter les paragraphes FR restants
        fr_paragraphs = re.findall(r'<p>([^<]{30,})</p>', html_target)
        print(f"   {len(fr_paragraphs)} paragraphes FR détectés")
        
        if len(fr_paragraphs) == 0:
            print(f"   ✓ Déjà traduit, skip")
            continue
        
        # Traduire (limité à 20 par paragraphe pour ne pas surcharger)
        new_html, count = translate_paragraphs_in_html(html_target, lang)
        
        # Sauvegarder
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(new_html)
        
        print(f"   ✓ {count} paragraphes traduits et sauvegardés")
    
    print("\n" + "=" * 60)
    print("Traduction terminée !")
    print("=" * 60)

def translate_specific_phrases():
    """Traduit des phrases spécifiques dures en dur"""
    
    # Dictionnaire de phrases clés à traduire
    phrases = {
        'en': {
            'Les Origines du Village': 'The Origins of the Village',
            'Le Château': 'The Castle',
            'Les Frères Goulard': 'The Goulard Brothers',
            'Un Decor Unique': 'A Unique Decor',
            'La Querelle Religieuse': 'The Religious Dispute',
        },
        'nl': {
            'Les Origines du Village': 'De Oorsprong van het Dorp',
            'Le Château': 'Het Kasteel',
            'Les Frères Goulard': 'De Broers Goulard',
            'Un Decor Unique': 'Een Unieke Decoratie',
            'La Querelle Religieuse': 'Het Religieuze Conflictt',
        },
        'de': {
            'Les Origines du Village': 'Die Ursprünge des Dorfes',
            'Le Château': 'Die Burg',
            'Les Frères Goulard': 'Die Brüder Goulard',
            'Un Decor Unique': 'Eine Einzigartige Ausstattung',
            'La Querelle Religieuse': 'Der Religiöse Streitt',
        },
        'zh': {
            'Les Origines du Village': '村庄的起源',
            'Le Château': '城堡',
            'Les Frères Goulard': '戈拉尔兄弟',
            'Un Decor Unique': '独特的装饰',
            'La Querelle Religieuse': '宗教争议',
        }
    }
    
    base_path = Path('/home/openclawadmin/projets/lachapelle-site-web')
    
    print("\n📝 Application des traductions de titres...")
    for lang, translations in phrases.items():
        target_file = base_path / lang / 'index.html'
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for fr, translated in translations.items():
            if fr in content:
                content = content.replace(fr, translated)
        
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"   ✓ {lang.upper()}: {len(translations)} titres mis à jour")

def check_libretranslate_running():
    """Vérifie que LibreTranslate tourne"""
    try:
        response = requests.get("http://localhost:5000/languages", timeout=5)
        if response.status_code == 200:
            print("✓ LibreTranslate détecté sur localhost:5000")
            return True
    except:
        pass
    print("✗ LibreTranslate non détecté sur localhost:5000")
    print("  → Lancez: libretranslate --host 0.0.0.0 --port 5000")
    return False

if __name__ == '__main__':
    if not check_libretranslate_running():
        exit(1)
    
    translate_specific_phrases()
    translate_specific_sections()
    
    print("\n💡 Pour traduire plus de contenu, relancez ce script plusieurs fois")
    print("   ou modifiez la limite (actuellement 20 paragraphes par section)")
