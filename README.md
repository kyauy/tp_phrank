# TP phrank

## Installer un terminal sur votre téléphone

- Installer Termux (Android) disponible sur Google Play Store

## Commande à faire depuis Termux

Installer python = le langage de programmation le plus répandu
Installer git = permet de copier des programmes en ligne sur la plateforme de partage de code github
```
pkg install python
pkg install git
```

Récupérer les datas =

```
git clone https://github.com/kyauy/tp_phrank.git
```

Lancer la ligne de commande :
cd = change directory

```
cd tp_phrank
python phrank.py HP:0001562,HP:0000105,HP:0000113 > test.txt
```

Regarder le resultat : 
```
head test.txt
```
