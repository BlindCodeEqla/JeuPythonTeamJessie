def personnage():
    import time
    delai= 0.5
    print("CREATION DE PERSONNAGE")
    time.sleep(delai)
    
    nom= input("Chois ton nom: ")
    time.sleep(delai)
    
    sexe= input("Choisis ton sexe (H - F - X): ")
    time.sleep(delai)
    while sexe != "H" and sexe != "F" and sexe != "X":
        sexe= input("Ce choix est incorrect, choisis ton sexe (H - F - X) :")
        time.sleep(delai)
    if sexe=="H":
        sexe= "Un homme"
    if sexe=="F":
        sexe= "Une femme"
    if sexe== "X":
        sexe= "Une personne d'un genre autre"
        
    age= input("Choisis ton âge: ")
    time.sleep(delai)
    while not age.isnumeric() :
        age= input("Ce n'est pas un nombre, choisi ton âge: ")
        time.sleep(delai)
        
    cheveux= input("Choisis ta couleur de cheveux, tape la lettre correspondante à ton choix):\na) Blonds\nb) Châtains\nc) Bruns\nd) Noirs\ne) Roux\nf) Blancs\n")
    time.sleep(delai)
    while cheveux!= "a" and cheveux!="b" and cheveux!="c" and cheveux!="d" and cheveux!="e" and cheveux!="f":
        cheveux=input("Ce choix est incorrect, choisis ta couleur de cheveux: ")
        time.sleep(delai)
    if cheveux=="a":
        cheveux="blonds"
    if cheveux=="b":
        cheveux="châtains"
    if cheveux=="c":
        cheveux="bruns"
    if cheveux=="d":
        cheveux="noirs"
    if cheveux=="e":
        cheveux="roux"
    if cheveux=="f":
        cheveux="blancs"
    
    print("Tu es "+ nom+". " +sexe+" de "+age+" ans aux cheveux "+cheveux+".")
    time.sleep(delai)
    
    creation= input("Es-tu satisfait de ton choix? Tape \"oui\" pour commencer le jeu ou \"non\" pour recommencer la création de personnage: ")
    while creation!="oui" and creation!="non":
        creation= input("Choix incorrect, tape \"oui\" ou \"non\" pour continuer ou recommencer la création de eprsonnage: ")
    if creation== "non":
        personnage()
    
