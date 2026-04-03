#!/bin/bash
# Script de téléchargement des images Wikimedia Commons pour Lachapelle

mkdir -p /home/openclawadmin/projets/lachapelle-site-web/images/wikimedia
cd /home/openclawadmin/projets/lachapelle-site-web/images/wikimedia

echo "Téléchargement des images Wikimedia Commons..."
echo "Attente de 2 secondes entre chaque image pour éviter le blocage..."
echo ""

# Images déjà téléchargées (ne pas re-télécharger si > 1000 octets)
[[ -s Lachapelle-Saint-Pierre-eglise-1.jpg && $(stat -c%s Lachapelle-Saint-Pierre-eglise-1.jpg) -gt 1000 ]] && echo "✓ Lachapelle-Saint-Pierre-eglise-1.jpg déjà présent" || curl -sL -o Lachapelle-Saint-Pierre-eglise-1.jpg "https://upload.wikimedia.org/wikipedia/commons/7/75/Lachapelle-Saint-Pierre_%C3%A9glise_1.JPG"
sleep 2

[[ -s Lachapelle-Saint-Pierre-eglise-2.jpg && $(stat -c%s Lachapelle-Saint-Pierre-eglise-2.jpg) -gt 1000 ]] && echo "✓ Lachapelle-Saint-Pierre-eglise-2.jpg déjà présent" || curl -sL -o Lachapelle-Saint-Pierre-eglise-2.jpg "https://upload.wikimedia.org/wikipedia/commons/5/5b/Lachapelle-Saint-Pierre_%C3%A9glise_2.JPG"
sleep 2

# Lachapelle - Église Saint-Pierre (série -1 à -7)
curl -sL -o Lachapelle-eglise-Saint-Pierre-1.jpg "https://upload.wikimedia.org/wikipedia/commons/1/1a/Lachapelle_-_%C3%89glise_Saint-Pierre_-1.JPG" && echo "✓ Lachapelle-eglise-Saint-Pierre-1.jpg" || echo "✗ Lachapelle-eglise-Saint-Pierre-1.jpg"
sleep 2

curl -sL -o Lachapelle-eglise-Saint-Pierre-2.jpg "https://upload.wikimedia.org/wikipedia/commons/6/62/Lachapelle_-_%C3%89glise_Saint-Pierre_-2.JPG" && echo "✓ Lachapelle-eglise-Saint-Pierre-2.jpg" || echo "✗ Lachapelle-eglise-Saint-Pierre-2.jpg"
sleep 2

curl -sL -o Lachapelle-eglise-Saint-Pierre-4.jpg "https://upload.wikimedia.org/wikipedia/commons/a/a6/Lachapelle_-_%C3%89glise_Saint-Pierre_-4.JPG" && echo "✓ Lachapelle-eglise-Saint-Pierre-4.jpg" || echo "✗ Lachapelle-eglise-Saint-Pierre-4.jpg"
sleep 2

curl -sL -o Lachapelle-eglise-Saint-Pierre-6.jpg "https://upload.wikimedia.org/wikipedia/commons/9/95/Lachapelle_-_%C3%89glise_Saint-Pierre_-6.JPG" && echo "✓ Lachapelle-eglise-Saint-Pierre-6.jpg" || echo "✗ Lachapelle-eglise-Saint-Pierre-6.jpg"
sleep 2

curl -sL -o Lachapelle-eglise-Saint-Pierre-7.jpg "https://upload.wikimedia.org/wikipedia/commons/8/89/Lachapelle_-_%C3%89glise_Saint-Pierre_-7.JPG" && echo "✓ Lachapelle-eglise-Saint-Pierre-7.jpg" || echo "✗ Lachapelle-eglise-Saint-Pierre-7.jpg"
sleep 2

# Série Église de Lachapelle 2021 (01 à 16)
curl -sL -o eglise-2021-01-choeur-autel.jpg "https://upload.wikimedia.org/wikipedia/commons/c/c6/%C3%89glise_de_Lachapelle_2021_01_-_Ch%C5%93ur_et_autel.jpg" && echo "✓ eglise-2021-01-choeur-autel.jpg" || echo "✗ eglise-2021-01-choeur-autel.jpg"
sleep 2

curl -sL -o eglise-2021-02-tableau-plafond.jpg "https://upload.wikimedia.org/wikipedia/commons/5/54/%C3%89glise_de_Lachapelle_2021_02_-_Tableau_et_plafond.jpg" && echo "✓ eglise-2021-02-tableau-plafond.jpg" || echo "✗ eglise-2021-02-tableau-plafond.jpg"
sleep 2

curl -sL -o eglise-2021-03-lutrin.jpg "https://upload.wikimedia.org/wikipedia/commons/c/c9/%C3%89glise_de_Lachapelle_2021_03_-_Lutrin.jpg" && echo "✓ eglise-2021-03-lutrin.jpg" || echo "✗ eglise-2021-03-lutrin.jpg"
sleep 2

