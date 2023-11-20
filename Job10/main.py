# Initialisation des variables
montant_initial = 10000.0
taux_rendement = 0.05

# Calcul et affichage du gain annuel
gain_annuel = montant_initial * taux_rendement
print(f"Gain annuel : {gain_annuel}")

# Augmentation du capital et du taux de rendement
montant_initial += 5000
taux_rendement += 0.02

# Calcul et affichage du nouveau gain annuel
gain_annuel = montant_initial * taux_rendement
print(f"Gain annuel après augmentation : {gain_annuel}")

# Retrait de 10% du montant total et diminution du rendement de 1%
montant_initial *= 0.9
taux_rendement -= 0.01

# Calcul et affichage du gain final
gain_final = montant_initial * taux_rendement
print(f"Gain final : {gain_final}")
