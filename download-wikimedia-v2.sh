#!/bin/bash
# Script amélioré avec User-Agent et délai de 5 secondes

USER_AGENT="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

mkdir -p /home/openclawadmin/projets/lachapelle-site-web/images/wikimedia
cd /home/openclawadmin/projets/lachapelle-site-web/images/wikimedia

echo "Téléchargement avec User-Agent et délai de 5 secondes..."
echo ""

# Fonction pour télécharger avec vérification
download_file() {
    local url=$1
    local output=$2
    
    # Vérifier si déjà présent et valide (> 100Ko)
    if [[ -f "$output" && $(stat -c%s "$output" 2>/dev/null) -gt 100000 ]]; then
        echo "✓ $output déjà présent ($(du -h "$output" | cut -f1))"
        return 0
    fi
    
    echo "⏳ Téléchargement: $output..."
    curl -sL \
        -A "$USER_AGENT" \
        --fail \
        -o "$output" \
        "$url"
    
    # Vérifier le résultat
    if [[ -f "$output" ]]; then
        size=$(stat -c%s "$output" 2>/dev/null || echo 0)
        if [[ $size -gt 50000 ]]; then
            echo "  ✓ OK ($(du -h "$output" | cut -f1))"
            return 0
        else
            echo "  ✗ Fichier trop petit ($size octets)"
            rm -f "$output"
            return 1
        fi
    else
        echo "  ✗ Échec"
        return 1
    fi
}

# Images à télécharger (série Église de Lachapelle 2021)
declare -a IMAGES=(
    "https://upload.wikimedia.org/wikipedia/commons/c/c6/%C3%89glise_de_Lachapelle_2021_01_-_Ch%C5%93ur_et_autel.jpg:eglise-2021-01-choeur-autel.jpg"
    "https://upload.wikimedia.org/wikipedia/commons/5/54/%C3%89glise_de_Lachapelle_2021_02_-_Tableau_et_plafond.jpg:eglise-2021-02-tableau-plafond.jpg"
    "https://upload.wikimedia.org/wikipedia/commons/c/c9/%C3%89glise_de_Lachapelle_2021_03_-_Lutrin.jpg:eglise-2021-03-lutrin.jpg"
    "https://upload.wikimedia.org/wikipedia/commons/4/4a/%C3%89glise_de_Lachapelle_2021_04_-_Tableau.jpg:eglise-2021-04-tableau.jpg"
    "https://upload.wikimedia.org/wikipedia/commons/6/62/%C3%89glise_de_Lachapelle_2021_05_-_Chaire.jpg:eglise-2021-05-chaire.jpg"
    "https://upload.wikimedia.org/wikipedia/commons/3/34/%C3%89glise_de_Lachapelle_2021_06_-_Escalier_et_entr%C3%A9e.jpg:eglise-2021-06-escalier.jpg"
    "https://upload.wikimedia.org/wikipedia/commons/f/f8/%C3%89glise_de_Lachapelle_2021_07_-_Statues.jpg:eglise-2021-07-statues.jpg"
    "https://upload.wikimedia.org/wikipedia/commons/8/8c/%C3%89glise_de_Lachapelle_2021_08_-_Harmonium.jpg:eglise-2021-08-harmonium.jpg"
    "https://upload.wikimedia.org/wikipedia/commons/4/45/%C3%89glise_de_Lachapelle_2021_09_-_Vitrail.jpg:eglise-2021-09-vitrail.jpg"
    "https://upload.wikimedia.org/wikipedia/commons/a/a2/%C3%89glise_de_Lachapelle_2021_10_-_Ch%C5%93ur.jpg:eglise-2021-10-choeur.jpg"
    "https://upload.wikimedia.org/wikipedia/commons/1/15/%C3%89glise_de_Lachapelle_2021_11_-_Tribune.jpg:eglise-2021-11-tribune.jpg"
    "https://upload.wikimedia.org/wikipedia/commons/a/a8/%C3%89glise_de_Lachapelle_2021_12_-_Fonts_baptismaux.jpg:eglise-2021-12-fonts-baptismaux.jpg"
    "https://upload.wikimedia.org/wikipedia/commons/a/a7/%C3%89glise_de_Lachapelle_2021_13_-_Cr%C3%A8che.jpg:eglise-2021-13-creche.jpg"
    "https://upload.wikimedia.org/wikipedia/commons/9/99/%C3%89glise_de_Lachapelle_2021_14_-_Haut_de_la_tribune.jpg:eglise-2021-14-haut-tribune.jpg"
    "https://upload.wikimedia.org/wikipedia/commons/1/15/%C3%89glise_de_Lachapelle_2021_15_-_Portail.jpg:eglise-2021-15-portail.jpg"
    "https://upload.wikimedia.org/wikipedia/commons/5/59/%C3%89glise_de_Lachapelle_2021_16_-_Porche.jpg:eglise-2021-16-porche.jpg"
)

success=0
failed=0

for item in "${IMAGES[@]}"; do
    IFS=":" read -r url output <<< "$item"
    
    if download_file "$url" "$output"; then
        ((success++))
    else
        ((failed++))
    fi
    
    # Délai de 5 secondes entre chaque téléchargement
    sleep 5
done

echo ""
echo "=========================================="
echo "RÉSULTAT:"
echo "  ✅ Réussis: $success"
echo "  ❌ Échoués: $failed"
echo "=========================================="
echo ""
echo "Images dans le dossier:"
ls -lhS /home/openclawadmin/projets/lachapelle-site-web/images/wikimedia/