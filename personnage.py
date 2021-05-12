
def personnage():
    import time
    import sys
    print("CREATION DE PERSONNAGE")
    time.sleep(2)
    name= input("Choisissez votre nom: ")
    sexe= input("Choisissez votre sexe (H - F - X): ")
    while sexe != "H" and sexe != "F" and sexe != "X":
        sexe= input("Ce choix est incorrect, choisissez votre sexe (H - F - X) :")
        
    
personnage()