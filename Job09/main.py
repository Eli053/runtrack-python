# Initialisation des variables du produit
nom = "Produit A"
prix_unitaire = 10.0
quantite_en_stock = 100

# Affichage des informations du produit
print(f"Nom du produit : {nom}")
print(f"Prix unitaire : {prix_unitaire}")
print(f"Quantité en stock : {quantite_en_stock}")

# Ajout de produits en stock
quantite_achat = int(input("Entrez la quantité de produits que vous souhaitez acheter : "))
quantite_en_stock += quantite_achat

# Augmentation du prix du produit de 10%
prix_unitaire *= 1.1

# Affichage des informations du produit après mise à jour
print(f"Nom du produit : {nom}")
print(f"Prix unitaire : {prix_unitaire}")
print(f"Quantité en stock : {quantite_en_stock}")