curl -sL -o eglise-2021-04-tableau.jpg "https://upload.wikimedia.org/wikipedia/commons/4/4a/%C3%89glise_de_Lachapelle_2021_04_-_Tableau.jpg" && echo "✓ eglise-2021-04-tableau.jpg" || echo "✗ eglise-2021-04-tableau.jpg"
sleep 2

curl -sL -o eglise-2021-05-chaire.jpg "https://upload.wikimedia.org/wikipedia/commons/6/62/%C3%89glise_de_Lachapelle_2021_05_-_Chaire.jpg" && echo "✓ eglise-2021-05-chaire.jpg" || echo "✗ eglise-2021-05-chaire.jpg"
sleep 2

curl -sL -o eglise-2021-06-escalier.jpg "https://upload.wikimedia.org/wikipedia/commons/3/34/%C3%89glise_de_Lachapelle_2021_06_-_Escalier_et_entr%C3%A9e.jpg" && echo "✓ eglise-2021-06-escalier.jpg" || echo "✗ eglise-2021-06-escalier.jpg"
sleep 2

curl -sL -o eglise-2021-07-statues.jpg "https://upload.wikimedia.org/wikipedia/commons/f/f8/%C3%89glise_de_Lachapelle_2021_07_-_Statues.jpg" && echo "✓ eglise-2021-07-statues.jpg" || echo "✗ eglise-2021-07-statues.jpg"
sleep 2

curl -sL -o eglise-2021-08-harmonium.jpg "https://upload.wikimedia.org/wikipedia/commons/8/8c/%C3%89glise_de_Lachapelle_2021_08_-_Harmonium.jpg" && echo "✓ eglise-2021-08-harmonium.jpg" || echo "✗ eglise-2021-08-harmonium.jpg"
sleep 2

curl -sL -o eglise-2021-09-vitrail.jpg "https://upload.wikimedia.org/wikipedia/commons/4/45/%C3%89glise_de_Lachapelle_2021_09_-_Vitrail.jpg" && echo "✓ eglise-2021-09-vitrail.jpg" || echo "✗ eglise-2021-09-vitrail.jpg"
sleep 2

curl -sL -o eglise-2021-10-choeur.jpg "https://upload.wikimedia.org/wikipedia/commons/a/a2/%C3%89glise_de_Lachapelle_2021_10_-_Ch%C5%93ur.jpg" && echo "✓ eglise-2021-10-choeur.jpg" || echo "✗ eglise-2021-10-choeur.jpg"
sleep 2

curl -sL -o eglise-2021-11-tribune.jpg "https://upload.wikimedia.org/wikipedia/commons/1/15/%C3%89glise_de_Lachapelle_2021_11_-_Tribune.jpg" && echo "✓ eglise-2021-11-tribune.jpg" || echo "✗ eglise-2021-11-tribune.jpg"
sleep 2

curl -sL -o eglise-2021-12-fonts-baptismaux.jpg "https://upload.wikimedia.org/wikipedia/commons/a/a8/%C3%89glise_de_Lachapelle_2021_12_-_Fonts_baptismaux.jpg" && echo "✓ eglise-2021-12-fonts-baptismaux.jpg" || echo "✗ eglise-2021-12-fonts-baptismaux.jpg"
sleep 2

curl -sL -o eglise-2021-13-creche.jpg "https://upload.wikimedia.org/wikipedia/commons/a/a7/%C3%89glise_de_Lachapelle_2021_13_-_Cr%C3%A8che.jpg" && echo "✓ eglise-2021-13-creche.jpg" || echo "✗ eglise-2021-13-creche.jpg"
sleep 2

curl -sL -o eglise-2021-14-haut-tribune.jpg "https://upload.wikimedia.org/wikipedia/commons/9/99/%C3%89glise_de_Lachapelle_2021_14_-_Haut_de_la_tribune.jpg" && echo "✓ eglise-2021-14-haut-tribune.jpg" || echo "✗ eglise-2021-14-haut-tribune.jpg"
sleep 2

curl -sL -o eglise-2021-15-portail.jpg "https://upload.wikimedia.org/wikipedia/commons/1/15/%C3%89glise_de_Lachapelle_2021_15_-_Portail.jpg" && echo "✓ eglise-2021-15-portail.jpg" || echo "✗ eglise-2021-15-portail.jpg"
sleep 2

curl -sL -o eglise-2021-16-porche.jpg "https://upload.wikimedia.org/wikipedia/commons/5/59/%C3%89glise_de_Lachapelle_2021_16_-_Porche.jpg" && echo "✓ eglise-2021-16-porche.jpg" || echo "✗ eglise-2021-16-porche.jpg"

echo ""
echo "=========================================="
echo "Téléchargement terminé !"
echo "Images dans: images/wikimedia/"
echo "=========================================="
ls -lh /home/openclawadmin/projets/lachapelle-site-web/images/wikimedia/
