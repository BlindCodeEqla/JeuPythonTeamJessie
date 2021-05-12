
from fonctions import *
import personnage
from story import *
import time
print(story("presentation"))

# personnage.personnage()

print(story("debut"))



while(True):
    if not(Chance_Eleochat()):
        break

while(True):
    if not(Chance_Maximoum()):
        break

while(True):
    print(story("Harielle"))
    if not(Swap("Blindcode")):
        break

print(story("ifhariellewin"))







