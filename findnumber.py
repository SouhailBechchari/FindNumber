import re

def contient_chiffres_regex(chaine):
    pattern = re.compile(r'\d')
    return bool(pattern.search(chaine))

# Exemple d'utilisation
chaine_test = "Il fait 25 degrés aujourd'hui."
resultat = contient_chiffres_regex(chaine_test)
print(resultat)  
