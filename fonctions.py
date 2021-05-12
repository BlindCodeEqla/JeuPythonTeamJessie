import random
from story import *
def Chance_Eleochat():
	print(story(Eleonore))
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
	print("Enfin! te voilà! Il était temps!  \n Je suis maximoum le Maître des dés. \n lance les dés et si ton score est supérieur à 6, tu pourras continuer l'aventure.dans le cas contraire, tu devras retenter ta chance une autre fois.")

	input("Fais enter pour re(lancer) les dés")
	_number = random.randint(1, 12) 
	print(f"vous avez lancé le dé sur {_number}")
	if _number > 6:
		print(f"Vous avez gagné {_number} est bien plus grand que 6, tu continue l'aventure")
		return False 
	elif _number < 6: 
		print(f"tu as perdu, car {_number} est plus petit que 6")
		return True 

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




def enigm(goodanswer):
	userinput=input(story(enigmgohnny))
	if userinput==goodanswer:
		print(story(ifjohnnywin))
		return False 
	else:
		return True
		
>>>>>>> 7bbe7d31c10480934ee30ec4b2b5aef56b00ad18

	
	



# Swap("Blindcode")


# Guess_number()