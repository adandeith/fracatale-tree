import os
import sys
from random import randint

file_dir = os.path.dirname(__file__) #récupère le dossier du fichier actuel
sys.path.append(file_dir) #set le chemin d'execution au dossier actuel

from inputBox import InputBox

#règle du système L
base = "XY"
chr1, rule1 = "X", "F[@[-X]+X]"

#paramètres de générations
maxi = 13
mini = 8
nbGens=0 #on demande ensuite à l'utilisateur de choisir un chiffre

#paramètres de dessin
epaisseur = 20
step = 85
angle = lambda: randint(0, 45) #crée une minie fonction, l'angle sera différent à chaque appel
color =[0.35, 0.2, 0.0]
stack=[]


def apply_rules (base : str) -> str :
    return ''.join([rule1 if char == chr1 else char for char in base])
    #autre solution, renvoyer une chaine que l'on concatène à chaque itération (for char in base if char == chr1 : chaine =+ rule1 else chaine += char)



def get_instructions (nbGens : int , base : str) -> str :
    #global base #on fait appel à la variable base globale
    for gen in range(nbGens):
        base = apply_rules(base) #la valeur de base est remplacée par la valeur de chaine
    return base

def check_validity (number, mini, maxi) -> bool :
    if number not in range(mini, maxi+1, 1):
        return False
    else:
        return True


#récuperation du nombre de générations
while not check_validity(nbGens, mini, maxi) :
    try :
        nbGens = int(InputBox(texte_principal='Combien de générations souhaitez-vous lancer ?', texte_secondaire=f'Merci de renseigner un chiffre de {mini} à {maxi}').userinput)
    except :
        nbGens = int(InputBox(texte_principal='Combien de générations souhaitez-vous lancer ?', texte_secondaire=f'Votre saisie était incorrecte. Merci de renseigner un chiffre de {mini} à {maxi}').userinput)


instructions = get_instructions(nbGens, base)


#opens the drawing turtle screen and sets the bases
from settings import Canva
canva = Canva()
draw = canva.draw
draw.left(90)
draw.pensize(epaisseur)

try :
    for chr in instructions :
        draw.color(color)
        if chr == "X" or chr == "F" :
            draw.forward(step)
        elif chr == '-' :
            angle_tortue = angle()
            draw.left(angle_tortue)
        elif chr == '+' :
            angle_tortue = angle()
            draw.right(angle_tortue)
        elif chr == '[':
            saved_pos = draw.pos() #sauvegarde la position
            saved_angle = draw.heading() #savuagarde de l'angle 
            stack.append((saved_pos, saved_angle, epaisseur, step, color[1]))
        elif chr == ']':
            saved_pos, saved_angle, epaisseur, step, color[1] = stack.pop()
            draw.pensize(epaisseur)
            draw.setheading(saved_angle)
            draw.penup() #pour se déplacer sans dessiner 
            draw.goto(saved_pos) #va à la position sauvegardée
            draw.pendown()
        elif chr == '@':
            step -= 6
            color[1] += 0.04
            epaisseur -= 2
            epaisseur = max(1, epaisseur) #pour éviter d'avoir une épaisseur inférieure à 1
            draw.pensize(epaisseur)
    canva.close()

except :
    pass
    


