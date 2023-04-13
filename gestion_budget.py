# donnons la depense
def la_depense(montant, la_depense):
    la_depense.append(montant)
    print("la dépense est ajoutées", montant)
   
# donnons le revenu 
def le_revenu(montant, le_revenu):
    le_revenu.append(montant)
    print("le revenu est vérifié:", montant)
    
#liste
la_depense = []
le_revenu = []

# donnons la différence qui existe
def ecart(la_depense, le_revenu):
    depense_totale = sum(la_depense)
    revenu_totale = sum(le_revenu)
    ecart = revenu_totale-depense_totale
    print("la depense totale est:", depense_totale)
    print("le revenu total est :", revenu_totale)
    print("l'ecart qui existe est:", ecart)
    return ecart
   
While : True
print("       Bonjour comment vous allez ?      ")
print("                                         ")
print("   A) Remplissez la dépense")
print("   C) Consulter le revenu")
print("   E) Vérifier la difference entre la dépense et le revenu")
print("   0) quitter l'application")
choix = input("quel est votre désire:\n")
if choix == "A":
    montant = float(input("donnez le montant:"))
    print("la depense est :", montant)
elif choix == "C":
    montant = float(input("donnez le montant:"))
    print("le revenu est :", montant)
elif choix == "E":
    ecart(la_depense, le_revenu)
    print("l'ecart qui existe est :", la_depense, le_revenu)
elif choix == "0":
    print("Quitter")
    exit()
else:
    print("votre choix n'est pas reconnu" )


            