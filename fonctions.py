import random
from story import *
def Chance_Eleochat():
	print(story("Eleonore"))
	input("\n Fais enter pour (re)lancer les dés")
	_number = random.randint(1, 2)
	
	if _number == 1:
		print("\n Le choix s'est porté sur la boule au chocolat")
		print("Tu as gagné")
		return False
	else:
		print("\nLe choix s'est porté sur la boule de pistache")
		print("Tu as perdu")
		return True

def Chance_Maximoum():
	print(story("maximoum"))
	input("Fais enter pour re(lancer) les dés")
	_number = random.randint(1, 12) 
	print(f"vous avez lancé le dé sur {_number}")
	if _number > 6:
		print(f"Vous avez gagné {_number} est bien plus grand que 6, tu continue l'aventure")
		return False 
	elif _number < 6: 
		print(f"tu as perdu, car {_number} est plus petit que 6")
		return True 

def jessie():
    porte= input("Choisis la bonne porte, tape \"gauche\" ou \"droite\" pour choisir l'une des portes: ")
    if porte== "gauche":
        print("En ouvrant la porte, une avalanche de FATAL ERROR t'ensevelis...tu as perdu.")
        return True
    if porte== "droite":
        print("Tu as trouvé la bonne porte, tu peux continuer l'aventure!")
        return False
        
def Swap(_word):  
	_original = _word.upper()
	_anagram = list(_word)
	print(_anagram)
	_anagram = random.shuffle(_anagram)
	print(_anagram)
	

def Guess_number_sup(): 
	_number = random.randint(1,12)
	try:
		_user = int(input("Entre un chiffre entre 1 et 12"))
	except ValueError:
		print("C'est un chiffre qu'il faut entrer !")

def Guess_word(_word):
	pass




def enigm(goodanswer):
	userinput=input(story(enigmgohnny))
	if userinput==goodanswer:
		print(story(ifjohnnywin))
		return False 
	else:
		return True
		

	
	



# Swap("Blindcode")


